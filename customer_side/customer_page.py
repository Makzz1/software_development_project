
from tkinter import *
from tkinter import messagebox
import customer_side.menu_customer
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Customer:
    def __init__(self,token):
        self.token = token

    def customer_login(self):
        self.root = Tk()
        self.root.title("login")
        self.root.geometry("952x636+50+50")
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        image_path = 'photo.png'
        try:
            img = PhotoImage(file=image_path)
            Label(self.root, image=img, bg="white").place(x=0, y=0)
        except TclError:
            print("Error: Image file not found or unsupported format.")

        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=180)

        heading = Label(self.frame, text="sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=100, y=5)
        self.name()
        self.contact()
        self.email_id()
        self.sign_up()
        self.root.mainloop()

    def name(self):
        def on_enter(e):
            self.Name.delete(0, "end")

        def on_leave(e):
            name = self.Name.get()
            if name == "":
                self.Name.insert(0, "Name")

        self.Name = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.Name.place(x=30, y=80)
        self.Name.insert(0, "Name")
        self.Name.bind("<FocusIn>", on_enter)
        self.Name.bind("<FocusOut>", on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

    def contact(self):
        def on_enter(e):
            self.contact_no.delete(0, "end")

        def on_leave(e):
            name = self.contact_no.get()
            if name == "":
                self.contact_no.insert(0, "contact_no")

        self.contact_no = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.contact_no.place(x=30, y=150)
        self.contact_no.insert(0, "contact_no")
        self.contact_no.bind("<FocusIn>", on_enter)
        self.contact_no.bind("<FocusOut>", on_leave)
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

    def email_id(self):
        def on_enter(e):
            self.address.delete(0, "end")

        def on_leave(e):
            name = self.address.get()
            if name == "":
                self.address.insert(0, "E mail")

        self.address = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.address.place(x=30, y=230)
        self.address.insert(0, "E-mail")
        self.address.bind("<FocusIn>", on_enter)
        self.address.bind("<FocusOut>", on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=250)

    def sign_up(self):
        sign_up = Button(self.frame, width=6, text="enter", border=0, bg="white", cursor="hand2", fg="#57a1f8",command=self.enter)
        sign_up.place(x=150, y=300)

    def enter(self):
        name = self.Name.get()
        phone_no = self.contact_no.get()
        email = self.address.get()
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if name and phone_no and email and name != "Name" and phone_no != "contact_no" and email != "E-mail":
            if re.match(email_regex, email):
                print('mail:', email)
                self.root.destroy()
                self.menu = customer_side.menu_customer.Menu(name, phone_no, email, self.token)
                self.menu.menu_page()
            else:
                messagebox.showerror(message='Invalid email address')
        else:
            messagebox.showerror(message='Please fill all the above boxes')



