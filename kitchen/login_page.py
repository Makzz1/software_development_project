import tkinter as tk
from tkinter import Entry, Frame, Label, Button, messagebox
import admin_entry_page

IMAGE_PATH = 'adminpagephoto.png'

class Admin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hotel Pandian")
        self.root.geometry('952x636')
        self.root.resizable(False, False)

        try:
            self.img = tk.PhotoImage(file=IMAGE_PATH)
            tk.Label(self.root, image=self.img, bg="white").place(x=0, y=0)
        except tk.TclError:
            print("Error: Image file not found or unsupported format.")

        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=190)

        heading = Label(self.frame, text="sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=100, y=5)
        self.user_name()
        self.password()
        self.show_password = False
        self.sign_up()
        self.root.mainloop()

    def user_name(self):
        def on_enter(e):
            if self.user.get() == "username":
                self.user.delete(0, "end")

        def on_leave(e):
            if self.user.get() == "":
                self.user.insert(0, "username")

        self.user = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, "username")
        self.user.bind("<FocusIn>", on_enter)
        self.user.bind("<FocusOut>", on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

    def password(self):
        def on_enter(e):
            if self.code.get() == "password":
                self.code.delete(0, "end")
                self.code.config(show="*" if not self.show_password else "")

        def on_leave(e):
            if self.code.get() == "":
                self.code.insert(0, "password")
                self.code.config(show="")

        self.code = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, "password")
        self.code.bind("<FocusIn>", on_enter)
        self.code.bind("<FocusOut>", on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        self.toggle_button = Button(self.frame, text="Show", command=self.toggle_password, bg="white", cursor="hand2", fg="#57a1f8", border=0)
        self.toggle_button.place(x=260, y=145)

    def toggle_password(self):
        self.show_password = not self.show_password
        if self.show_password:
            self.code.config(show="")
            self.toggle_button.config(text="Hide")
        else:
            self.code.config(show="*" if self.code.get() != "password" else "")
            self.toggle_button.config(text="Show")

    def signin(self):
        username = self.user.get()
        password = self.code.get()
        if username == "admin" and password == "123456":
            self.root.destroy()
            admin_entry_page.admin_entry_page()
        elif username != "admin" and password != "123456":
            messagebox.showinfo('error', "Invalid username and password")
        elif password != "123456":
            messagebox.showinfo('error', "Invalid password")
        elif username != "admin":
            messagebox.showinfo('error', "Invalid username")

    def sign_up(self):
        sign_up = Button(self.frame, width=10, text="sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8",
                         command=self.signin)
        sign_up.place(x=150, y=210)

if __name__ == '__main__':
    l = Admin()
