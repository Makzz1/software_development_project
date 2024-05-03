import tkinter as tk
from tkinter import messagebox

class Login_page:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WELCOME TO ORDERDINE")
        self.user_name()
        self.password_button()
        self.login_button()

    def admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "2006":
            messagebox.showinfo("loginsuccessful", "welcome, {}".format(username))
        else:
            messagebox.showerror("login failed", "invalid username or password")

    def user_name(self):
        self.username_label = tk.Label(self.root, text="username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(padx=10, pady=10)

    def password_button(self):
        self.password_label = tk.Label(self.root, text="password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(padx=10, pady=10)
    def login_button(self):
        self.login_button = tk.Button(self.root, text="Login", command=self.admin_login)
        self.login_button.pack()
