from tkinter import *

FONT = ('times new roman', 21, 'italic')

class Menu:
    def __init__(self):
        self.b, self.l ,self.d = -1,-1,-1
        self.window = Tk()
        self.window.title("Pandian Restaurant")
        self.window.minsize(width=300, height=300)
        self.window.geometry("952x636")
        self.window.configure(bg="white")
        self.window.resizable(False, False)
        self.image_path = 'menu_background.jpg'

        try:
            self.img = PhotoImage(file=self.image_path)
            Label(self.window, image=self.img, bg="white").place(x=0, y=69)
        except TclError:
            print("Error: Image file not found or unsupported format.")

        self.canvas = Canvas(self.window, width=952, height=125, background='#DCF6E9')
        self.canvas.pack()
        self.canvas.create_text(500, 10, anchor=N, text="HOTEL PANDIAN", fill='#250220', font=('georgia', 56, 'italic'))

        # buttons
        self.breakfast = Button(self.window, text="Breakfast", font=FONT, command=self.breakfast_screen)
        self.breakfast.place(x=100, y=180)
        self.lunch = Button(self.window, text='Lunch', font=FONT, command=self.lunch_screen)
        self.lunch.place(x=430, y=180)
        self.dinner = Button(self.window, text='Dinner', font=FONT, command=self.dinner_screen)
        self.dinner.place(x=750, y=180)

        # exit button
        self.exit_button = Button(self.window, text='back', font=('arial', 11, 'italic'), command=self.exit, width=14,
                                  height=2, bg='#cc0000', fg='white')
        self.exit_button.place(x=400, y=515)

        self.window.mainloop()

    def breakfast_screen(self):
        self.b *= -1
        if self.b == 1:
            self.breakfast_frame = Frame(self.window, height=200, width=200)
            self.breakfast_frame.place(x=50, y=300)
            v_scrollbar = Scrollbar(self.breakfast_frame, orient=VERTICAL)
            v_scrollbar.grid(row=0, column=1, sticky='ns')

            # create the Text widget and link it with the scrollbar
            b_text = Text(self.breakfast_frame, width=20, height=7, font=('times new roman', 18, 'italic'),
                          yscrollcommand=v_scrollbar.set, wrap=WORD)
            b_text.grid(row=0, column=0)

            # configuring the scrollbars to work with the Text widget
            v_scrollbar.config(command=b_text.yview)
            b_text.tag_configure('heading', background='lightgrey')
            b_text.tag_configure('item', background='white')

            # Read breakfast data
            with open('breakfast.csv', 'r') as breakfast:
                data = breakfast.readlines()

            # Initialize item categories
            available_items_list = []
            not_available_items_list = []

            for i in data[1:]:
                j = i.split(',')
                item_name,item_price,item_status= j[0],j[1],j[2].strip()

                if item_status.lower() == 'true':
                    available_items_list.append(f'{item_name} - {item_price}')
                else:
                    not_available_items_list.append(f'{item_name} - {item_price}')

            # Insert items into the Text widget
            if available_items_list:
                b_text.insert(END, 'Available items\n', 'heading')
                for item in available_items_list:
                    b_text.insert(END, f'{item}\n', 'item')

            if not_available_items_list:
                b_text.insert(END, 'Not available items\n', 'heading')
                for item in not_available_items_list:
                    b_text.insert(END, f'{item}\n', 'item')

            b_text.config(state=DISABLED)
        else:
            if self.breakfast_frame:
                self.breakfast_frame.destroy()
                self.breakfast_frame = None

    def lunch_screen(self):
        self.l *= -1
        if self.l == 1:
            self.lunch_frame = Frame(self.window, height=200, width=200)
            self.lunch_frame.place(x=350, y=300)
            v_scrollbar = Scrollbar(self.lunch_frame, orient=VERTICAL)
            v_scrollbar.grid(row=0, column=1, sticky='ns')

            l_text = Text(self.lunch_frame, width=20, height=7, font=('times new roman', 18, 'italic'),
                          yscrollcommand=v_scrollbar.set, wrap=WORD)
            l_text.grid(row=0, column=0)

            v_scrollbar.config(command=l_text.yview)
            l_text.tag_configure('heading', background='lightgrey')
            l_text.tag_configure('item', background='white')

            with open('lunch.csv', 'r') as lunch:
                data = lunch.readlines()

            available_items_list = []
            not_available_items_list = []

            for i in data[1:]:
                j = i.split(',')
                item_name, item_price, item_status = j[0], j[1], j[2].strip()

                if item_status.lower() == 'true':
                    available_items_list.append(f'{item_name} - {item_price}')
                else:
                    not_available_items_list.append(f'{item_name} - {item_price}')

            if available_items_list:
                l_text.insert(END, 'Available items\n', 'heading')
                for item in available_items_list:
                    l_text.insert(END, f'{item}\n', 'item')

            if not_available_items_list:
                l_text.insert(END, 'Not available items\n', 'heading')
                for item in not_available_items_list:
                    l_text.insert(END, f'{item}\n', 'item')

            l_text.config(state=DISABLED)
        else:
            if self.lunch_frame:
                self.lunch_frame.destroy()
                self.lunch_frame = None

    def dinner_screen(self):
        self.d *= -1
        if self.d == 1:
            self.dinner_frame = Frame(self.window, height=200, width=200)
            self.dinner_frame.place(x=650, y=300)
            v_scrollbar = Scrollbar(self.dinner_frame, orient=VERTICAL)
            v_scrollbar.grid(row=0, column=1, sticky='ns')

            d_text = Text(self.dinner_frame, width=20, height=7, font=('times new roman', 18, 'italic'),
                          yscrollcommand=v_scrollbar.set, wrap=WORD)
            d_text.grid(row=0, column=0)

            v_scrollbar.config(command=d_text.yview)
            d_text.tag_configure('heading', background='lightgrey')
            d_text.tag_configure('item', background='white')

            with open('dinner.csv', 'r') as dinner:
                data = dinner.readlines()

            available_items_list = []
            not_available_items_list = []

            for i in data[1:]:
                j = i.split(',')
                item_name, item_price, item_status = j[0], j[1], j[2].strip()

                if item_status.lower() == 'true':
                    available_items_list.append(f'{item_name} - {item_price}')
                else:
                    not_available_items_list.append(f'{item_name} - {item_price}')

            if available_items_list:
                d_text.insert(END, 'Available items\n', 'heading')
                for item in available_items_list:
                    d_text.insert(END, f'{item}\n', 'item')

            if not_available_items_list:
                d_text.insert(END, 'Not available items\n', 'heading')
                for item in not_available_items_list:
                    d_text.insert(END, f'{item}\n', 'item')
                j = i.split(',')
                item_name, item_price, item_status = j[0], j[1], j[2].strip()

            d_text.config(state=DISABLED)
        else:
            if self.dinner_frame:
                self.dinner_frame.destroy()
                self.dinner_frame = None

    def exit(self):
        self.window.destroy()
        import admin_entry_page
        admin_entry_page.admin_entry_page()


if __name__ == "__main__":
    menu = Menu()
