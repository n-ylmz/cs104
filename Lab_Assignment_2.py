# Nazım Meriç Yılmaz, CS 104, Spring 2025, LAB Week 3
#Exercise 1
Temp=int(input("Enter the tempreture in Celcius: "))
if Temp<0:
    print("It's freezing!")
else:
    print("It's not freezing!")


#Exercise 2
Let=input("Enter a letter: ")
if Let=="a" or Let=="e" or Let=="i" or Let=="o" or Let=="u":
    print("Vowel")
else:
    print("Consonant")


#Exercise 3
age=int(input("Enter your age: "))
if age<0:
    print("Invalid input.")
elif age<12:
    print("You are a child.")
elif age<19:
    print("You are a teenager.")
elif age<64:
    print("You are a adult.")
else:
    print("You are a senior.")


#Exercise 4
length=float(input("Enter lenght: "))
width=float(input("Enter width: "))

if length<=0 or width<=0:
    print("Invalid input. Length and width must be greater than zero")
elif length!=width:
    print("It is a rectangle.")
else:
    print("It is a square.")

 