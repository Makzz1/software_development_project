from tkinter import*

FONT=('arial', 24, 'italic')
class Menu:
    def __init__(self):
        self.b = -1
        self.Y_P = 10
        self.window = Tk()
        self.window.title("Pandian Restaurant")
        self.window.minsize(width=300, height=300)
        self.window.geometry("1200x700")
        self.window.configure(bg="white")
        #button
        self.breakfast = Button(text="Breakfast", font=FONT ,command=self.breakfast_screen)
        self.breakfast.place(x=300,y=200)
        self.lunch = Button(text='Lunch',font=FONT,command=self.lunch_screen)
        self.lunch.place(x=600,y=200)
        self.dinner = Button(text='Dinner',font= FONT, command=self.dinner_screen())
        self.dinner.place(x=900,y=200)

        self.window.mainloop()
    def breakfast_screen(self):
        self.b *= -1
        if self.b == 1:
            self.breakfast_frame = Frame(self.window,height=200,width=200)
            self.breakfast_frame.place(x=300,y=300)
            self.breakfast_data = open('breakfast.csv','r')
            for i in self.breakfast_data:
                self.b_label = Label(self.breakfast_frame, text=i, font=('arial', 12, 'italic'))
                self.b_label.place(x=0,y=self.Y_P)
                self.Y_P += 50

        else:
            self.breakfast_frame.destroy()
            self.Y_P = 10

    def lunch_screen(self):
        self.Y_P = 0
        self.lunch_frame = Frame(self.window,height=200,width=200)
        self.lunch_frame.place(x=600,y=300)
        self.lunch_data = open('lunch.csv','r')
        for i in self.lunch_data:
            self.l_label = Label(self.lunch_frame, text=i, font=('arial', 12, 'italic'))
            self.l_label.place(x=0,y=self.Y_P)
            self.Y_P += 50
    def dinner_screen(self):
        pass





if __name__ == '__main__':
    menu = Menu()




'''def button_clicked():
    biriyani_total=int(biriyani_sp.get())*5
    poori_total=int(poori_sp.get())*15
    idly_total=int(idly_sp.get())*30
    dosai_total=int(dosai_sp.get())*3
    icecream_total=int(icecream_sp.get())*1
    freshjuice_total=int(freshjuice_sp.get())*2
    total_bills=biriyani_total+poori_total+idly_total+dosai_total+icecream_total+freshjuice_total
    bills=Label(text=f"your total billL ${total_bills}",font=("Times New Roman",18,"bold"),bg="tomato")
    bills.place(x=150,y=600)

#restaurant name label
resto_name=Label(text="WELCOME TO PANDIAN RESTAURANT",font=("Times New Roman",25,"bold"),bg="tomato")
resto_name.grid(column=1,row=0)

#restaurant quote label
quote=Label(text="We serve what you deserve",font=("Times New Roman",18,"italic"),bg="tomato")
quote.grid(column=1,row=2)

#food label
food_label=Label(text="choose your food",font=("Times New Roman",12,"normal"),bg="tomato")
food_label.grid(column=0,row=3)

#biriyani (food) image + info+spinbox
biriyani=PhotoImage(file="biriyani.png")
biriyani_label=Label(image=biriyani,borderwidth=0)
biriyani_label.place(x=50,y=130)
biriyani_info=Label(text="spicy chicken biriyani\n$5",font=("Times New Roman",12,"normal"),bg="tomato")
biriyani_info.place(x=40,y=230)
biriyani_sb=Spinbox(from_=0,to=10,width=5)
biriyani_sb.place(x=80,y=270)

#poori (food) image + info+spinbox
poori=PhotoImage(file="poori.png")
poori_label=Label(image=poori,borderwidth=0)
poori_label.place(x=200,y=130)
poori_info=Label(text="poori\n$15",font=("Times New Roman",12,"normal"),bg="tomato")
poori_info.place(x=210,y=230)
poori_sb=Spinbox(from_=0,to=10,width=5)
poori_sb.place(x=225,y=270)

#idly (food) image + info+spinbox
idly=PhotoImage(file="idly.png")
idly_label=Label(image=idly,borderwidth=0)
idly_label.place(x=350,y=130)
idly_info=Label(text="idly\n$30",font=("Times New Roman",12,"normal"),bg="tomato")
idly_info.place(x=350,y=230)
idly_sb=Spinbox(from_=0,to=10,width=5)
idly_sb.place(x=380,y=270)

#drink label
drink_label=Label(text="choose your drink",font=("Times New Roman",12,"normal"),bg="tomato")
drink_label.place(x=0,y=350)

#dosai (food) image + info+spinbox
dosai=PhotoImage(file="dosai.gif")
dosai_label=Label(image=dosai,borderwidth=0)
dosai_label.place(x=50,y=380)
dosai_info=Label(text="dosai\n$3",font=("Times New Roman",12,"normal"),bg="tomato")
dosai_info.place(x=40,y=480)
dosai_sb=Spinbox(from_=0,to=10,width=5)
dosai_sb.place(x=80,y=520)

#icecream (food) image + info+spinbox
icecream=PhotoImage(file="icecream.png")
icecream_label=Label(image=icecream,borderwidth=0)
icecream_label.place(x=200,y=380)
icecream_info=Label(text="icecream\n$1",font=("Times New Roman",12,"normal"),bg="tomato")
icecream_info.place(x=225,y=480)
icecream_sb=Spinbox(from_=0,to=10,width=5)
icecream_sb.place(x=80,y=520)

#freshjuice (food) image + info+spinbox
freshjuice=PhotoImage(file="freshjuice.png")
freshjuice_label=Label(image=freshjuice,borderwidth=0)
freshjuice_label.place(x=350,y=380)
freshjuice_info=Label(text="freshjuice\n$2",font=("Times New Roman",10,"normal"),bg="tomato")
freshjuice_info.place(x=360,y=480)
freshjuice_sb=Spinbox(from_=0,to=10,width=5)
freshjuice_sb.place(x=375,y=520)

#finish button
finish=Button(text="order",command=button_clicked)
finish.place(x=210,y=560)

window.mainloop()
'''