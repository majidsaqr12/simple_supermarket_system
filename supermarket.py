from tkinter import *
from tkinter import messagebox
import os , math , random

class supermarket:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1250x690+60+2')
        self.root.title('Supermarket System')
        self.root.resizable(False,False)
        title = Label(self.root , text = 'SuperMarket System' , fg = 'white' , bg = '#0B2F3A' , font=('tajawal',16))
        title.pack(fill = X)
        #============ V Customer =========
        self.name = StringVar()
        self.phone = StringVar()
        self.bill = StringVar()
        x = random.randint(1,100)
        self.bill.set(str(x))
        
        # =========== V section 1 ========
        self.s1 = IntVar()
        self.s2 = IntVar()
        self.s3 = IntVar()
        self.s4 = IntVar()
        self.s5 = IntVar()
        self.s6 = IntVar()
        self.s7 = IntVar()
        self.s8 = IntVar()
        self.s9 = IntVar()
        self.s10 = IntVar()
        self.s11 = IntVar()
        self.s12 = IntVar()
        self.s13 = IntVar()
        self.s14 = IntVar()
        self.s15 = IntVar()
        self.s16 = IntVar()
        self.s17 = IntVar()
        self.s18 = IntVar()
        
        # =========== V section 2 ========
        self.ss1 = IntVar()
        self.ss2 = IntVar()
        self.ss3 = IntVar()
        self.ss4 = IntVar()
        self.ss5 = IntVar()
        self.ss6 = IntVar()
        self.ss7 = IntVar()
        self.ss8 = IntVar()
        self.ss9 = IntVar()
        self.ss10 = IntVar()
        self.ss11 = IntVar()
        self.ss12 = IntVar()
        self.ss13 = IntVar()
        self.ss14 = IntVar()
        self.ss15 = IntVar()
        self.ss16 = IntVar()
        self.ss17 = IntVar()
        self.ss18 = IntVar()
        
        # =========== V section 3 ========
        self.sss1 = IntVar()
        self.sss2 = IntVar()
        self.sss3 = IntVar()
        self.sss4 = IntVar()
        self.sss5 = IntVar()
        self.sss6 = IntVar()
        self.sss7 = IntVar()
        self.sss8 = IntVar()
        self.sss9 = IntVar()
        self.sss10 = IntVar()
        self.sss11 = IntVar()
        self.sss12 = IntVar()
        self.sss13 = IntVar()
        self.sss14 = IntVar()
        self.sss15 = IntVar()
        
        # =========== V total =============
        self.section1 = StringVar()
        self.section2 = StringVar()
        self.section3 = StringVar()
        
        #============custumer Data===============#
        F1 = Frame(root, bd = 2 , width = 310 , height = 170 , bg = '#0B4C5f')
        F1.place(x=938,y=31)
        txt1 = Label (F1 , text = 'CUSTOMER INFO' , font=('tajawal',13 , 'bold') , fg = 'white' , bg = '#0B4C5f')
        txt1.place(x=100 , y=0)
        cust_name = Label(F1 , text = 'Name' , font=('tajawal',12) , fg = 'white' , bg = '#0B4C5f')
        cust_name.place(x = 5 , y = 40)
        cust_phone = Label(F1 , text = 'Phone' , font=('tajawal',12) , fg = 'white' , bg = '#0B4C5f')
        cust_phone.place(x = 5 , y = 70)
        cust_bill = Label(F1 , text = 'Bill Num' , font=('tajawal',12) , fg = 'white' , bg = '#0B4C5f')
        cust_bill.place(x = 5 , y = 100)
        
        En_name = Entry(F1 , textvariable = self.name, justify = 'center')
        En_name.place(x = 104, y = 40)
        En_phone = Entry(F1 , textvariable = self.phone, justify = 'center')
        En_phone.place(x = 104, y = 70)
        En_bill = Entry(F1 ,textvariable = self.bill, justify = 'center')
        En_bill.place(x = 104, y = 100)
        
        btn_cust = Button(F1 , text = 'search' , font=('tajawal',10) , width = 17 , height = 1, bg = 'gold' , fg = 'black')
        btn_cust.place(x =104 , y = 130)
        
        #==============BILL=================#
        F2 = Frame(root , bd = 2 , width = 309 , height = 320 , bg = 'white')
        F2.place(x= 938 , y = 205)
        scrol_y = Scrollbar (F2 , orient = VERTICAL)
        self.txtarea = Text(F2 , yscrollcommand = scrol_y.set)
        scrol_y.pack(side = LEFT , fill = Y)
        scrol_y.config(command = self.txtarea.yview)
        self.txtarea.pack(fill = BOTH , expand = 1)
        
        #===============PRICE=================#
        F3 = Frame(root, bd = 2 , width = 605, height =130 , bg = '#0B4C5f' )
        F3.place(x= 642 , y = 558)
        total = Button(F3 , text = 'TOTAL' , width =8 , height = 1 , fg = 'black' , bg = 'gold' ,font=('tajawal',10) , command = self.total)
        total.place(x = 500 , y = 5)
        bill = Button(F3 , text = 'EXPORT' , width =8 , height = 1 , fg = 'black' , bg = 'gold' ,font=('tajawal',10) , command = self.billl)
        bill.place(x = 500, y = 44)
        clear = Button(F3 , text = 'CLEAR' , width =8 , height = 1 , fg = 'black' , bg = 'gold' ,font=('tajawal',10) , command = self.clear)
        clear.place(x = 500, y = 83)
        
        txt2 = Label(F3 , text = 'Section 1' , font=('tajawal',15 , 'bold') , bg = '#0B4C5f' , fg = 'gold')
        txt2.place(x = 5, y = 10)       
        txt3= Label(F3 , text = 'Section 2' , font=('tajawal',15 ,'bold' ) , bg = '#0B4C5f' , fg = 'gold')
        txt3.place(x = 5, y = 50)        
        txt4= Label(F3 , text = 'Section 3' , font=('tajawal',15 , 'bold') , bg = '#0B4C5f' , fg = 'gold')
        txt4.place(x = 5, y = 90)
        
        En_1 = Entry(F3 , textvariable = self.section1, width = 24 ,justify = 'center')
        En_1.place(x = 280, y = 10)        
        En_2 = Entry(F3 , textvariable = self.section2, width = 24 ,justify = 'center')
        En_2.place(x = 280, y = 50)        
        En_3 = Entry(F3 , textvariable = self.section3 , width = 24 ,justify = 'center')
        En_3.place(x = 280, y = 90)
        
        #===================ITems[1]=====================
        F4 = Frame(root , width = 318 , height = 660 , bg ='#0B4C5f')
        F4.place(x = 1, y = 31)
        text4 = Label(F4 , text ='Section 1' , font=('tajawal',15 , 'bold') , bg = '#0B4C5f' , fg = 'gold')
        text4.place(x = 108 , y = 0)
        
        l1 = Label(F4 , text ='Element 1' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l1.place(x = 20 , y = 50)        
        l2 = Label(F4 , text ='Element 2' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l2.place(x = 20 , y = 80)        
        l3 = Label(F4 , text ='Element 3' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l3.place(x = 20 , y = 110)        
        l4 = Label(F4 , text ='Element 4' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l4.place(x = 20 , y = 140)        
        l5 = Label(F4 , text ='Element 5' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l5.place(x = 20 , y = 170)       
        l6 = Label(F4 , text ='Element 6' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l6.place(x = 20 , y = 200)       
        l7 = Label(F4 , text ='Element 7' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l7.place(x = 20 , y = 230)       
        l8 = Label(F4 , text ='Element 8' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l8.place(x = 20 , y = 260)       
        l9 = Label(F4 , text ='Element 9' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l9.place(x = 20 , y = 290)       
        l10 = Label(F4 , text ='Element 10' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l10.place(x = 20, y = 320)        
        l11 = Label(F4 , text ='Element 11' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l11.place(x = 20 , y = 350)        
        l12 = Label(F4 , text ='Element 12' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l12.place(x = 20 , y = 380)        
        l13 = Label(F4 , text ='Element 13' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l13.place(x = 20 , y = 410)       
        l14 = Label(F4 , text ='Element 14' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l14.place(x = 20 , y = 440)       
        l15 = Label(F4 , text ='Element 15' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l15.place(x = 20 , y = 470)       
        l16 = Label(F4 , text ='Element 16' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l16.place(x = 20 , y = 500)       
        l17 = Label(F4 , text ='Element 17' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l17.place(x = 20 , y = 530)       
        l18 = Label(F4 , text ='Element 18' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        l18.place(x = 20 , y = 560)
        #Button
        lEnt1 = Entry(F4 ,textvariable = self.s1, width = 12 , justify = 'center')
        lEnt1.place(x= 150, y =50)       
        lEnt2 = Entry(F4 ,textvariable = self.s2, width = 12 , justify = 'center')
        lEnt2.place(x= 150, y =80)       
        lEnt3 = Entry(F4 ,textvariable = self.s3, width = 12 , justify = 'center')
        lEnt3.place(x= 150, y =110)       
        lEnt4 = Entry(F4 ,textvariable = self.s4, width = 12 , justify = 'center')
        lEnt4.place(x= 150, y =140)       
        lEnt5 = Entry(F4 ,textvariable = self.s5, width = 12 , justify = 'center')
        lEnt5.place(x= 150, y =170)       
        lEnt6 = Entry(F4 ,textvariable = self.s6, width = 12 , justify = 'center')
        lEnt6.place(x= 150, y =200)       
        lEnt7 = Entry(F4 ,textvariable = self.s7, width = 12 , justify = 'center')
        lEnt7.place(x= 150, y =230)       
        lEnt8 = Entry(F4 , textvariable = self.s8,width = 12 , justify = 'center')
        lEnt8.place(x= 150, y =260)      
        lEnt9 = Entry(F4 ,textvariable = self.s9, width = 12 , justify = 'center')
        lEnt9.place(x= 150, y =290)      
        lEnt10 = Entry(F4 ,textvariable = self.s10, width = 12 , justify = 'center')
        lEnt10.place(x= 150, y =320)      
        lEnt11 = Entry(F4 ,textvariable = self.s11, width = 12 , justify = 'center')
        lEnt11.place(x= 150, y =350)      
        lEnt12 = Entry(F4 ,textvariable = self.s12, width = 12 , justify = 'center')
        lEnt12.place(x= 150, y =380)    
        lEnt13 = Entry(F4 , textvariable = self.s13,width = 12 , justify = 'center')
        lEnt13.place(x= 150, y =410)     
        lEnt14 = Entry(F4 , textvariable = self.s14,width = 12 , justify = 'center')
        lEnt14.place(x= 150, y =440)     
        lEnt15 = Entry(F4 ,textvariable = self.s15, width = 12 , justify = 'center')
        lEnt15.place(x= 150, y =470)     
        lEnt16 = Entry(F4 , textvariable = self.s16,width = 12 , justify = 'center')
        lEnt16.place(x= 150, y =500)    
        lEnt17 = Entry(F4 ,textvariable = self.s17, width = 12 , justify = 'center')
        lEnt17.place(x= 150, y =530) 
        lEnt18 = Entry(F4 ,textvariable = self.s18, width = 12 , justify = 'center')
        lEnt18.place(x= 150, y =560)
        
        
        #==========Items[2]=========================
        F5 = Frame(root , width = 320 , height = 660 , bg ='#0B4C5f')
        F5.place(x = 320, y = 31)
        text5 = Label(F5 , text ='Section 2' , font=('tajawal',15 , 'bold') , bg = '#0B4C5f' , fg = 'gold')
        text5.place(x = 110 , y = 0)
        
        h1 = Label(F5 , text ='Element 1' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h1.place(x = 20 , y = 50)        
        h2 = Label(F5 , text ='Element 2' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h2.place(x = 20 , y = 80)        
        h3 = Label(F5 , text ='Element 3' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h3.place(x = 20 , y = 110)        
        h4 = Label(F5 , text ='Element 4' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h4.place(x = 20 , y = 140)        
        h5 = Label(F5 , text ='Element 5' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h5.place(x = 20 , y = 170)       
        h6 = Label(F5 , text ='Element 6' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h6.place(x = 20 , y = 200)       
        h7 = Label(F5, text ='Element 7' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h7.place(x = 20 , y = 230)       
        h8 = Label(F5, text ='Element 8' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h8.place(x = 20 , y = 260)       
        h9 = Label(F5, text ='Element 9' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h9.place(x = 20 , y = 290)       
        h10 = Label(F5, text ='Element 10' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h10.place(x = 20, y = 320)        
        h11 = Label(F5, text ='Element 11' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h11.place(x = 20 , y = 350)        
        h12 = Label(F5, text ='Element 12' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h12.place(x = 20 , y = 380)        
        h13 = Label(F5, text ='Element 13' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h13.place(x = 20 , y = 410)       
        h14 = Label(F5, text ='Element 14' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h14.place(x = 20 , y = 440)       
        h15 = Label(F5, text ='Element 15' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h15.place(x = 20 , y = 470)       
        h16 = Label(F5, text ='Element 16' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h16.place(x = 20 , y = 500)       
        h17 = Label(F5, text ='Element 17' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h17.place(x = 20 , y = 530)       
        h18 = Label(F5, text ='Element 18' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        h18.place(x = 20 , y = 560)
        
        #Button
        hEnt1 = Entry(F5 ,textvariable = self.ss1, width = 12 , justify = 'center')
        hEnt1.place(x= 150, y =50)       
        hEnt2 = Entry(F5 ,textvariable = self.ss2, width = 12 , justify = 'center')
        hEnt2.place(x= 150, y =80)       
        hEnt3 = Entry(F5 , textvariable = self.ss3,width = 12 , justify = 'center')
        hEnt3.place(x= 150, y =110)       
        hEnt4 = Entry(F5 ,textvariable = self.ss4, width = 12 , justify = 'center')
        hEnt4.place(x= 150, y =140)       
        hEnt5 = Entry(F5 ,textvariable = self.ss5, width = 12 , justify = 'center')
        hEnt5.place(x= 150, y =170)       
        hEnt6 = Entry(F5 , textvariable = self.ss6,width = 12 , justify = 'center')
        hEnt6.place(x= 150, y =200)       
        hEnt7 = Entry(F5 , textvariable = self.ss7,width = 12 , justify = 'center')
        hEnt7.place(x= 150, y =230)       
        hEnt8 = Entry(F5 , textvariable = self.ss8,width = 12 , justify = 'center')
        hEnt8.place(x= 150, y =260)      
        hEnt9 = Entry(F5 , textvariable = self.ss9,width = 12 , justify = 'center')
        hEnt9.place(x= 150, y =290)      
        hEnt10 = Entry(F5 ,textvariable = self.ss10, width = 12 , justify = 'center')
        hEnt10.place(x= 150, y =320)      
        hEnt11 = Entry(F5 ,textvariable = self.ss11, width = 12 , justify = 'center')
        hEnt11.place(x= 150, y =350)      
        hEnt12 = Entry(F5 ,textvariable = self.ss12, width = 12 , justify = 'center')
        hEnt12.place(x= 150, y =380)    
        hEnt13 = Entry(F5, textvariable = self.ss13,width = 12 , justify = 'center')
        hEnt13.place(x= 150, y =410)     
        hEnt14 = Entry(F5 , textvariable = self.ss14,width = 12 , justify = 'center')
        hEnt14.place(x= 150, y =440)     
        hEnt15 = Entry(F5 ,textvariable = self.ss15, width = 12 , justify = 'center')
        hEnt15.place(x= 150, y =470)     
        hEnt16 = Entry(F5 ,textvariable = self.ss16, width = 12 , justify = 'center')
        hEnt16.place(x= 150, y =500)    
        hEnt17 = Entry(F5 , textvariable = self.ss17,width = 12 , justify = 'center')
        hEnt17.place(x= 150, y =530) 
        hEnt18 = Entry(F5 , textvariable = self.ss18,width = 12 , justify = 'center')
        hEnt18.place(x= 150, y =560)
        
        #=============ITEMS[3]============================
        F6 = Frame(root , width = 295 , height = 525, bg ='#0B4C5f')
        F6.place(x = 642, y = 31)
        text6 = Label(F6 , text ='Section 3', font=('tajawal',15 , 'bold') , bg = '#0B4C5f' , fg = 'gold')
        text6.place(x = 110 , y = 0)
        
        e1 = Label(F6 , text ='Element 1' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e1.place(x = 20 , y = 50)        
        e2 = Label(F6 , text ='Element 2' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e2.place(x = 20 , y = 80)        
        e3 = Label(F6 , text ='Element 3' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e3.place(x = 20 , y = 110)        
        e4 = Label(F6 , text ='Element 4' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e4.place(x = 20 , y = 140)        
        e5 = Label(F6 , text ='Element 5' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e5.place(x = 20 , y = 170)       
        e6 = Label(F6 , text ='Element 6' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e6.place(x = 20 , y = 200)       
        e7 = Label(F6, text ='Element 7' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e7.place(x = 20 , y = 230)       
        e8 = Label(F6, text ='Element 8' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e8.place(x = 20 , y = 260)       
        e9 = Label(F6, text ='Element 9' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e9.place(x = 20 , y = 290)       
        e10 = Label(F6, text ='Element 10' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e10.place(x = 20, y = 320)        
        e11 = Label(F6, text ='Element 11' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e11.place(x = 20 , y = 350)        
        e12 = Label(F6, text ='Element 12' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e12.place(x = 20 , y = 380)        
        e13 = Label(F6, text ='Element 13' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e13.place(x = 20 , y = 410)       
        e14 = Label(F6, text ='Element 14' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e14.place(x = 20 , y = 440)       
        e15 = Label(F6, text ='Element 15' , font=('tajawal',12) , bg = '#0B4C5f' , fg = 'white')
        e15.place(x = 20 , y = 470)       

        #Button
        eEnt1 = Entry(F6 , textvariable = self.sss1, width = 12 , justify = 'center')
        eEnt1.place(x= 150, y =50)       
        eEnt2 = Entry(F6 ,textvariable = self.sss2, width = 12 , justify = 'center')
        eEnt2.place(x= 150, y =80)       
        eEnt3 = Entry(F6 ,textvariable = self.sss3, width = 12 , justify = 'center')
        eEnt3.place(x= 150, y =110)       
        eEnt4 = Entry(F6 ,textvariable = self.sss4, width = 12 , justify = 'center')
        eEnt4.place(x= 150, y =140)       
        eEnt5 = Entry(F6 ,textvariable = self.sss5, width = 12 , justify = 'center')
        eEnt5.place(x= 150, y =170)       
        eEnt6 = Entry(F6 ,textvariable = self.sss6, width = 12 , justify = 'center')
        eEnt6.place(x= 150, y =200)       
        eEnt7 = Entry(F6 ,textvariable = self.sss7, width = 12 , justify = 'center')
        eEnt7.place(x= 150, y =230)       
        eEnt8 = Entry(F6 , textvariable = self.sss8,width = 12 , justify = 'center')
        eEnt8.place(x= 150, y =260)      
        eEnt9 = Entry(F6 , textvariable = self.sss9,width = 12 , justify = 'center')
        eEnt9.place(x= 150, y =290)      
        eEnt10 = Entry(F6 , textvariable = self.sss10,width = 12 , justify = 'center')
        eEnt10.place(x= 150, y =320)      
        eEnt11 = Entry(F6 , textvariable = self.sss11,width = 12 , justify = 'center')
        eEnt11.place(x= 150, y =350)      
        eEnt12 = Entry(F6 ,textvariable = self.sss12, width = 12 , justify = 'center')
        eEnt12.place(x= 150, y =380)    
        eEnt13 = Entry(F6,textvariable = self.sss13, width = 12 , justify = 'center')
        eEnt13.place(x= 150, y =410)     
        eEnt14 = Entry(F6 ,textvariable = self.sss14, width = 12 , justify = 'center')
        eEnt14.place(x= 150, y =440)     
        eEnt15 = Entry(F6 ,textvariable = self.sss15, width = 12 , justify = 'center')
        eEnt15.place(x= 150, y =470)     
        
        self.welcome()
        
    def total(self):
        self.ts1 = self.s1.get()*1.5
        self.ts2 = self.s2.get()*2
        self.ts3 = self.s3.get()*1.5
        self.ts4 = self.s4.get()*2
        self.ts5 = self.s5.get()*1.5
        self.ts6 = self.s6.get()*2
        self.ts7 = self.s7.get()*1.5
        self.ts8 = self.s8.get()*2
        self.ts9 = self.s9.get()*1.5
        self.ts10 = self.s10.get()*2
        self.ts11 = self.s11.get()*1.5
        self.ts12 = self.s12.get()*2
        self.ts13 = self.s13.get()*1.5
        self.ts14 = self.s14.get()*2
        self.ts15 = self.s15.get()*1.5
        self.ts16 = self.s16.get()*2
        self.ts17 = self.s17.get()*1.5
        self.ts18 = self.s18.get()*2
        
        self.tsec1 = float(
            self.ts1+
            self.ts2+
            self.ts3+
            self.ts4+
            self.ts5+
            self.ts6+
            self.ts7+
            self.ts8+
            self.ts9+
            self.ts10+
            self.ts11+
            self.ts12+
            self.ts13+
            self.ts14+
            self.ts15+
            self.ts16+
            self.ts17+
            self.ts18
            )
        self.section1.set(str(self.tsec1) + " $ ")
            
        self.tss1 = self.ss1.get()*1.5
        self.tss2 = self.ss2.get()*2
        self.tss3 = self.ss3.get()*1.5
        self.tss4 = self.ss4.get()*2
        self.tss5 = self.ss5.get()*1.5
        self.tss6 = self.ss6.get()*2
        self.tss7 = self.ss7.get()*1.5
        self.tss8 = self.ss8.get()*2
        self.tss9 = self.ss9.get()*1.5
        self.tss10 = self.ss10.get()*2
        self.tss11 = self.ss11.get()*1.5
        self.tss12 = self.ss12.get()*2
        self.tss13 = self.ss13.get()*1.5
        self.tss14 = self.ss14.get()*2
        self.tss15 = self.ss15.get()*1.5
        self.tss16 = self.ss16.get()*2
        self.tss17 = self.ss17.get()*1.5
        self.tss18 = self.ss18.get()*2
        
        self.tsec2 = float(
            self.tss1+
            self.tss2+
            self.tss3+
            self.tss4+
            self.tss5+
            self.tss6+
            self.tss7+
            self.tss8+
            self.tss9+
            self.tss10+
            self.tss11+
            self.tss12+
            self.tss13+
            self.tss14+
            self.tss15+
            self.tss16+
            self.tss17+
            self.tss18
            )
        self.section2.set(str(self.tsec2) + " $ ")
            
        self.tsss1 = self.sss1.get()*1.5
        self.tsss2 = self.sss2.get()*2
        self.tsss3 = self.sss3.get()*1.5
        self.tsss4 = self.sss4.get()*2
        self.tsss5 = self.sss5.get()*1.5
        self.tsss6 = self.sss6.get()*2
        self.tsss7 = self.sss7.get()*1.5
        self.tsss8 = self.sss8.get()*2
        self.tsss9 = self.sss9.get()*1.5
        self.tsss10 = self.sss10.get()*2
        self.tsss11 = self.sss11.get()*1.5
        self.tsss12 = self.sss12.get()*2
        self.tsss13 = self.sss13.get()*1.5
        self.tsss14 = self.sss14.get()*2
        self.tsss15 = self.sss15.get()*1.5
        self.tsec3 = float(
            self.tsss1+
            self.tsss2+
            self.tsss3+
            self.tsss4+
            self.tsss5+
            self.tsss6+
            self.tsss7+
            self.tsss8+
            self.tsss9+
            self.tsss10+
            self.tsss11+
            self.tsss12+
            self.tsss13+
            self.tsss14+
            self.tsss15
                )
        self.section3.set(str(self.tsec3) + " $ ")
        self.all = float(self.tsec1 + self.tsec2 + self.tsec3)
            
    def welcome(self):
        #self.txtarea.delete('1.0', END)
        self.txtarea.insert(END , "   Welcome in your SuperMarket")
        self.txtarea.insert(END,"\n===============================")
        self.txtarea.insert(END, f"\n\t B.NUM    : {self.bill.get()}")
        self.txtarea.insert(END,f"\n\t Name     : {self.name.get()}")
        self.txtarea.insert(END,f"\n\t PHONE    : {self.name.get()}")
        self.txtarea.insert(END,"\n===============================")
        self.txtarea.insert(END,f"\nPrice\t    Conter\t       Purchases")
        self.txtarea.insert(END, "\n==============================")

    def clear(self):
        self.s1.set(0)
        self.s2.set(0)
        self.s3.set(0)
        self.s4.set(0)
        self.s5.set(0)
        self.s6.set(0)
        self.s7.set(0)
        self.s8.set(0)
        self.s9.set(0)
        self.s10.set(0)
        self.s11.set(0)
        self.s12.set(0)
        self.s13.set(0)
        self.s14.set(0)
        self.s15.set(0)
        self.s16.set(0)
        self.s17.set(0)
        self.s18.set(0)
        
        self.ss1.set(0)
        self.ss2.set(0)
        self.ss3.set(0)
        self.ss4.set(0)
        self.ss5.set(0)
        self.ss6.set(0)
        self.ss7.set(0)
        self.ss8.set(0)
        self.ss9.set(0)
        self.ss10.set(0)
        self.ss11.set(0)
        self.ss12.set(0)
        self.ss13.set(0)
        self.ss14.set(0)
        self.ss15.set(0)
        self.ss16.set(0)
        self.ss17.set(0)
        self.ss18.set(0)
        
        self.sss1.set(0)
        self.sss2.set(0)
        self.sss3.set(0)
        self.sss4.set(0)
        self.sss5.set(0)
        self.sss6.set(0)
        self.sss7.set(0)
        self.sss8.set(0)
        self.sss9.set(0)
        self.sss10.set(0)
        self.sss11.set(0)
        self.sss12.set(0)
        self.sss13.set(0)
        self.sss14.set(0)
        self.sss15.set(0)
        
        self.section1.set('')
        self.section2.set('')
        self.section3.set('')
        
        self.name.set('')
        self.phone.set('')
        self.bill.set('')
        
    def close(self):
        self.root.destroy()
        
    def save(self):
        op = messagebox.askyesno(" Save " , " Do you want save the bill ? ")
        if op > 0:
            self.bb = self.txtarea.get("1.0" , END)
            f1 = open('majidsaqr' + str(self.bill.get())+".txt" , "w" , encoding = "utf-8")
            f1.write(self.bb)
            f1.close()
        else:
            return
        
    def billl(self):
        
#         self.welcome()
        if self.s1.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts1}\t\t{self.s1.get()}\t\tElement1 ")
            
        if self.s2.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts2}\t\t{self.s2.get()}\t\tElement2 ")
            
        if self.s3.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts3}\t\t{self.s3.get()}\t\tElement3 ")
            
        if self.s4.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts4}\t\t{self.s4.get()}\t\tElement4 ")
            
        if self.s5.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts5}\t\t{self.s5.get()}\t\tElement5 ")
            
        if self.s6.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts6}\t\t{self.s6.get()}\t\tElement6 ")
            
        if self.s7.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts7}\t\t{self.s7.get()}\t\tElement7 ")
            
        if self.s8.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts8}\t\t{self.s8.get()}\t\tElement8 ")
            
        if self.s9.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts9}\t\t{self.s9.get()}\t\tElement9 ")
            
        if self.s10.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts10}\t\t{self.s10.get()}\t\tElement10 ")
            
        if self.s11.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts11}\t\t{self.s11.get()}\t\tElement11 ")
            
        if self.s12.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts12}\t\t{self.s12.get()}\t\tElement12 ")
            
        if self.s13.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts13}\t\t{self.s13.get()}\t\tElement13 ")
            
        if self.s14.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts14}\t\t{self.s14.get()}\t\tElement14 ")
            
        if self.s15.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts15}\t\t{self.s15.get()}\t\tElement15 ")
            
        if self.s16.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts16}\t\t{self.s16.get()}\t\tElement16 ")
            
        if self.s17.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts17}\t\t{self.s17.get()}\t\tElement17 ")
            
        if self.s18.get() != 0:
            self.txtarea.insert(END , f"\n {self.ts18}\t\t{self.s18.get()}\t\tElement18 ")
            
        if self.ss1.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss1}\t\t{self.ss1.get()}\t\tElement1 ")
        
        if self.ss2.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss2}\t\t{self.ss2.get()}\t\tElement2 ")
            
        if self.ss3.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss3}\t\t{self.ss3.get()}\t\tElement3 ")
            
        if self.ss4.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss4}\t\t{self.ss4.get()}\t\tElement4 ")
            
        if self.ss5.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss5}\t\t{self.ss5.get()}\t\tElement5 ")
            
        if self.ss5.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss5}\t\t{self.ss5.get()}\t\tElement5 ")
            
        if self.ss6.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss6}\t\t{self.ss6.get()}\t\tElement6 ")
            
        if self.ss7.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss7}\t\t{self.ss7.get()}\t\tElement7 ")
            
        if self.ss8.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss8}\t\t{self.ss8.get()}\t\tElement8 ")
            
        if self.ss9.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss9}\t\t{self.ss9.get()}\t\tElement9 ")
            
        if self.ss10.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss10}\t\t{self.ss10.get()}\t\tElement10 ")
            
        if self.ss11.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss11}\t\t{self.ss11.get()}\t\tElement11 ")
            
        if self.ss12.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss12}\t\t{self.ss12.get()}\t\tElement12 ")
            
        if self.ss13.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss13}\t\t{self.ss13.get()}\t\tElement13 ")
            
        if self.ss14.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss14}\t\t{self.ss14.get()}\t\tElement14 ")
            
        if self.ss15.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss15}\t\t{self.ss15.get()}\t\tElement15 ")
            
        if self.ss16.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss16}\t\t{self.ss16.get()}\t\tElement16 ")
            
        if self.ss17.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss17}\t\t{self.ss17.get()}\t\tElement17 ")
            
        if self.ss18.get() != 0:
            self.txtarea.insert(END , f"\n {self.tss18}\t\t{self.ss18.get()}\t\tElement18 ")
            
        if self.sss1.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss1}\t\t{self.sss1.get()}\t\tElement1 ")
        
        if self.sss2.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss2}\t\t{self.sss2.get()}\t\tElement2 ")
            
        if self.sss3.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss3}\t\t{self.sss3.get()}\t\tElement3 ")
            
        if self.sss4.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss4}\t\t{self.sss4.get()}\t\tElement4 ")
            
        if self.sss5.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss5}\t\t{self.sss5.get()}\t\tElement5 ")
            
        if self.sss6.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss6}\t\t{self.sss6.get()}\t\tElement6 ")
            
        if self.sss7.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss7}\t\t{self.sss7.get()}\t\tElement7 ")
            
        if self.sss8.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss8}\t\t{self.sss8.get()}\t\tElement8 ")
            
        if self.sss9.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss9}\t\t{self.sss9.get()}\t\tElement9 ")
            
        if self.sss10.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss10}\t\t{self.sss10.get()}\t\tElement10 ")
            
        if self.sss11.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss11}\t\t{self.sss11.get()}\t\tElement11 ")
            
        if self.sss12.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss12}\t\t{self.sss12.get()}\t\tElement12 ")
            
        if self.sss13.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss13}\t\t{self.sss13.get()}\t\tElement13 ")
            
        if self.sss14.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss14}\t\t{self.sss14.get()}\t\tElement14 ")
            
        if self.sss15.get() != 0:
            self.txtarea.insert(END , f"\n {self.tsss15}\t\t{self.sss9.get()}\t\tElement15 ")
            

            
        self.txtarea.insert(END , "\n.......................................")
        self.txtarea.insert(END , f"\nTotal Price $\t             {self.all}")
        self.txtarea.insert(END , "\n.......................................")
        self.save()      
        
        
root = Tk()
window = supermarket(root)
root.mainloop()