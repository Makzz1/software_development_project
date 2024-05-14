import tkinter as tk
from tkinter import Entry, Frame, Label, Button, messagebox
class Admin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hotel Pandian")
        self.root.geometry('925x500')
        image_path = 'photo.png'
        try:
            self.img = tk.PhotoImage(file=image_path)
            tk.Label(self.root, image=self.img, bg="white").place(x=0, y=0)
        except tk.TclError:
            print("Error: Image file not found or unsupported format.")

        self.frame = Frame(self.root, width=350, height=350, bg="white")
        self.frame.place(x=480, y=70)

        heading = Label(self.frame, text="sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=100, y=5)
        self.user_name()
        self.password()
        self.sign_up()

    def user_name(self):
        def on_enter(e):
            self.user.delete(0, "end")

        def on_leave(e):
            name = self.user.get()
            if name == "":
                self.user.insert(0, "username")

        self.user = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, "username")
        self.user.bind("<FocusIn>", on_enter)
        self.user.bind("<FocusOut>", on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

    def password(self):
        def on_enter(e):
            self.code.delete(0, "end")

        def on_leave(e):
            name = self.code.get()
            if name == "":
                self.code.insert(0, "password")

        self.code = Entry(self.frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, "password")
        self.code.bind("<FocusIn>", on_enter)
        self.code.bind("<FocusOut>", on_leave)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

    def signin(self):
        username = self.user.get()
        password = self.code.get()
        if username == "admin" and password == "1234":
            self.root.destroy()
            screen = tk.Toplevel()
            screen.title("app")
            screen.geometry("925x500+300+200")
            screen.config(bg="white")
            tk.Label(screen, text="welcome admin!!!", bg="#fff", font=("calibri(Body)", 50, "bold")).pack(expand=True)
            screen.mainloop()

        elif username != "admin" and password != "1234":
            messagebox.showerror("Invalid username and password")

        elif password != "1234":
            messagebox.showerror("Invalid password")

        elif username != "admin":
            messagebox.showerror("Invalid username")

    def sign_up(self):
        sign_up = Button(self.frame, width=6, text="sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8",command=self.signin)
        sign_up.place(x=150, y=200)