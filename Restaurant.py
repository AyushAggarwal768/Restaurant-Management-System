
from tkinter import *
import random
import time 
import datetime
from tkinter import messagebox

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Ayush Aggarwal Project")
root.configure(background="#1B4F72")

###############################################################################
# 	frames
###############################################################################

Tops = Frame(root, width=w, height=50, bg="#1B4F72", relief="flat")
Tops.pack(side = TOP)

f1 = Frame(root, width = 1000, height = 750, bg="#1B4F72",  relief="flat")
f1.pack(side = LEFT,padx = 30)

f2 = Frame(root, width = 300, height = 750, bg="#1B4F72", relief="flat")
f2.pack(side = LEFT,padx = 20)

f3 = Frame(root, width = 450, height = 750, bg="#1B4F72", relief="flat")
f3.pack(side = LEFT,padx = 10)

###############################################################################
#    TIME
###############################################################################
localtime=time.asctime(time.localtime(time.time()))

###############################################################################
#   lable info
###############################################################################
lbl = Label(Tops, font=( 'Courier New' ,30, 'bold' ),text="Restaurant Management System",fg="white",bg="#1B4F72",anchor='w')
lbl.grid(row=0,column=0)
lbl = Label(Tops, font=( 'Courier New' ,20, ),text=localtime,fg="white",bg="#1B4F72",anchor='w')
lbl.grid(row=1,column=0)
lbl = Label(Tops, font=( 'Courier New' ,20, ),text="Project By Ayush Aggarwal",fg="white",bg="#1B4F72",anchor='w')
lbl.grid(row=2,column=0)
###############################################################################
#calculator frame 3
###############################################################################

text_Input=StringVar()
operator =""

txtdisplay = Entry(f3,font=('Courier New' ,20,'bold'), textvariable=text_Input , bd=4 ,insertwidth=6 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""
    
btn7=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="7",bg="#85C1E9", command=lambda: btnclick(7) )
btn7.grid(row=1,column=0)

btn8=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="8",bg="#85C1E9", command=lambda: btnclick(8) )
btn8.grid(row=1,column=1)

btn9=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="9",bg="#85C1E9", command=lambda: btnclick(9) )
btn9.grid(row=1,column=2)

Addition=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="+",bg="#85C1E9", command=lambda: btnclick("+") )
Addition.grid(row=1,column=3)
###############################################################################
btn4=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="4",bg="#85C1E9", command=lambda: btnclick(4) )
btn4.grid(row=2,column=0)

btn5=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="5",bg="#85C1E9", command=lambda: btnclick(5) )
btn5.grid(row=2,column=1)

btn6=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="6",bg="#85C1E9", command=lambda: btnclick(6) )
btn6.grid(row=2,column=2)

Substraction=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="-",bg="#85C1E9", command=lambda: btnclick("-") )
Substraction.grid(row=2,column=3)
###############################################################################
btn1=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="1",bg="#85C1E9", command=lambda: btnclick(1) )
btn1.grid(row=3,column=0)

btn2=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="2",bg="#85C1E9", command=lambda: btnclick(2) )
btn2.grid(row=3,column=1)

btn3=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="3",bg="#85C1E9", command=lambda: btnclick(3) )
btn3.grid(row=3,column=2)

multiply=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="*",bg="#85C1E9", command=lambda: btnclick("*") )
multiply.grid(row=3,column=3)
###############################################################################
btn0=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="0",bg="#85C1E9", command=lambda: btnclick(0) )
btn0.grid(row=4,column=1)

btnc=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="c",bg="#85C1E9", command=clrdisplay)
btnc.grid(row=4,column=0)

Decimal=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text=".",bg="#85C1E9", command=lambda: btnclick(".") )
Decimal.grid(row=4,column=2)

Division=Button(f3,padx=15,pady=15,bd=4, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="/",bg="#85C1E9", command=lambda: btnclick("/") )
Division.grid(row=4,column=3)

btnequal=Button(f3,padx=15,pady=15,bd=4,width = 18, fg="#F7F9F9", font=('Courier New', 20 ,'bold'),text="=",bg="#85C1E9",command=eqals)
btnequal.grid(columnspan=4)
###############################################################################
#    order info frame 1
###############################################################################

