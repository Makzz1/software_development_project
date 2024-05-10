
from tkinter import *
import login_page
import customer_page

def create_login_page():
    login = login_page.Admin()
    root.destroy()
def create_customer_page():
    customer = customer_page.Customer()
    root.destroy()

import tkinter.messagebox as messagebox

root=Tk()
root.title("Hotel Pandian")
root.geometry('852x536')
root.configure(bg='white')

image_path = "photo.png"
image = PhotoImage(file=image_path)

# Create a label to display the image
image_label = Label(root, image=image)
image_label.place(x=0,y=0)

admin=Button(root, text="ADMIN", height=4, width=20,command=create_login_page,bg='#eda807', fg='black')
customer=Button(root, text="CUSTOMER", height=4, width=20,command = create_customer_page, bg='#eda807' , fg='black')


admin.place(x=600, y=180)
customer.place(x=600, y=280)

root.columnconfigure(0,weight=1)
root.mainloop()