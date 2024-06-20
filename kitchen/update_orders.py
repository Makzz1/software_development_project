from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
import csv

FONT = ('Ailza Bright Demo', 13)
FONT2 = ('Ailza Bright Demo', 13)

class Update:
    def __init__(self):
        self.window = Tk()
        self.window.title("Pandian Restaurant")
        self.window.minsize(width=300, height=300)
        self.window.geometry("952x636")
        self.window.configure(bg='#DCF6E9')
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, width=952, height=120, background='#c1e8f7')
        self.canvas.pack()
        self.canvas.create_text(480, 40, anchor=N, text="HOTEL PANDIAN", fill='#250220', font=('georgia', 35, 'italic'))

        self.add_item_button = Button(text="Add Item", font=FONT2, width=15, bg='blue', fg='white', height=2,
                                      command=self.add_item_screen)
        self.add_item_button.place(x=100, y=150)
        self.delete_item_button = Button(text="Delete Item", font=FONT2, width=15, bg='blue', fg='white', height=2,
                                         command=self.delete_item_screen)
        self.delete_item_button.place(x=300, y=150)
        self.update_item_button = Button(text="Update Item", font=FONT2, width=15, bg='blue', fg='white', height=2,
                                         command=self.update_item_screen)
        self.update_item_button.place(x=500, y=150)

        logout = Button(text="Back", font=FONT2, bg='red', fg='white', height=2, width=15, command=self.back)
        logout.place(x=700, y=150)
        self.window.mainloop()

    def display_buttons(self):

        if hasattr(self, 'menu_frame') and self.menu_frame.winfo_exists():
            self.menu_frame.destroy()

        self.menu_frame = Frame(self.window, height=350, width=850, background='#fce8e9')
        self.menu_frame.place(x=50, y=250)

        try:
            self.image = PhotoImage(file='wave.png')
            Label(self.menu_frame, image=self.image, bg="white").place(x=0, y=0)
        except TclError:
            print("Error: Image file not found or unsupported format.")

        self.breakfast_button = Button(self.menu_frame, text="Breakfast", width=15, height=2, font=FONT,
                                       command=self.breakfast_screen)
        self.breakfast_button.place(x=10, y=30)
        self.lunch_button = Button(self.menu_frame, text='Lunch', width=15, height=2, font=FONT,
                                   command=self.lunch_screen)
        self.lunch_button.place(x=10, y=130)
        self.dinner_button = Button(self.menu_frame, text='Dinner', width=15, height=2, font=FONT,
                                    command=self.dinner_screen)
        self.dinner_button.place(x=10, y=230)

    def configure_treeview_style(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview.Heading",font=('Ailza Bright Demo', 15, 'bold'),foreground='blue')
        style.configure("Treeview",font=('Ailza Bright Demo', 15),background='white',foreground='black',fieldbackground='white')
    def breakfast_screen(self):
        self.hide_all_tables()
        self.breakfast_table = ttk.Treeview(self.menu_frame, columns=("Item Name", "Price", "Availability"),
                                             show='headings', style=self.configure_treeview_style())
        self.breakfast_table.heading("Item Name", text="Item Name")
        self.breakfast_table.heading("Price", text="Price")
        self.breakfast_table.heading("Availability", text="Availability")
        self.breakfast_table.place(x=220, y=20)
        self.load_menu('breakfast.csv', self.breakfast_table)

    def lunch_screen(self):
        self.hide_all_tables()
        self.lunch_table = ttk.Treeview(self.menu_frame, columns=("Item Name", "Price", "Availability"),
                                         show='headings', style=self.configure_treeview_style())
        self.lunch_table.heading("Item Name", text="Item Name")
        self.lunch_table.heading("Price", text="Price")
        self.lunch_table.heading("Availability", text="Availability")
        self.lunch_table.place(x=220, y=20)
        self.load_menu('lunch.csv', self.lunch_table)

    def dinner_screen(self):
        self.hide_all_tables()
        self.dinner_table = ttk.Treeview(self.menu_frame, columns=("Item Name", "Price", "Availability"),
                                          show='headings', style=self.configure_treeview_style())
        self.dinner_table.heading("Item Name", text="Item Name")
        self.dinner_table.heading("Price", text="Price")
        self.dinner_table.heading("Availability", text="Availability")
        self.dinner_table.place(x=220, y=20)
        self.load_menu('dinner.csv', self.dinner_table)


    def hide_all_tables(self):
        if hasattr(self, 'breakfast_table') and self.breakfast_table.winfo_exists():
            self.breakfast_table.destroy()
        if hasattr(self, 'lunch_table') and self.lunch_table.winfo_exists():
            self.lunch_table.destroy()
        if hasattr(self, 'dinner_table') and self.dinner_table.winfo_exists():
            self.dinner_table.destroy()

        if hasattr(self, 'add_item_frame') and self.add_item_frame.winfo_exists():
            self.add_item_frame.destroy()

    def load_menu(self, filename, table):
        for i in table.get_children():
            table.delete(i)
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        item_name = row['item_name']
                        price = row['price']
                        availability = row['availability']
                        table.insert('', END, values=(item_name, price, availability))
                    except KeyError as e:
                        print(f"KeyError: {e}. The row data is {row}")
                        messagebox.showwarning("File Format Error", f"Missing column in CSV file: {e}")
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", f"The file {filename} does not exist.")
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"An error occurred while loading the menu: {e}")

    def get_selected_table(self):
        if hasattr(self, 'breakfast_table') and self.breakfast_table.winfo_exists() and self.breakfast_table.winfo_ismapped():
            return 'breakfast.csv', self.breakfast_table
        elif hasattr(self, 'lunch_table') and self.lunch_table.winfo_exists() and self.lunch_table.winfo_ismapped():
            return 'lunch.csv', self.lunch_table
        elif hasattr(self, 'dinner_table') and self.dinner_table.winfo_exists() and self.dinner_table.winfo_ismapped():
            return 'dinner.csv', self.dinner_table
        else:
            return None, None

    def back(self):
        self.window.destroy()
        import admin_entry_page
        admin_entry_page.admin_entry_page()

    def add_item_screen(self):
        if hasattr(self, 'add_item_frame') and self.add_item_frame.winfo_exists():
            self.add_item_frame.destroy()
            return

        if hasattr(self,'menu_frame') and self.menu_frame.winfo_exists():
            self.menu_frame.destroy()

        if hasattr(self, 'update_item_frame') and self.update_item_frame.winfo_exists():
            self.update_item_frame.destroy()

        self.add_item_frame = Frame(self.window, height=350, width=850, background='#c1e8f7')
        self.add_item_frame.place(x=50, y=250)

        try:
            self.image = PhotoImage(file='wave.png')
            Label(self.add_item_frame, image=self.image, bg="white").place(x=0, y=0)
        except TclError:
            print("Error: Image file not found or unsupported format.")

        self.item_name_var = StringVar()
        self.price_var = DoubleVar()
        self.availability_var = StringVar()
        self.category_var = StringVar()

        Label(self.add_item_frame, text="Enter the item name:", font=('Ailza Bright Demo', 14), bg='#c1e8f7').place(x=250,y=50)
        Entry(self.add_item_frame, textvariable=self.item_name_var, width=30,insertwidth= 2).place(x=480,y=50)
        Label(self.add_item_frame, text="Enter the price:", font=('Ailza Bright Demo', 14), bg='#c1e8f7').place(x=250,y=100)
        Entry(self.add_item_frame, textvariable=self.price_var, width=30,insertwidth=2).place(x=480,y=100)
        Label(self.add_item_frame, text="Select the availability:", font=('Ailza Bright Demo', 14),bg='#c1e8f7').place(x=250, y=150)
        self.availability_combobox = Combobox(self.add_item_frame, textvariable=self.availability_var,values=['True', 'False'], state='readonly', width=27)
        self.availability_combobox.place(x=480, y=150)

        Label(self.add_item_frame, text="Choose Category:", font=('Ailza Bright Demo', 14), bg='#c1e8f7').place(x=250,y=200)
        OptionMenu(self.add_item_frame, self.category_var, "Breakfast", "Lunch", "Dinner").place(x=480,y=200)


        Button(self.add_item_frame, text="Add", font=('Ailza Bright Demo', 11), width=10, height=2, command=self.add_item, fg='white', bg='blue').place(x=400,y=270)



    def add_item(self):
        category = self.category_var.get()

        if not category:
            messagebox.showwarning("Selection Error", "Please choose a category")
            return

        filename = ''
        table = None
        if category == 'Breakfast':
            filename = 'breakfast.csv'
        elif category == 'Lunch':
            filename = 'lunch.csv'
        elif category == 'Dinner':
            filename = 'dinner.csv'

        item_name = self.item_name_var.get()
        price = self.price_var.get()
        availability = self.availability_var.get()

        import csv
        from tkinter import messagebox

        if item_name and price and availability:
            try:
                with open(filename, mode='a', newline='') as file:
                    fieldnames = ['item_name', 'price', 'availability']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    # Check if the file is empty to write the header only if needed
                    file_is_empty = file.tell() == 0
                    if file_is_empty:
                        writer.writeheader()
                    writer.writerow({'item_name': item_name, 'price': price, 'availability': availability})

                messagebox.showinfo("Success", "Item added successfully")
                self.add_item_frame.destroy()
            except FileNotFoundError:
                with open(filename, mode='w', newline='') as file:
                    fieldnames = ['item_name', 'price', 'availability']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow({'item_name': item_name, 'price': price, 'availability': availability})

                messagebox.showinfo("Success", "Item added successfully")
                self.add_item_frame.destroy()

        else:
            messagebox.showwarning("Input Error", "All fields are required")

    def delete_item_screen(self):
        self.display_buttons()
        self._label = Label(self.menu_frame, text='Choose an item to delete ',height=2,font=('Ailza Bright Demo',15),bg='#c1e8f7')
        self._label.place(x=330,y=270)
        self.delete = Button(self.menu_frame, text='Delete', command=self.delete_item, height=2, width=10, font=FONT2, bg='blue', fg='white')
        self.delete.place(x=600, y=270)

    def delete_item(self):
        filename, table = self.get_selected_table()
        if not filename:
            messagebox.showwarning("Selection Error", "No category selected")
            return

        selected_item = table.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "No item selected")
            return

        item_name = table.item(selected_item)['values'][0]
        menu_data = []
        item_found = False

        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['item_name'] != item_name:
                        menu_data.append(row)
                    else:
                        item_found = True
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", f"The file {filename} does not exist.")
            return

        if not item_found:
            messagebox.showwarning("Item Not Found", "The selected item does not exist in the menu.")
            return

        with open(filename, mode='w', newline='') as file:
            fieldnames = ['item_name', 'price', 'availability']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(menu_data)

        self.load_menu(filename, table)
        messagebox.showinfo("Success", "Item deleted successfully")

    def update_item_screen(self):
        self.hide_all_tables()
        self.display_buttons()

        self.Label = Label(self.menu_frame, text='Choose an item to update',height=2,font=('Ailza Bright Demo',15),bg='#c1e8f7')
        self.Label.place(x=330,y=270)
        self.update_button = Button(self.menu_frame, text="Update", font=('Ailza Bright Demo', 11), width=10, height=2,
                                    command=self.update_item, fg='white', bg='blue')
        self.update_button.place(x=600, y=270)
        self.update_button.config(state='disabled')


        def check_selection():
            if not self.window.winfo_exists():
                return
            filename, table = self.get_selected_table()
            if table and table.selection():
                selected_item = table.selection()
                item_name = table.item(selected_item)['values'][0]
                self.item_name_var = StringVar(value=item_name)
                self.price_var = DoubleVar()
                self.availability_var = StringVar()

                #Enable update button after a selection is made
                self.update_button.config(state='normal')

            #Re-checking after 100 milliseconds
            self.menu_frame.after(100, check_selection)

        check_selection()

    def update_item(self):
        filename, table = self.get_selected_table()
        self.update_item_frame = Frame(self.window, height=350, width=850, background='#c1e8f7')
        self.update_item_frame.place(x=50, y=250)

        try:
            self.image = PhotoImage(file='wave.png')
            Label(self.update_item_frame, image=self.image, bg="white").place(x=0, y=0)
        except TclError:
            print("Error: Image file not found or unsupported format.")

        self.hide_all_tables()
        self.menu_frame.destroy()

        if not filename:
            messagebox.showwarning("Selection Error", "No category selected")
            self.update_item_frame.destroy()
            return

        Label(self.update_item_frame, text="Update menu", font=('Ailza Bright Demo', 20, 'underline'), bg='#c1e8f7', fg='blue').place(x=350, y=30)
        Label(self.update_item_frame, text="Item name:", font=('Ailza Bright Demo', 14), bg='#c1e8f7').place(x=250,y=100)
        entry = Entry(self.update_item_frame, textvariable=self.item_name_var, font=('Ailza Bright Demo', 14),bg='#c1e8f7')
        entry.config(state='readonly')
        entry.place(x=480, y=100)

        Label(self.update_item_frame, text="Enter the new price:", font=('Ailza Bright Demo', 14), bg='#c1e8f7').place(x=250, y=150)
        Entry(self.update_item_frame, textvariable=self.price_var, width=30, insertwidth=4).place(x=480, y=150)

        Label(self.update_item_frame, text="Select the new availability:", font=('Ailza Bright Demo', 14),bg='#c1e8f7').place(x=250, y=200)
        self.availability_combobox = Combobox(self.update_item_frame, textvariable=self.availability_var,values=['True', 'False'], state='readonly', width=27)
        self.availability_combobox.place(x=480, y=200)

        def done():
            item_name = self.item_name_var.get()
            price = self.price_var.get()
            availability = self.availability_var.get() == 'True'  # Convert to boolean

            if item_name and price and availability is not None:
                menu_data = []
                item_found = False
                try:
                    with open(filename, mode='r', newline='') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if row['item_name'] == item_name:
                                row['price'] = price
                                row['availability'] = availability  # Boolean value
                                item_found = True
                            menu_data.append(row)
                except FileNotFoundError:
                    pass

                if not item_found:
                    messagebox.showwarning("Item Not Found", "The selected item does not exist in the menu.")
                    self.update_item_frame.destroy()
                    return

                with open(filename, mode='w', newline='') as file:
                    fieldnames = ['item_name', 'price', 'availability']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(menu_data)

                messagebox.showinfo("Success", "Item updated successfully")
                self.update_item_frame.destroy()
            else:
                messagebox.showwarning("Input Error", "All fields are required")
            self.menu_frame.destroy()

        Button(self.update_item_frame, text="Done", height=2, width=15, fg='white', bg='blue', command=done).place(x=650, y=250)

if __name__ =='__main__':
    Update()
