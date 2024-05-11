from tkinter import *
import csv



# resource
RICE = 100
WATER = 100


class Order_display:
#kitchen_screen
    def __init__(self):
        self.y_pos = 0
        self.flag =False
        self.root = Tk()
        self.root.geometry('1300x700')
        self.root.configure(background='#92efd3')
        self.root.title('Hotel Pandian')
        self.title = Label(self.root, text="ORDER", font=('arial', 32, 'bold'), background='#92efd3')
        self.title.place(x=580, y=20)
        self.resource_frame = Frame(self.root, bg='#c2fae9', height=550, width=450)
        self.resource_frame.place(x=800, y=100)
        self.rice_label = Label(self.resource_frame, text=f'RICE:{RICE} kg', font=('arial', 24, 'italic'), borderwidth=2, bg ='#dbfcf2')
        self.rice_label.place(x=50,y=50)
        self.order_frame = Frame(self.root, bg='#c2fae9', height=550, width=700 )
        self.order_frame.place(x=60, y=100)
        self.next_order_button = Button(text='next order',command=self.destroy,width=17,height=2,font=('arial', 10, 'italic'))
        self.next_order_button.place(x=1080,y=655)
        self.display()
        self.root.mainloop()


    def display(self):
            self.writing_in_frame('../customer_side/order.csv')


    def writing_in_frame(self,filename):
        # Open the CSV file in read mode
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.order = Label(self.order_frame, text=str(f' Order : {row[0]} , Quantity : {row[1]}'), font=('arial', 24, 'italic'), borderwidth=2, bg='#dbfcf2')
                self.order.place(x=10, y=self.y_pos)
                self.y_pos += 50

    def destroy(self):
        self.root.destroy()


c=Order_display()