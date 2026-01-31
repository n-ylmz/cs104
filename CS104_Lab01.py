# Nazım Meriç Yılmaz, CS 104, Spring 2025
# This program writes CS with "#" character (task number 1)
print("#"*4+" "+"#"*4) 
print("#"+" "*4+"#") 
print("#"+" "*4+"#"*4) 
print("#"+" "*7+"#") 
print("#"*4+" "+"#"*4) 
 
print(" ") #this line is to make output more readable 


# This program writes the expected face like shape with different characters (task number 2)
print(" "+"-"*5+" ") 
print("/"+" "+"^"+" "+"-"+" "+'\\')
print("\\"+" "+"\\"+"_"+"/"+" "+"/")
print(" "+"-"*5+" ")
print("Hello Nazım")

print(" ") #this line is to make output more readable 


# This program converts Turkish Liras (TRY) to other currencies (task number 3)
TRY=int(input("Enter the amount of Turkish Lira's you want to convert to different currencies: "))
USD = TRY/36
GBP = TRY/44.5
EUR = TRY/37
print(str(TRY) +" TRY is "+str(round(USD,2 ))+" USD")
print(str(TRY) +" TRY is "+str(round(GBP,2 ))+" GBP")
print(str(TRY) +" TRY is "+str(round(EUR,2 ))+" EUR")

print(" ") #this line is to make output more readable 


# This program takes points obtained for grading items from the user one by one, computes the overall grade, and prints it (task number 4)
l=float(input("Enter the total grade for labs: "))
q=float(input("Enter the total grade for quizzes: "))
m1=float(input("Enter the total grade for first midterm exam: "))
m2=float(input("Enter the total grade for second midterm exam: "))
f=float(input("Enter the total grade for the final exam: "))
grade = l*0.1+(q+m1+m2)*0.2+f*0.3
print("The overall grade is " + str(round(grade, 2)))