def Ref():
    x=random.randint(12980, 50876)
    randomRef = x
    rand.set(randomRef)

    cof= float(Fries.get())
    col= float(Lunch.get())
    cob= float(Burger.get())
    cop= float(Pizza.get())
    cocb=float(CheeseBurger.get())
    cod= float(Drinks.get())

    costoffries = cof*40
    costoflunch = col*70
    costofburger = cob*35
    costofpizza = cop*99
    costofcheeseburger = cocb*49
    costofdrinks = cod*35


    costofmeal = (costoffries +  costoflunch + costofburger + costofpizza + costofcheeseburger + costofdrinks)
    PayTax=((costoffries +  costoflunch + costofburger + costofpizza +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflunch + costofburger + costofpizza  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflunch + costofburger + costofpizza + costofcheeseburger + costofdrinks)/99)
    Service=(Ser_Charge)
    OverAllCost=( PayTax + Totalcost + Ser_Charge)
    PaidTax=(PayTax)

    ServiceCharge.set("Rs."+ str('%.2f'%Service))
    Cost.set("Rs."+ str('%.2f'%costofmeal))
    Tax.set("Rs."+ str('%.2f'%PaidTax))
    Subtotal.set("Rs."+ str(costofmeal))
    Total.set("Rs."+ str('%.2f'%OverAllCost))
    
def qExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
        
def reset():
    rand.set("0")
    Drinks.set("0")
    Fries.set("0")
    Cost.set("0")
    Lunch.set("0")
    ServiceCharge.set("0")
    Burger.set("0")
    Tax.set("0")
    Pizza.set("0")
    Subtotal.set("0")
    CheeseBurger.set("0")
    Total.set("0")



rand = StringVar()
Drinks = StringVar()
Fries = StringVar()
Cost = StringVar()
Lunch = StringVar()
ServiceCharge = StringVar()
Burger = StringVar()
Tax = StringVar()
Pizza = StringVar()
Subtotal = StringVar()
CheeseBurger = StringVar()
Total = StringVar()

