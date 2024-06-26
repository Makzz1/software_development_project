from tkinter import *
import json
from tkinter import messagebox
import customer_side.our_queue
from datetime import datetime
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FONT = ('times new roman', 24, 'italic')

class Menu:
    def __init__(self,name,phone,email,token):
        self.flag = True
        self.ordered_items = {}
        self.name = name
        self.phone = phone
        self.token = token
        self.email = email
        self.data_to_write = None
        self.b = -1
        self.l = -1
        self.d = -1
        self.breakfast_data = {}  # the data of breakfast are stored in this (dict)
        self.lunch_data = {}  # the data of lunch are stored in this (dict)
        self.dinner_data = {}  # the data of dinner are stored in this
        # time
        self.curent = datetime.now().time()
        self.hr = self.curent.hour
        self.min = self.curent.minute

    def menu_page(self):
        self.totalprice = 0
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
            self.breakfast = open('../kitchen/breakfast.csv', 'r')
            self.b_listbox = Listbox(self.breakfast_frame, width=200, height=200, font=('times new roman', 18, 'italic'))
            self.b_listbox.place(x=0, y=0)
            data = self.breakfast.readlines()

            for i in data[1:]:
                j = i.strip().split(',')
                item_name, price, availability = j[0], j[1], j[2] == 'True'
                self.breakfast_data[item_name] = float(price)
                if availability:
                    self.b_listbox.insert(0, f'{item_name} - {price}', )

        else:
            self.breakfast_frame.destroy()

    def lunch_screen(self):
        self.l *= -1
        if self.l == 1:
            self.lunch_frame = Frame(self.window, height=200, width=200)
            self.lunch_frame.place(x=340, y=230)
            self.lunch = open('../kitchen/lunch.csv', 'r')
            self.l_listbox = Listbox(self.lunch_frame, width=200, height=200, font=('times new roman', 18, 'italic'))
            self.l_listbox.place(x=0, y=0)
            data = self.lunch.readlines()

            for i in data[1:]:
                j = i.strip().split(',')
                item_name, price, availability = j[0], j[1], j[2] == 'True'
                self.lunch_data[item_name] = float(price)
                if availability:
                    self.l_listbox.insert(0, f'{item_name} - {price}', )
        else:
            self.lunch_frame.destroy()

    def dinner_screen(self):
        self.d *= -1
        if self.d == 1:
            self.dinner_frame = Frame(self.window, height=200, width=200)
            self.dinner_frame.place(x=600, y=230)
            self.dinner = open('../kitchen/dinner.csv', 'r')
            self.d_listbox = Listbox(self.dinner_frame, height=200, width=200, font=('times new roman', 18, 'italic'))
            self.d_listbox.place(x=0, y=0)
            data = self.dinner.readlines()
            for i in data[1:]:
                j = i.strip().split(',')
                item_name, price, availability = j[0], j[1], j[2] == 'True'
                self.dinner_data[item_name] = float(price)
                if availability:
                    self.d_listbox.insert(0, f'{item_name} - {price}', )
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

        if item and price and quantity != 0:
            self.order_frame_listbox.insert(END, f'{item}             {quantity}             {price * quantity}')
            self.ordered_items[item] = f'{item}-{quantity} : {price*quantity}'
            self.totalprice += price * quantity


    def remove_order(self):
        selected = self.order_frame_listbox.curselection()
        if selected:
            item = self.order_frame_listbox.get(selected)
            order = item.split('             ')[0]
            del self.ordered_items[order]
            item_price = float(item.split()[-1])
            self.totalprice -= item_price
            self.order_frame_listbox.delete(selected)

    def place_order(self):
        y=160
        if self.totalprice > 0:
           self.confirm_frame =  Frame(self.window,height=500,width=450,bg='white',borderwidth=2, relief="solid")
           self.confirm_frame.place(x=400,y=30)
           title1 = Label(self.confirm_frame,text=f'CONFIRM ORDER',font=FONT,bg="white")
           title1.place(x=90,y=20)
           title2 = Label(self.confirm_frame,text= ' Your Order : ',font=FONT,bg="white")
           title2.place(x=20,y=110)
           for order in self.ordered_items.values():
                items = Label(self.confirm_frame,text=f'{order}',font=FONT,bg="white")
                items.place(x=60,y=y)
                y += 50
           line = Label(self.confirm_frame,text=f'-----------------------------------',font=FONT,bg='white')
           line.place(x=20,y=y)
           price = Label(self.confirm_frame,text=f'Total : {self.totalprice}',font=FONT,bg='white')
           price.place(x=60,y=y+40)
           confirm = Button(self.confirm_frame,text='confirm',height=2,width=12,command=self.confirm)
           confirm.place(x=120,y=430)
           back = Button(self.confirm_frame,text='back',height=2,width=12,command=self.back)
           back.place(x=220,y=430)
           time_order = Label(self.confirm_frame,text=f'Time of the order {self.hr}:{self.min}',font=('times new roman', 12, 'italic'),bg='white')
           time_order.place(x=30,y=70)


    def back(self):
        self.confirm_frame.destroy()

    def confirm(self):
        self.data_to_write = {'order':{},'token':self.token,'name':self.name,'email':self.email}
        while self.order_frame_listbox.get(1):
            data = self.order_frame_listbox.get(1)
            self.order_frame_listbox.delete(1)
            data = data.split('             ')
            self.data_to_write['order'][data[0]] = int(data[1])
        self.update("order.json")

    def update(self,filename):
        self.dict = {}
        self.queue_list = customer_side.our_queue.Queue()

        self.send_email(self.email)
        if self.flag:
            try:
                with open(filename,'r') as file1:
                    content = json.load(file1)
                if content:
                    for i in content:
                        print('json:',content[i])
                        self.dict[int(i)] = (content[i])
            except:
                print('file is empty')


            self.dict[self.token] = self.data_to_write
            print(self.dict)
            for i in range(1,self.token+1):
                try:
                    self.queue_list.add(self.dict[i])
                except:
                    pass
            temp = self.queue_list.head
            data_items={}
            while temp:
                data = temp.value
                temp = temp.next
                data_items[data["token"]] = data

            print(data_items)

            with open("order.json","w") as file2:
                json.dump(data_items,file2)

            temp = self.queue_list.head
            with open("email.csv",'w',newline='') as csvfile1:
                writer = csv.writer(csvfile1)
                while temp:
                    data = temp.value
                    temp = temp.next
                    writer.writerow([data['email'], data['name']])

            self.token += 1

        self.window.destroy()
        self.totalprice = 0
        import customer_page
        customer_page = customer_page.Customer(self.token)
        customer_page.customer_login()

    def send_email(self,recipient_email):
        sender_email = 'hotelpandianmail@gmail.com'
        sender_password = "zibfzkbecvxdqmsl"  # Use an app-specific password if you have 2FA enabled
        subject = "This mail is to inform you that your ordering at Hotel Pandian is confirmed."
        body = (
        f''' Hii {self.name},
This is to inform you that your order has been confirmed.
The total price would be {self.totalprice}.
Your order : {self.data_to_write['order']} 
Hope you enjoy our service 
Thank you, Do visit us again
        ''')
        try:
            # Set up the MIME
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = recipient_email
            message['Subject'] = subject

            # Add body to email
            message.attach(MIMEText(body, 'plain'))

            # Use Gmail's SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the SMTP server
            text = message.as_string()  # Convert the message to a string
            server.sendmail(sender_email, recipient_email, text)  # Send the email
            server.quit()
            # Close the connection
        except Exception as e:
            print(f'Failed to send email. Error: {e}')
            self.flag = False
            messagebox.showerror(message='Please provide a correct mail id,Thank you')



if __name__ == '__main__':
    m = Menu()
    m.menu_page()