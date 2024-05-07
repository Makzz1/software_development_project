import tkinter as tk
from tkinter import messagebox


class Customer_page:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WELCOME TO ORDERDINE")
        self.name()
        self.contact()
        self.address()
        self.login_button()
        self.root.geometry("500x500")

    def welcome(self):
        self.name = self.name_entry.get()
        self.contact = self.contact_entry.get()
        self.address = self.address_entry.get()

    def name(self):
        self.name_label = tk.Label(self.root, text="NAME:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

    def contact(self):
        self.contact_label = tk.Label(self.root, text="CONTACT NO:")
        self.contact_label.pack()
        self.contact_entry = tk.Entry(self.root)
        self.contact_entry.pack()

    def address(self):
        self.address_label = tk.Label(self.root, text="ADDRESS:")
        self.address_label.pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack()

    def login_button(self):
        login_button = tk.Button(self.root, text="Login", command=self.welcome)
        login_button.pack()