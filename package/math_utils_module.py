from datetime import datetime
from time import time
import math
import random
import string 
import time

from uuid import uuid4 


def date_time():
    while True :
        print("Date-Time and Time Operation :")
        print("1. Display and Time Operaion")
        print("2. Calculate diffrence between two dates/times ")
        print("3. Formate date into custom format")
        print("4. Stop-Watch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu ")
        print()

        choice = int(input("Enter Your Choice:- "))
        print("=======================")

        if choice == 1 :
            dt = datetime.now()
            print(f"Current Date and Time : {dt}")
            print("=======================")


        elif choice == 2 :
            current = input("Enter First Date (YYYY-MM-DD) : ")
            second = input("Enter second Date (YYYY-MM-DD) : ")

            dt1 = datetime.strptime(current,"%Y-%m-%d")
            dt2 = datetime.strptime(second,"%Y-%m-%d")

            print(f"Difference : {abs(dt2-dt1)}")
            print("=======================")
        

        elif choice == 3 :
            print("Choose an option")
            print("1 Date-Time")
            print("2 Date")
            print("3 Time")
            print()

            choice = int(input("Enter Your Choice:-"))

            if choice == 1 :
                dt = datetime.now()
                print(f"Current Date and Time : {dt}")
                print()

            elif choice == 2 :
                dt1 = datetime.today()
                print(f"Current Date :{dt1.strftime("%Y-%m-%d") }")
                print()

            elif choice == 3 :
                t = datetime.now()
                print(f"Current Time :{t.strftime("%H:%M:%S")}")
                print("=======================")

            else:
                print("Enter Valid Choice !")

        elif choice == 4 :
            start = time.time()
            input("Enter To Stop Timer :")
            end = time.time()
            difference=end-start

            print(f"Differetent In Second : {difference:.2f}")
            print()



        elif choice == 5 :
            count = int(input("Enter a time in seconds:- "))
  
            for i in range(count, 0, -1):
                print(i)
                time.sleep(1)

            print("Time's up!")

        elif choice == 6 :
            break

        else :
            print(" Invalid Choice! Please enter 1 to 7 ")
 
def math_Opration():
    while True :
        print()
        print("Mathamatical Operation :")
        print("1. Calculate factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Menu ")

        choice = int(input("Enter Your Choice:-"))
        print()

        if choice == 1 :
            num = int(input("Enter a number To Calculate factorial :-"))
            print(math.factorial(num))
            print()

        elif choice == 2 :
            money = int(input("Enter a Principal Ammount : "))
            rent = int(input("Enter To Interest ( in %) : "))
            year = int(input("Enter Year : "))

            com = money * (1+ rent/100) ** year-money
            print(f"Compound Interest : {com:.2f}")
            print()

        elif choice == 3 :
            value = float(input("Enter Value :-"))
            value = math.radians(value)
            print(f"Sin {math.sin(value):.2f}")
            print(f"Cos {math.cos(value):.2f}")
            print()

        elif choice == 4 :
            print("Select an Option: ")
            print()
            print("1. Area of Circle")
            print("2. Area of Rectangle")
            print("3. Area of Square")
            print("4. Back to main menu")

            choice = int(input("Enter Choice:-"))
            print()

            if choice == 1 :
                radius = float(input("Enter radius: "))
                area = math.pi * radius ** 2
                print(f"Area of Circle = {area:.2f}")
                print()

            elif choice == 2:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = length * width
                print(f"Area of Rectangle = {area:.2f}")
                print()

            elif choice == 3:
                side = float(input("Enter side: "))
                area = side ** 2
                print(f"Area of Square = {area:.2f}" )
                print()


            elif choice == 4:
                print("Back to main menu")
                break

            else:
                print("Invalid choice")

        elif choice == 5  :
            print("Back to main menu")
            break

        else:
            print("Enter Valid Chioce !")

def random_Opration():
    while True :

        print("Random Data Generation :")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP ")
        print("5. Back to Main Menu ")

        choice = int(input("Enter Choice :- "))
        print()

        if choice == 1 :
            num = random.randint(1,100)
            print(num)
            print()


        elif choice == 2 :
            l = [30,60,90,70,80]
            random.shuffle(l)
            print(l)
            print()


        elif choice == 3 :
            lenght = int(input("Enter Password lenth :"))
            value = string.ascii_letters + string.punctuation + string.digits
            password = "".join(random.choices(value,k=lenght))
            print(f"Generated Password : {password}")
            print()


        elif choice == 4 :
            otp = random.randint(100000,999999)
            print(f"Your Generate OTP is : {otp}")
            print()

        elif choice == 5 :
            print("Thank You !")
            break

        else :
            print("Enter Valid Choice ! ")

def uniqu_id():

    print("Generate Unique Identifiers :")
    while True :
        print("1. Creat To UUID :")
        print("2. Back to Menu :")

        choice = int(input("Enter Choice :-"))

        if choice == 1 :
            id = uuid4()
            print(f"Generated UUID: {id}")
            print()

        elif choice == 2 :
            break

        else :
            print("Enter Valide Choice !")
