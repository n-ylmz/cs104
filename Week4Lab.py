#Nazım Meriç Yılmaz, CS104, Spring 2025, LAB Week 4

#Exercise 1
size=int(input("Enter the size of the square: "))
for i in range(size):
    print("*"*size)
    
#Exercise 2
n1=int(input("Enter a number: "))
for i in range(1,n1+1):
    if i%2==0:
        print(str(i)+" is even")
    else:
        print(str(i)+" is odd")

#Exercise 3
Enum=int(input("Enter the number of exams: "))
Gsum=0
for i in range(Enum):
    print("Exam " + str(i+1))
    grade=int(input("Enter the grade: "))
    Gsum=Gsum+grade
print("Average: " + str(Gsum/Enum))

#Exercise 4
x=int(input("Enter the X coordinate (0-9): "))
y=int(input("Enter the Y coordinate (0-9): "))
for i in range(y):
    print(". "*10)
print(". "*x + "X " + ". "*(9-x))
for i in range(9-y):
    print(". "*10)