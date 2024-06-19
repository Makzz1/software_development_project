from tkinter import *
import order_display
class admin_entry_page:

    def __init__(self):
        self.root = Tk()
        self.root.title("Hotel Pandian")
        self.root.geometry('952x636')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        self.image_path = 'adminpagephoto.png'

        try:
            self.img = PhotoImage(file=self.image_path)
            Label(self.root, image=self.img, bg="white").place(x=0, y=0)
        except TclError:
            print("Error: Image file not found or unsupported format.")

        #heading_label = Label(self.root, text="Hotel Pandian", font=("Verdana", 30))
        #heading_label.pack(pady=50)

        frame = Frame(self.root, width=400, height=450, bg="#F3E2C1",bd=2, relief=SOLID)
        frame.place(x=280, y=100)

        heading = Label(frame, text="Welcome admin", fg="black", bg="#F3E2C1", font=("Microsoft YaHei UI", 20, "bold"))
        heading.place(x=90, y=20)

        display_menu = Button(frame, text="Display menu", font=("Verdana", 12), bg='white', height=3, width=15, command = self.display_menu)
        display_menu.place(x=120, y=100)

        update_menu = Button(frame, text="Update menu", font=("Verdana", 12), bg='white', height=3, width=15,command=self.update_menu)
        update_menu.place(x=120, y=200)

        orders = Button(frame, text="Pending Orders", font=("Verdana", 12), bg='white', height=3, width=15,command=self.order)
        orders.place(x=120, y=300)

        logout = Button(self.root, text="Logout", font=("Verdana", 12, 'bold'), bg='#C33718', fg='white', height=2,
                        width=10, command=self.logout)
        logout.place(x=780, y=550)

        self.root.mainloop()

    def logout(self):
        self.root.destroy()
        import login_page

    def display_menu(self):
        import menu_kitchen
        self.root.destroy()
        menu_kitchen.Menu()
    def update_menu(self):
        import update_orders
        self.root.destroy()
        update_orders.Update()

    def order(self):
        self.root.destroy()
        order_display.Order_display()



if __name__ == '__main__':
    admin_entry_page()
