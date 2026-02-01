# Nazım Meriç Yılmaz, CS 104, Spring 2025, LAB Week 8

# Exercise 1
numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    if i%2==0:
        numbers.remove(i)
print(numbers)


# Exercise 2

numbers = [1, 2, 3, 4, 5, 6]
def remove_even_numbers(list1):
    for i in list1:
        if i%2==0:
            list1.remove(i)

    print(list1)

remove_even_numbers(numbers)

# Exercise 3
numbers=[]
num=0
while num!=-1:
    num=int(input("Enter a number (or type -1 to finish): "))
    if num==-1:
        break
    else:
        numbers.append(num)

odd_numbers=[]
for i in numbers:
    if i%2!=0:
        odd_numbers.append(i)
        
print(odd_numbers)

# Exercise 4
numbers=[]
num=0
odd_numbers=[]
even_numbers=[]
while num!=-1:
    num=int(input("Enter a number (or type -1 to finish): "))
    if num==-1:
        break

    elif num%2==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"Odd numbers: {odd_numbers}")
print(f"Even numbers: {even_numbers}")

# Exercise 5
numbers=[]
num=0
while num!=-1:
    num=int(input("Enter a number (or type -1 to finish): "))
    if num==-1:
        break
    else:
        numbers.append(num)

numdel=int(input("Enter a number to delete: "))
for i in numbers:
    if i==numdel:
        numbers.remove(numdel)
    
print(f"Updated list: {numbers}")