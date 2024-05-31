from tkinter import *
import csv

FONT = ('arial', 24, 'italic')

# resource
RICE = 100
WATER = 100


class Order_display:
#kitchen_screen
    def __init__(self):
        self.y_pos = 0
        self.flag = False
        self.display()


    def display(self):
        self.root = Tk()
        self.root.geometry('1300x700')
        self.root.configure(background='#92efd3')
        self.root.title('Hotel Pandian')
        self.title = Label(self.root, text="ORDER", font=('arial', 32, 'bold'), background='#92efd3')
        self.title.place(x=580, y=20)
        # resouce frame
        self.resource_frame = Frame(self.root, bg='#c2fae9', height=550, width=450)
        self.resource_frame.place(x=800, y=100)
        self.rice_label = Label(self.resource_frame, text=f'RICE:{RICE} kg', font=FONT, borderwidth=2, bg ='#dbfcf2')
        self.rice_label.place(x=50,y=50)
        # order frame
        self.order_frame = Frame(self.root, bg='#c2fae9', height=550, width=700 )
        self.order_frame.place(x=60, y=100)
        self.next_order_button = Button(self.root,text='next order',command=self.read_the_order_csv,width=14,height=2,font=('arial', 10, 'italic'))
        self.next_order_button.place(x=1000,y=655)
        self.exit_button = Button(self.root,text='exit',font=('arial', 10, 'italic'),command=self.root.destroy,width=14,height=2)
        self.exit_button.place(x=1150,y=655)
        self.writing_in_frame('../customer_side/order.csv')
        self.root.mainloop()


    def writing_in_frame(self,filename):
        # Open the CSV file in read mode
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.order = Label(self.order_frame, text=str(f' Order : {row[0]} , Quantity : {row[1]}'), font=('arial', 24, 'italic'), borderwidth=2, bg='#dbfcf2')
                self.order.place(x=10, y=self.y_pos)
                self.y_pos += 50

    def read_the_order_csv(self):
        self.root.destroy()
        self.y_pos = 0
        self.display()




if __name__ == "__main__":
    order = Order_display()