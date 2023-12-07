from tkinter import *
window=Tk()
window.title('Currency Converter Program')
window.geometry("800x700+500+5")
def convert():
    curr1=E1.get()
    curr2=E2.get()
    curr3=float(E3.get())
    if curr1=="A" and curr2=="B":
        finalamount=curr3*1.07
        r="Dollar"
    elif curr1=="A"and curr2=="C":
        finalamount=curr3*33.14
        r = "EGP"
    elif curr1 == "A" and curr2=="D":
        finalamount=curr3*150.94
        r = "Yen"
    elif curr1 == "A" and curr2=="E":
        finalamount=curr3*0.33
        r = "Kuwaiti Dinar"
    elif curr1 == "B" and curr2=="A":
        r = "Euro"
        finalamount = curr3*0.93
    elif curr1 == "B" and curr2=="C":
        finalamount = curr3 * 30.88
        r="EGP"
    elif curr1 == "B" and curr2=="D":
        finalamount = curr3 * 140.66
        r = "Yen"
    elif curr1 == "B" and curr2=="E":
        finalamount = curr3 * 0.31
        r = "Kuwaiti Dinar"
    elif curr1 == "C" and curr2=="A":
        finalamount = curr3 * 0.030
        r="Euro"
    elif curr1 == "C" and curr2=="B":
        finalamount = curr3 * 0.032
        r = "Dollar"
    elif curr1 == "C" and curr2=="D":
        finalamount = curr3 * 4.55
        r = "Yen"
    elif curr1 == "C" and curr2=="E":
        finalamount = curr3 * 0.0100
        r = "Kuwaiti Dinar"
    elif curr1 == "D" and curr2=="A":
        finalamount = curr3 * 0.0066
        r="Euro"
    elif curr1 == "D" and curr2=="B":
        finalamount = curr3 * 0.0071
        r = "Dollar"
    elif curr1 == "D" and curr2=="C":
        finalamount = curr3 * 0.22
        r = "EGP"
    elif curr1 == "D" and curr2=="E":
        finalamount = curr3 * 0.0022
        r = "Kuwaiti Dinar"
    elif curr1 == "E" and curr2=="A":
        finalamount = curr3 * 3.03
        r = "Euro"
    elif curr1 == "E" and curr2=="B":
        finalamount = curr3 * 3.25
        r = "Dollar"
    elif curr1 == "E" and curr2=="C":
        finalamount = curr3 * 100.44
        r = "EGP"
    elif curr1 == "E" and curr2=="D":
        finalamount = curr3 * 457.43
        r = "Yen"
    else:
        finalamount="error,enter A B C D E only !"
        r=""
    z=str(finalamount)+" "+r
    L11.config(text=z)
def clear():
    E1.delete(0,'end')
    E2.delete(0,'end')
def exit():
    window.quit()
L1=Label(window,text="Welcome to Currency Convertor",bg="pink",font=('Time 16 bold italic'))
L1.pack()
L7=Label()
L7.pack()
L2=Label(window,text="Steps: 1-Enter letters of currencies mentioned in the menu and amount / 2-Select convert button",font=('Time 12 bold'))
L2.pack()
L3=Label(window,text="Menu: Euro=A // Dollar=B // EGP=C // Yen=D // Kuwaiti Dinar=E",font=('Times 14 bold italic'))
L3.pack()
L8=Label()
L8.pack()
L4=Label(window,text="Convert from:",font=('Times 14 bold'))
L4.pack()
E1=Entry(bd=4,font=('Time 14'))
E1.pack()
L5=Label(window,text="Convert to:",font=('Times 14 bold'))
L5.pack()
E2=Entry(bd=4,font=('Time 14'))
E2.pack()
L8=Label(window,text="Enter amount:",font=('Times 14 bold'))
L8.pack()
E3=Entry(bd=4,font=('Time 14'))
E3.pack()
L9=Label()
L9.pack()
B1=Button(window,text="Convert",padx=20,pady=20,bd=5,command=convert)
B1.pack()
L10=Label()
L10.pack()
B2=Button(window,text="Clear",bd=5,padx=10,pady=10,command=clear)
B2.pack(side=LEFT)
B3=Button(window,text="Exit",bd=5,padx=10,pady=10,command=exit)
B3.pack(side=RIGHT)
L11=Label()
L11.pack()
P=PhotoImage(file="download.png")
L12=Label(window,text="image",image=P)
L12.pack()
window.mainloop()
