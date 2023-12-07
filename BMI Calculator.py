print("""                                           Welcome User to BMI Calculator""")
weight=float(input("please enter your weight in kilograms:"))
height=float(input("please enter your height in meters which is equal[your height in centimeters/100]:"))
BMI=weight/(height*height)
print("Your Body mass Index(BMI)=",round(BMI,2))
if BMI<16:
    print("Interpretation: seriously underweight")
elif BMI>=16 and BMI<18:
    print("Interpretation: underweight")
elif BMI>=18 and BMI<24:
    print("Interpretation: normal weight")
elif BMI>=24 and BMI<29:
    print("Interpretation: overweight")
elif BMI>=29 and BMI<=35:
    print("Interpretation: seriously overweight")
elif BMI>35:
    print("Interpretation: gravely overweight")












