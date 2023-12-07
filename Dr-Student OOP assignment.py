import sys
class Person:
    def __init__(self,name,NID,phone,program):
        self.name=name
        self.__NID=NID
        self.phone=phone
        self.faculty = "Faculty of Commerce , Business Information Systems"
        self.program=program
        self.semester="two"
        self.year="2022-2023"
    def AccountDetails(self):
        print(f"Name :- {self.name}")
        print(f"NID :- {self.__NID}")
        print(f"Phone Number :- {self.phone}")
        print(f"Faculty :- {self.faculty}")
        print(f"Program :- {self.program}")
        print(f"Semester :- {self.semester}")
        print(f"Year :- {self.year}")
class Doctor (Person):
    def __init__(self,name,NID,phone,program,code,course,salary,hoursworked) :
        super().__init__(name,NID,phone,program)
        self.code = code
        self.course = course
        self.salary = salary
        self.HoursWorked = hoursworked
    def CheckCourse(self):
        print(f"Course :- {self.course}")
    def ChangeCourse(self,newcourse):
        self.course=newcourse
        print(f"Course Changed Successfully")
        print(f"New Course :- {self.course}")
    def AccountDetails(self):
        super().AccountDetails()
        print(f"Code :- {self.code}")
        print(f"Course :- {self.course}")
        print(f"Salary :- {self.salary}")
        print(f"HoursWorked :- {self.HoursWorked}")
    def CheckHoursWorked(self):
        print(f"Hours Worked :- {self.HoursWorked}")
    def CheckSalary(self):
        print(f"Salary :- {self.salary}")
    def AddHoursWorked(self,newhours):
        self.HoursWorked+=newhours
        print(f"Hours Worked added Successfully")
        print(f"Total Hours Worked :- {self.HoursWorked}")
        if self.HoursWorked>30:
            self.OverTime=self.HoursWorked-30
            self.OverTimeAmount=(self.OverTime*(self.salary/30))
            self.salary=self.salary+self.OverTimeAmount
            print(f"Overtime Performed :- {self.OverTime}")
        else:
            print(f"Overtime Performed :- {self.OverTime}")
    def action1(self):
        print("""Welcome to System
        For Doctor Account Details enter 1
        For Check Course enter 2
        For Change Course enter 3
        For Check Hours Worked enter 4
        For Check Salary enter 5
        For Add hours worked enter 6
        For Exit enter 7""")
        while True:
            try:
                Option=int(input("Please enter 1 or 2 or 3 or 4 or 5 or 6 or 7 :- "))
            except:
                print("Error , Please enter 1 or 2 or 3 or 4 or 5 or 6 or 7 only\n")
                continue
            else:
                if Option == 1:
                    self.AccountDetails()
                if Option == 2:
                    self.CheckCourse()
                if Option == 3:
                    newcourse=input("Please enter the new course :- ")
                    self.ChangeCourse(newcourse)
                if Option == 4:
                    self.CheckHoursWorked()
                if Option == 6:
                    newhours = int(input("Enter the new hours :- "))
                    self.AddHoursWorked(newhours)
                if Option == 5:
                    self.CheckSalary()
                if Option == 7:
                    print("You are logged out")
                    sys.exit()
class Student (Person):
    def __init__(self,name,NID,phone,program,ID,universityemail):
        super().__init__(name,NID,phone,program)
        self.iD=ID
        self.UniEmail=universityemail
    def CheckNationalID(self):
        return self.__NID
    def ChangeNationalID(self,NewNID):
        self.__NID=NewNID
    def AccountDetails(self):
        super().AccountDetails()
        print(f"ID :- {self.iD}")
        print(f"University E-mail :- {self.UniEmail}")
    def action2(self):
        print("""Welcome to Student System
        For Student Account Details enter 1
        For Check National ID enter 2
        For change National ID enter 3
        For Exiting System enter 4""")
        while True:
            try:
                option=int(input("Enter 1 or 2 or 3 or 4 :- "))
            except:
                print("Error , Please enter 1 or 2 or 3 or 4 only\n")
                continue
            else:
                if option == 2:
                    print(self.CheckNationalID())
                elif option == 3:
                    NewID = int(input("please enter the new national ID"))
                    self.ChangeNationalID(NewID)
                elif option == 1:
                    self.AccountDetails()
                elif option == 4:
                    print("You are logged out")
                    sys.exit()

print("""Hello User!
                  Welcome to faculty persons program""")
while True:
    try:
        user=int(input("In case you are a Doctor enter 1 , In case your a Student enter 2 :- "))
    except:
        print("Error : Enter 1 or 2 only!")
        continue
    else:
        if user== 1:
            print("Account Creation")
            name=input("Please enter your name :- ")
            NID=input("Please enter your National ID :- ")
            phone=int(input("Please enter your phone number :- "))
            program=input("Please enter your program :- ")
            code=int(input("Please enter your code :- "))
            course=input("Please enter course :- ")
            salary=int(input("Please enter your salary :- "))
            hoursworked=int(input("Please enter Hours Worked :- "))
            print("Account created successfully")
            Dr=Doctor(name,NID,phone,program,code,course,salary,hoursworked)
            while True:
                    optionn=input("Do you want any transactions(type: yes/no)???")
                    if optionn=="yes":
                        Dr.action1()
                    elif optionn=="no":
                        print("Thanks Dr , Visit us again")
                        sys.exit()
                    else:
                        print("Error : please type yes or no only !")

        elif user==2:
            print("Account Creation")
            name = input("Please enter your name :- ")
            NID = input("Please enter your National ID :- ")
            phone = int(input("Please enter your phone number :- "))
            program = input("Please enter your program :- ")
            ID = int(input("Please enter your ID :- "))
            universityemail = input("Please enter University Email :- ")
            Stu = Student(name, phone, program, ID, NID, universityemail)
            Stu.ChangeNationalID(NID)
            print("Account created successfully")
            while True:
                    optionn = input("Do you want any transactions(type: yes/no)???")
                    if optionn == "yes":
                        Stu.action2()
                    elif optionn == "no":
                        print("Thanks Student , Visit us again")
                        sys.exit()
                    else:
                        print("Error : please type yes or no only !")





























