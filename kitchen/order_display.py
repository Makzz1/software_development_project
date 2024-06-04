import tkinter as tk
import csv

FONT = ('arial', 24, 'italic')

# resource
RICE = 100
WATER = 100


class Order_display:
    def __init__(self):
        self.y_pos = 0
        self.root = tk.Tk()
        self.root.geometry('1300x700')
        self.root.configure(background='#92efd3')
        self.root.title('Hotel Pandian')
        self.title = tk.Label(self.root, text="ORDER", font=('arial', 32, 'bold'), background='#92efd3')
        self.title.place(x=580, y=20)
        # resource frame
        self.resource_frame = tk.Frame(self.root, bg='#c2fae9', height=550, width=450)
        self.resource_frame.place(x=800, y=100)
        self.rice_label = tk.Label(self.resource_frame, text=f'RICE:{RICE} kg', font=FONT, borderwidth=2, bg ='#dbfcf2')
        self.rice_label.place(x=50,y=50)
        # order frame
        self.order_frame = tk.Frame(self.root, bg='#c2fae9', height=550, width=700 )
        self.order_frame.place(x=60, y=100)
        #exit button
        self.exit_button = tk.Button(self.root, text='exit', font=('arial', 10, 'italic'), command=self.root.destroy,width=14, height=2)
        self.exit_button.place(x=1150, y=655)
        self.display_orders()
        self.root.mainloop()

    def display_orders(self):
        self.y_pos = 0
        print('check case')
        self.writing_in_frame('../customer_side/order.csv')
        self.root.after(5000, self.display_orders)  # Display orders every 5 seconds

    def writing_in_frame(self, filename):
        for widget in self.order_frame.winfo_children():
            widget.destroy()  # Clear previous orders
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                order = tk.Label(self.order_frame, text=str(f' Order : {row[0]} , Quantity : {row[1]}'), font=('arial', 24, 'italic'), borderwidth=2, bg='#dbfcf2')
                order.place(x=10, y=self.y_pos)
                self.y_pos += 50


if __name__ == "__main__":
    order = Order_display()




