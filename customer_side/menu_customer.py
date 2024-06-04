from tkinter import *

FONT = ('times new roman', 24, 'italic')


class Menu:
    def __init__(self):
        self.b = -1
        self.l = -1
        self.d = -1
        self.window = Tk()
        self.window.title("Pandian Restaurant")
        self.window.minsize(width=300, height=300)
        self.window.geometry("1200x563")
        self.window.configure(bg="white")
        self.window.resizable(False, False)
        self.image_path = 'pngtree-simple-summer-drink-menu-promotion-background-picture-image_1034454.jpg'

        try:
            self.img = PhotoImage(file=self.image_path)
            Label(self.window, image=self.img, bg="white").place(x=0, y=0)
        except TclError:
            print("Error: Image file not found or unsupported format.")

        self.canvas = Canvas(self.window, width=1200, height=120, background='#DCF6E9')
        self.canvas.pack()
        self.canvas.create_text(600, 10, anchor=N, text="HOTEL PANDIAN", fill='#250220', font=('georgia', 58, 'italic'))

        # button
        self.breakfast = Button(text="Breakfast", font=FONT, command=self.breakfast_screen)
        self.breakfast.place(x=300, y=200)
        self.lunch = Button(text='Lunch', font=FONT, command=self.lunch_screen)
        self.lunch.place(x=580, y=200)
        self.dinner = Button(text='Dinner', font=FONT, command=self.dinner_screen)
        self.dinner.place(x=840, y=200)
        self.add = Button(self.window, text='ADD', height=2, width=15, command=self.add_order)
        self.add.place(x=550, y=515)

        self.window.mainloop()

    def breakfast_screen(self):
        self.b *= -1
        if self.b == 1:
            self.breakfast_frame = Frame(self.window, height=200, width=200)
            self.breakfast_frame.place(x=280, y=300)
            self.breakfast = open('D:/pycharm/software_development_project/kitchen/breakfast.csv', 'r')
            b_listbox = Listbox(self.breakfast_frame, width=200, height=200, font=('times new roman', 18, 'italic'))
            b_listbox.place(x=0, y=0)
            data = self.breakfast.readlines()
            self.breakfast_data = []  # the data of breakfast are stored in this
            for i in data:
                j = i.split(',')
                print(j)
                self.breakfast_data.append(j)
                b_listbox.insert(0, f'{j[0]} Price:{j[1]}', )
        else:
            self.breakfast_frame.destroy()

    def lunch_screen(self):
        self.l *= -1
        if self.l == 1:
            self.lunch_frame = Frame(self.window, height=200, width=200)
            self.lunch_frame.place(x=540, y=300)
            self.lunch = open('D:/pycharm/software_development_project/kitchen/lunch.csv', 'r')
            l_listbox = Listbox(self.lunch_frame, width=200, height=200, font=('times new roman', 18, 'italic'))
            l_listbox.place(x=0, y=0)
            data = self.lunch.readlines()
            self.lunch_data = []  # the data of lunch are stored in this
            for i in data:
                j = i.split(',')
                self.lunch_data.append(j)
                l_listbox.insert(0, f'{j[0]} Price:{j[1]}')
        else:
            self.lunch_frame.destroy()

    def dinner_screen(self):
        self.d *= -1
        if self.d == 1:
            self.dinner_frame = Frame(self.window, height=200, width=200)
            self.dinner_frame.place(x=800, y=300)
            self.dinner = open('D:/pycharm/software_development_project/kitchen/dinner.csv', 'r')
            d_listbox = Listbox(self.dinner_frame, height=200, width=200, font=('times new roman', 18, 'italic'))
            d_listbox.place(x=0, y=0)
            data = self.dinner.readlines()
            self.dinner_data = []  # the data of dinner are stored in this
            for i in data:
                j = i.split(',')
                self.dinner_data.append(j)
                d_listbox.insert(0, f'{j[0]} Price:{j[1]}')
        else:
            self.dinner_frame.destroy()

    def add_order(self):
            if self.b_listbox.get(ANCHOR):
                data = self.b_listbox.get(ANCHOR)


if __name__ == "__main__":
    menu = Menu()