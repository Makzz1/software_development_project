from tkinter import *
import login_page
from customer_side import customer_page


def create_login_page():
    root.destroy()
    login = login_page.Admin()


def create_customer_page():
    root.destroy()
    customer = customer_page.Customer()


root=Tk()
root.title("WELCOME TO ORDERDINE")
root.geometry('852x536')
root.configure(bg='white')

image_path = 'photo.png'
image = PhotoImage(file=image_path)
image_label = Label(root,image=image)
image_label.place(x=0, y=0)

admin=Button(root, text="ADMIN", height=4, width=20,command=create_login_page)
admin.place(x=600,y=180)

customer=Button(root, text="CUSTOMER", height=4, width=20,command=create_customer_page)
customer.place(x=600,y=280)

root.columnconfigure(0,weight=1)
root.mainloop()