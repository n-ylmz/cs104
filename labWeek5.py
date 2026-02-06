# Nazım Meriç Yılmaz, CS 104, Spring 2025, LAB Week 5

# Exercise 1
debt=100
print("Your debt: 100")
while debt>0:
    pay=int(input("Enter payment amount: "))
    debt=debt-pay
    print("Remaining debt: " + str(debt))
print("Debt is fully repaid!")

# Exercise 2
grade=0
gradeSum=0
examCount=0
while grade!=-1:
    grade=float(input("Enter the new grade (Enter -1 to exit): "))
    examCount+=1
    gradeSum=gradeSum+grade
print("Average: " + str((gradeSum+1)/(examCount-1)))

# Exercise 3
num=0
evenSum=0
oddMul=1
evenExist=0
oddExist=0
num=int(input("Enter a number: "))
while num>=0:
    if num%2==0:
        evenSum=evenSum+num
        evenExist=1
    elif num%2==1:
        oddMul=oddMul*num
        oddExist=1
    num=int(input("Enter a number: "))


if evenExist==1:
    print("Total sum of even numbers: " + str(evenSum))
else: 
    print("No even numbers were entered.")


if oddExist==1:
    print("Product of odd numbers: " + str(oddMul))
else: 
    print("No odd numbers were entered.")

# Exercise 4
n=-1
while n<0:
    n=int(input("Enter a positive integer: "))

for i in range(n+1):
    print(str(i)*i)
