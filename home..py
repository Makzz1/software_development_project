from tkinter import*
import login_page

def create_login_page():
    login = login_page.Login_page()
    root.destroy()


import tkinter.messagebox as messagebox
root=Tk()
root.title("WELCOME TO ORDERDINE")
root.geometry('400x350')

admin=Button(root, text="ADMIN", height=4, width=20,command=create_login_page)
admin.grid(row=0, column=0, padx=10, pady=10)

customer=Button(root, text="CUSTOMER", height=4, width=20)
customer.grid(row=1, column=0, padx=10, pady=10)

root.columnconfigure(0,weight=1)
root.mainloop()