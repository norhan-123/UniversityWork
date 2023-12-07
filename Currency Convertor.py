print("""Welcome User
This program converts from Egyptian Pound to dollar , euro , Japanese yen , Saudi Riyal and Kuwaiti Dinar""")
def converter(EGP,Currency):
    if Currency == "dollar":
        Amount = EGP/27.20
    elif Currency == "euro":
        Amount = EGP/28.63
    elif Currency == "Saudi Riyal":
        Amount = EGP/7.24
    elif Currency == "Kuwaiti Dinar":
        Amount = EGP/88.64
    return Amount

Entered_Amount=float(input("Please enter the amount you want to convert:"))
Entered_Currency=input(f"Please type the currency you want to convert to:"
                         "[choose one of those: dollar , euro , Saudi Riyal , Kuwaiti Dinar]:")

while Entered_Currency != "dollar" and Entered_Currency != "euro" and Entered_Currency != "Saudi Riyal" and Entered_Currency != "Kuwaiti Dinar":
    Entered_Currency=input("Wrong Currency , Please enter a valid one:")

z=converter(Entered_Amount,Entered_Currency)
print(f"Entered Amount:{Entered_Amount} , Entered Currency:{Entered_Currency} , Transferred Amount:{z:,.2f} {Entered_Currency}s")



