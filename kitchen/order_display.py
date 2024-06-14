import tkinter as tk
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        order_data = f.readlines()
        order_data.pop(0)
        f.close()
        f = open('../customer_side/order.csv', 'w' , newline='')
        print(order_data)
        for i in order_data:
            f.write((i))
        f.close()

        f = open('../customer_side/email.csv','r',newline='')
        reader = csv.reader(f)
        self.data_email = list(reader)


        if self.data_email:
            self.first_line = self.data_email[0]
            self.gmail = self.first_line[0]
            self.name = self.first_line[1]

            print(self.gmail,self.name)
            self.data_email = self.data_email[1:]

        f.close()

        with open('../customer_side/email.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.data_email)
        csvfile.close()

        self.send_email(self.gmail)
        self.display_orders()

    def send_email(self, recipient_email):
            print(recipient_email)
            sender_email = 'hotelpandianmail@gmail.com'
            sender_password = "zibfzkbecvxdqmsl"  # Use an app-specific password if you have 2FA enabled
            subject = "This mail is to inform you that your ordering at Hotel Pandian is ready."
            body = (
f''' Hii {self.name},
    This is to inform you that your order has been ready.
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

    def exit(self):
        self.root.destroy()
        import admin_entry_page
        admin_entry_page.admin_entry_page()


if __name__ == "__main__":
    order = Order_display()