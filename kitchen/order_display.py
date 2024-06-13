import tkinter as tk
import csv

FONT = ('arial', 24, 'italic')

class Order_display:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1300x700')
        self.root.configure(background='#92efd3')
        self.root.title('Hotel Pandian')
        self.title = tk.Label(self.root, text="ORDER", font=('arial', 32, 'bold'), background='#92efd3')
        self.title.place(x=580, y=20)
        # order frame
        self.order_frame = tk.Frame(self.root, bg='#c2fae9', height=550, width=1200 )
        self.order_frame.place(x=60, y=100)
        # exit button
        self.exit_button = tk.Button(self.root, text='exit', font=('arial', 10, 'italic'), command=self.exit,width=14, height=2)
        self.exit_button.place(x=1150, y=655)
        # done button
        self.done_button = tk.Button(self.root, text ='done', font=('arial', 10, 'italic'),command=self.done_button_action , width=14, height=2 )
        self.done_button.place(x=1000,y=655)

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
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data_on_queue = {'order':{}}
            for row in reader:
                order = ''
                for i in row:
                    order += i + " "
                order_label = tk.Label(self.order_frame, text=str(f'Order : {order}'), font=('arial', 24, 'italic'), borderwidth=2, bg='#dbfcf2')
                order_label.place(x=10, y=self.y_pos)
                self.y_pos += 50

    def done_button_action(self):
        for widget in self.order_frame.winfo_children():
            widget.destroy()
        f = open('../customer_side/order.csv', 'r' , newline='')
        data = f.readlines()
        data.pop(0)
        f.close()
        f = open('../customer_side/order.csv', 'w' , newline='')
        print(data)
        for i in data:
            f.write((i))

        self.display_orders()

    def exit(self):
        self.root.destroy()
        import admin_entry_page
        admin_entry_page.admin_entry_page()


if __name__ == "__main__":
    order = Order_display()