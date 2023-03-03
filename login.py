from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys

pro = Tk()  # windows class
pro.geometry('800x450+280+100')  # width and height of windows ( width , height , left , up )
pro.resizable(False, False)  # close minimum

pro.title("SUPERMARKET")  # ( TITLE )s
# pro.iconbitmap('/home/maidservant/Desktop icon.icon')
# title = Label(pro,text='Super Market System', fg='white', bg='#0B2F3A',font=('tajawal',16,'bold'))
# title.pack(fill=X)

F1 = Frame(pro, width=230, height=450, bg='#0B2F3A')  # Make custom place
F1.place(x=570, y=0)

# ( Start TEXTS )

# txt1 = Label(F1, text='Developer Information', bg='#0B2F3A' , fg = 'white' , font=('tajawal',12,'bold'))
# txt1.place(x=15,y=10)

# txt2 = Label(F1, text='Majid Saqr', bg='#0B2F3A' , fg = 'white' , font=('tajawal',12,'bold'))
# txt2.place(x=65,y=40)
# 
# txt3 = Label(F1, text='Contact Me', bg='#0B2F3A' , fg = 'white' , font=('tajawal',12,'bold'))
# txt3.place(x=65,y=80)

# ( End TEXTS )

# ( Start Functions )

facebook = 'https://www.facebook.com/majid.sakr.18/'
github = 'https://github.com/majidsaqr12'
whatsapp = 'https://wa.me/qr/HY5MBCDMG4KIG1'


def open1():
    webbrowser.open_new(facebook)


def open2():
    webbrowser.open_new(github)


def open3():
    webbrowser.open_new(whatsapp)


def log():
    user = EnUser.get()
    password = EnPass.get()
    if user == 'admin' and password == '1234':
        messagebox.showinfo('Welcome', ' Welcome you , Correct Data')
    else:
        messagebox.showerror('Error', ' Faild user or password')
        s


# ( End Function )

# ( Start BUTTUNS )

btn1 = Button(F1, text='Facebook', width=10, fg='black', bg='#DBA901', font=('tajawal', 10, 'bold'), command=open1)
btn1.place(x=55, y=50)

btn2 = Button(F1, text='Whatsapp', width=10, fg='black', bg='#DBA901', font=('tajawal', 10, 'bold'), command=open3)
btn2.place(x=55, y=100)

btn3 = Button(F1, text='Telegram', width=10, fg='black', bg='#DBA901', font=('tajawal', 10, 'bold'))
btn3.place(x=55, y=150)

btn3 = Button(F1, text='LinkedIn', width=10, fg='black', bg='#DBA901', font=('tajawal', 10, 'bold'))
btn3.place(x=55, y=200)

btn4 = Button(F1, text='Github', width=10, fg='black', bg='#DBA901', font=('tajawal', 10, 'bold'), command=open2)
btn4.place(x=55, y=250)

btn5 = Button(F1, text='Close', width=10, fg='black', bg='#DBA901', font=('tajawal', 10, 'bold'), command=quit)
btn5.place(x=55, y=300)

# ( End BUTTON )

# ( start photo )

# img = PhotoImage(file="COURSES:\\r.jpg")
# imo = lable(pro,image = img)
# imo.place(x=120,y=43,width=308,height=272)

# ( End Photo )

# ( Start Login )

F2 = Frame(pro, width=569, height=450, bg='#0B2F3A')  # Make custom place
F2.place(x=0, y=0)

txt4 = Label(F2, text='SuperMarket System', bg='#0B2F3A', fg='white', font=('tajawal', 15, 'bold'))
txt4.place(x=100, y=50)

txt5 = Label(F2, text='Welcome ! Please Login', bg='#0B2F3A', fg='white', font=('tajawal', 15, 'bold'))
txt5.place(x=100, y=100)

l1 = Label(pro, text='UserName', fg='gold', bg='#0B2F3A', font=('tagawal', 12))
l1.place(x=100, y=200)

l2 = Label(pro, text='Password', fg='gold', bg='#0B2F3A', font=('tagawal', 12))
l2.place(x=100, y=240)

EnUser = Entry(pro, font=('tajawal', 12), justify='center')
EnUser.place(x=200, y=200)

EnPass = Entry(pro, font=('tajawal', 12), justify='center')
EnPass.place(x=200, y=240)

btn6 = Button(F2, text='Login', width=10, fg='black', bg='#DBA901', font=('tajawal', 10, 'bold'), command=log)
btn6.place(x=240, y=280)

# ( End Login )
pro.mainloop()  # open windows
