from tkinter import *
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

        heading_label = Label(self.root, text="Hotel Pandian", font=("Verdana", 30))
        heading_label.pack(pady=50)

        frame = Frame(self.root, width=350, height=350, bg="white")
        frame.place(x=300, y=180)

        heading = Label(frame, text="Welcome admin", fg="blue", bg="white", font=("Microsoft YaHei UI", 20, "bold"))
        heading.place(x=70, y=10)

        display_menu = Button(frame, text="Display menu", font=("Verdana", 12), bg='white', height=3, width=15)
        display_menu.place(x=100, y=70)

        update_menu = Button(frame, text="Update menu", font=("Verdana", 12), bg='white', height=3, width=15)
        update_menu.place(x=100, y=160)

        orders = Button(frame, text="Pending Orders", font=("Verdana", 12), bg='white', height=3, width=15,command=self.order)
        orders.place(x=100, y=250)

        logout = Button(self.root, text="Logout", font=("Verdana", 12, 'bold'), bg='red', fg='white', height=2,
                        width=10, command=self.logout)
        logout.place(x=800, y=40)

        self.root.mainloop()
    def order(self):
        import way_to_connect_login_order_page
    def logout(self):
        self.root.destroy()
        import login_page

if __name__ == '__main__':
    admin_entry_page()