lbl0 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Order No.",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl0.grid(row=0,column=0)
txt0 = Entry(f1,font=('arial' ,12,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt0.grid(row=0,column=1)    

lbl2 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Fries Meal",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl2.grid(row=1,column=0)
txt2 = Entry(f1,font=('arial' ,12,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt2.grid(row=1,column=1) 

lbl4 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Lunch Meal",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl4.grid(row=2,column=0)
txt4 = Entry(f1,font=('arial' ,12,'bold'), textvariable=Lunch , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt4.grid(row=2,column=1)

lbl6 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Burger Meal",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl6.grid(row=3,column=0)
txt6 = Entry(f1,font=('arial' ,12,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt6.grid(row=3,column=1)   

lbl8 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Pizza",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl8.grid(row=4,column=0)
txt8 = Entry(f1,font=('arial' ,12,'bold'), textvariable=Pizza , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt8.grid(row=4,column=1)   

lbl10 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Cheese Burger",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl10.grid(row=5,column=0)
txt10 = Entry(f1,font=('arial' ,12,'bold'), textvariable=CheeseBurger , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt10.grid(row=5,column=1)   

lbl1 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Drinks",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl1.grid(row=0,column=2)
txt1 = Entry(f1,font=('arial' ,12,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt1.grid(row=0,column=3)        
 
lbl3 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Cost",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl3.grid(row=1,column=2)
txt3 = Entry(f1,font=('arial' ,12,'bold'), textvariable=Cost , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt3.grid(row=1,column=3)    

lbl5 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Service Tax",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl5.grid(row=2,column=2)
txt5 = Entry(f1,font=('arial' ,12,'bold'), textvariable=ServiceCharge , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt5.grid(row=2,column=3)    

lbl7 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Tax",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl7.grid(row=3,column=2)
txt7 = Entry(f1,font=('arial' ,12,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt7.grid(row=3,column=3)    

lbl9 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Subtotal",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl9.grid(row=4,column=2)
txt9 = Entry(f1,font=('arial' ,12,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt9.grid(row=4,column=3)    

lbl11 = Label(f1, font=( 'arial' ,12, 'bold' ),text="Total",bg="#1B4F72",fg="#FBFCFC",bd=10,anchor='w')
lbl11.grid(row=5,column=2)
txt11 = Entry(f1,font=('arial' ,12,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="#00B0FF" ,justify='right')
txt11.grid(row=5,column=3)  

###############################################################################
#   Receipt
###############################################################################

def Receipt():
            
        txtReceipt.delete("1.0", END)
        txtReceipt.insert(END, 'Order No:\t\t\t' + rand.get())
        txtReceipt.insert(END, '\t\t\t' + localtime + "\n")
        txtReceipt.insert(END, 'Items\t\t           ' + "Quantity \n\n")
        txtReceipt.insert(END, 'Fries:\t\t\t      ' + Fries.get() + "\n")
        txtReceipt.insert(END, 'Lunch Meal: \t\t\t      ' + Lunch.get() + "\n")
        txtReceipt.insert(END, 'Burger: \t\t\t      ' + Burger.get() + "\n")
        txtReceipt.insert(END, 'Pizza: \t\t\t      ' + Pizza.get() + "\n")
        txtReceipt.insert(END, 'Cheese Burger: \t\t\t      ' + CheeseBurger.get() + "\n")
        txtReceipt.insert(END, 'Drinks: \t\t\t      ' + Drinks.get() + "\n")
        txtReceipt.insert(END, 'Cost: \t\t\t' + Cost.get() + "\nTax Paid: \t\t\t" + Tax.get() + "\n")
        txtReceipt.insert(END, 'Service Charge: \t\t\t' + ServiceCharge.get() + "\nTotal Cost: \t\t\t" + Total.get() + "\n")


###############################################################################
#   Button
###############################################################################

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="#FBFCFC",font=('arial' ,12,'bold'),width=10, text="TOTAL", bg="#00B0FF",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="#FBFCFC",font=('arial' ,12,'bold'),width=10, text="RESET", bg="#00B0FF",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="#FBFCFC",font=('arial' ,12,'bold'),width=10, text="EXIT", bg="#00B0FF",command=qExit)
btnexit.grid(row=8, column=0)

btnReceipt = Button(f1,padx=16,pady=8, bd=10 ,fg="#FBFCFC",font=('arial' ,12,'bold'),width=10, text="RECEIPT", bg="#00B0FF", command=Receipt)
btnReceipt.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("300x300+0+0")
    roo.title("Price List")
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="ITEM", fg="black", bd=5)
    lbl.grid(row=0, column=0)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="PRICE", fg="black", anchor=W)
    lbl.grid(row=0, column=3)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="Fries Meal", fg="#1B4F72", anchor=W)
    lbl.grid(row=1, column=0)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="40", fg="#1B4F72", anchor=W)
    lbl.grid(row=1, column=3)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="Lunch Meal", fg="#1B4F72", anchor=W)
    lbl.grid(row=2, column=0)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="70", fg="#1B4F72", anchor=W)
    lbl.grid(row=2, column=3)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="Burger Meal", fg="#1B4F72", anchor=W)
    lbl.grid(row=3, column=0)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="35", fg="#1B4F72", anchor=W)
    lbl.grid(row=3, column=3)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="Pizza Meal", fg="#1B4F72", anchor=W)
    lbl.grid(row=4, column=0)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="99", fg="#1B4F72", anchor=W)
    lbl.grid(row=4, column=3)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="Cheese Burger", fg="#1B4F72", anchor=W)
    lbl.grid(row=5, column=0)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="49", fg="#1B4F72", anchor=W)
    lbl.grid(row=5, column=3)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="Drinks", fg="#1B4F72", anchor=W)
    lbl.grid(row=6, column=0)
    lbl = Label(roo, font=('Courier New', 15 ,'bold'), text="35", fg="#1B4F72", anchor=W)
    lbl.grid(row=6, column=3)

    roo.mainloop()
btnPrice=Button(f1,padx=16,pady=8, bd=10 ,fg="#FBFCFC",font=('arial' ,12,'bold'),width=10, text="PRICE", bg="#00B0FF",command=price)
btnPrice.grid(row=7, column=0)

###############################################################################
#    Receipt frame 2
###############################################################################

lblReceipt = Label(f2, font=('Courier New', 15 ,'bold'), text="Receipt", bd=2, anchor='w', fg="#FBFCFC" ,bg='#1B4F72')
lblReceipt.grid(row=0, column=0)
txtReceipt = Text(f2, width=40, height=22, bg="#ECF0F1", bd=4, font=('Courier New', 11 ,'bold'))
txtReceipt.grid(row=1, column=0)




root.mainloop()