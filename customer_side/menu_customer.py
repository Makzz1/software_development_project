from tkinter import *
import queue
import csv

FONT = ('times new roman', 24, 'italic')


class Menu:
    def __init__(self):
        self.b = -1
        self.l = -1
        self.d = -1
        self.breakfast_data = {}  # the data of breakfast are stored in this (dict)
        self.lunch_data = {}  # the data of lunch are stored in this (dict)
        self.dinner_data = {}  # the data of dinner are stored in this
        self.totalprice = 0
        self.queue_list = queue.Queue()
        self.window = Tk()
        self.window.title("Pandian Restaurant")
        self.window.minsize(width=300, height=300)
        self.window.geometry("1200x563")
        self.window.configure(bg="white")
        self.window.resizable(False, False)
        self.image_path = 'pngtree-simple-summer-drink-menu-promotion-background-picture-image_1034454.jpg'

        try:
            self.img = PhotoImage(file=self.image_path)
            Label(self.window, image=self.img, bg="white").place(x=0, y=0)
        except TclError:
            print("Error: Image file not found or unsupported format.")

        self.canvas = Canvas(self.window, width=1200, height=120, background='#DCF6E9')
        self.canvas.pack()
        self.canvas.create_text(600, 10, anchor=N, text="HOTEL PANDIAN", fill='#250220', font=('georgia', 58, 'italic'))

        # button
        self.breakfast = Button(text="Breakfast", font=FONT, command=self.breakfast_screen)
        self.breakfast.place(x=100, y=150)
        self.lunch = Button(text='Lunch', font=FONT, command=self.lunch_screen)
        self.lunch.place(x=380, y=150)
        self.dinner = Button(text='Dinner', font=FONT, command=self.dinner_screen)
        self.dinner.place(x=640, y=150)
        self.add = Button(self.window, text='ADD', height=2, width=15, command=self.add_order)
        self.add.place(x=400, y=515)
        self.remove = Button(self.window,text="REMOVE",height=2,width=15,command=self.remove_order)
        self.remove.place(x=550,y=515)
        self.order = Button(self.window,text="ORDER",height=2,width=15,command=self.place_order)
        self.order.place(x=700,y=515)

        #quntity roller
        self.quantity = Spinbox(self.window,from_=0,to=100,width=6)
        self.quantity.place(x=950,y=525)

        #your order frame
        self.order_frame = Frame(self.window,height=370,width=300)
        self.order_frame.place(x=850,y=130)
        self.order_frame_listbox = Listbox(self.order_frame,height=370,width=300,font=('times new roman', 18, 'italic'))
        self.order_frame_listbox.place(x=0,y=0)
        self.order_frame_listbox.insert(0,'ITEM     QUANTITY     PRICE')

        self.window.mainloop()

    def breakfast_screen(self):
        self.b *= -1
        if self.b == 1:
            self.breakfast_frame = Frame(self.window, height=200, width=200)
            self.breakfast_frame.place(x=80, y=230)
            self.breakfast = open('D:/pycharm/software_development_project/kitchen/breakfast.csv', 'r')
            self.b_listbox = Listbox(self.breakfast_frame, width=200, height=200, font=('times new roman', 18, 'italic'))
            self.b_listbox.place(x=0, y=0)
            data = self.breakfast.readlines()

            for i in data:
                j = i.split(',')
                self.breakfast_data[j[0]] = int(j[1])
                self.b_listbox.insert(0, f'{j[0]} Price:{j[1]}', )
            print(self.breakfast_data)

        else:
            self.breakfast_frame.destroy()

    def lunch_screen(self):
        self.l *= -1
        if self.l == 1:
            self.lunch_frame = Frame(self.window, height=200, width=200)
            self.lunch_frame.place(x=340, y=230)
            self.lunch = open('D:/pycharm/software_development_project/kitchen/lunch.csv', 'r')
            self.l_listbox = Listbox(self.lunch_frame, width=200, height=200, font=('times new roman', 18, 'italic'))
            self.l_listbox.place(x=0, y=0)
            data = self.lunch.readlines()

            for i in data:
                j = i.split(',')
                self.lunch_data[j[0]] = int(j[1])
                self.l_listbox.insert(0, f'{j[0]} Price:{j[1]}')
        else:
            self.lunch_frame.destroy()

    def dinner_screen(self):
        self.d *= -1
        if self.d == 1:
            self.dinner_frame = Frame(self.window, height=200, width=200)
            self.dinner_frame.place(x=600, y=230)
            self.dinner = open('D:/pycharm/software_development_project/kitchen/dinner.csv', 'r')
            self.d_listbox = Listbox(self.dinner_frame, height=200, width=200, font=('times new roman', 18, 'italic'))
            self.d_listbox.place(x=0, y=0)
            data = self.dinner.readlines()

            for i in data:
                j = i.split(',')
                self.dinner_data[j[0]] = int(j[1])
                self.d_listbox.insert(0, f'{j[0]} Price:{j[1]}')
        else:
            self.dinner_frame.destroy()

    def add_order(self):
        quantity = int(self.quantity.get())
        item, price = None, None
        if hasattr(self, 'b_listbox') and self.b_listbox.curselection():
            item = self.b_listbox.get(ANCHOR).split(' ')[0]
            price = self.breakfast_data[item]
        elif hasattr(self, 'l_listbox') and self.l_listbox.curselection():
            item = self.l_listbox.get(ANCHOR).split(' ')[0]
            price = self.lunch_data[item]
        elif hasattr(self, 'd_listbox') and self.d_listbox.curselection():
            item = self.d_listbox.get(ANCHOR).split(' ')[0]
            price = self.dinner_data[item]

        if item and price:
            self.order_frame_listbox.insert(END, f'{item}             {quantity}             {price * quantity}')
            self.totalprice += price * quantity

    def remove_order(self):
        selected = self.order_frame_listbox.curselection()
        if selected:
            item = self.order_frame_listbox.get(selected)
            item_price = int(item.split()[-1])
            self.totalprice -= item_price
            self.order_frame_listbox.delete(selected)

    def place_order(self):
        if self.totalprice > 0:
           self.confirm_frame =  Frame(self.window,height=300,width=350,bg='#B9F3E6')
           self.confirm_frame.place(x=450,y=100)

           title = Label(self.confirm_frame,text=f'confirm purchase\n {self.totalprice} ?',font=FONT,bg="#B9F3E6")
           title.place(x=70,y=5)
           confirm = Button(self.confirm_frame,text='confirm',height=2,width=12,command=self.confirm)
           confirm.place(x=80,y=130)
           back = Button(self.confirm_frame,text='back',height=2,width=12,command=self.back)
           back.place(x=180,y=130)

    def back(self):
        self.confirm_frame.destroy()

    def confirm(self):
        self.totalprice = 0
        data_to_write = {'order':{}}
        while self.order_frame_listbox.get(1):
            data = self.order_frame_listbox.get(1)
            self.order_frame_listbox.delete(1)
            data = data.split('             ')
            data_to_write['order'][data[0]] = int(data[1])
        print(data_to_write)
        self.queue_list.add(data_to_write)
        self.update_csv("order.csv")

    def update_csv(self,filename):
        # Open the CSV file in append mode
        with open(filename, 'w', newline='') as csvfile:
            for i in self.queue_list.order:
                print(i)
                writer = csv.writer(csvfile)
                writer.writerow(i['order'].items())
        self.confirm_frame.destroy()




if __name__ == "__main__":
    menu = Menu()