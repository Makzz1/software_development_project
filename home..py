from tkinter import *
import login_page
import customer_page

def create_login_page():
    login = login_page.Login_page()
    root.destroy()
def create_customer_page():
    customer = customer_page.Customer_page()
    root.destroy()

import tkinter.messagebox as messagebox

root=Tk()
root.title("Hotel Pandian")
root.geometry('820x600')
root.configure(bg="yellow")

image_path = "img.png"
image = PhotoImage(file=image_path)

# Create a label to display the image
image_label = Label(root, image=image)
image_label.place(x=60, y=100)

admin=Button(root, text="ADMIN", height=4, width=20,command=create_login_page,bg='pink', fg='black')
customer=Button(root, text="CUSTOMER", height=4, width=20,command = create_customer_page, bg='pink' , fg='black')


admin.place(x=600, y=180)
customer.place(x=600, y=280)

root.columnconfigure(0,weight=1)
root.mainloop()