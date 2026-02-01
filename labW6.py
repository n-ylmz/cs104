# Nazım Meriç Yılmaz, CS 104, Spring 2025, LAB Week 6
# Exercise 1
def print_label_and_stars(label, count):
    print(label + " : " + count*"*")

print_label_and_stars("A",5)

# Exercise 2
rate=1
count1=0
count2=0
count3=0
count4=0
count5=0

while rate!=-1:
    rate=int(input("Enter a rating (1-5, or -1 to stop): "))
    if rate==1:
        count1=count1+1
    elif rate==2:
        count2=count2+1
    elif rate==3:
        count3=count3+1
    elif rate==4:
        count4=count4+1
    elif rate==5:
        count5=count5+1
    
print_label_and_stars("1",count1)
print_label_and_stars("2",count2)
print_label_and_stars("3",count3)  
print_label_and_stars("4",count4)  
print_label_and_stars("5",count5)  

# Exercise 3
def to_celsius(temp, scale):
    if scale=="F":
        tempC = (temp - 32) * 5/9
    elif scale=="K":
        tempC = temp - 273.15 
    return tempC

def from_celsius_to_fahrenheit(C):
    F = C * 9/5 + 32
    return F

def from_celsius_to_kelvin(C):
    K = C + 273.15
    return K

def  convert_temperature(tValue, unit):
    if unit!="C":
        tValue=to_celsius(tValue, unit)
    print("Temperature in Celsius: " + str(tValue)+"°C")
    print("Temperature in Fahrenheit: " + str(from_celsius_to_fahrenheit(tValue))+"°F")
    print("Temperature in Kelvin: " + str(from_celsius_to_kelvin(tValue))+"°K")

temperature=int(input("Enter temperature value: "))
scale=input("Enter the scale (C, F, or K): ")
convert_temperature(temperature, scale)

# Exercise 4
def is_divisor(number, divisor):
    if number%divisor==0:
        return True
    else: 
        return False
    
def print_divisors(number):
    finalProduct=""
    for i in range(1,number+1):
        if number%i==0:
            finalProduct=finalProduct+str(i)+" "
    print(str(number)+": Divisors -> "+finalProduct)

number1=int(input("Enter a positive integer: "))
number2=int(input("Enter a positive integer: "))
print_divisors(number1)
print_divisors(number2)