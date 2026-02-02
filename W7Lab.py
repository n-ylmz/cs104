# Nazım Meriç Yılmaz, CS 104, Spring 2025, LAB Week 6

# Exercise 1

def calculate_power(num,pow):
    print("The result is " + str((num**pow)))


num=float(input("Enter a number: "))
pow=float(input("Enter the power: "))

calculate_power(num,pow)

# Exercise 2

highest_temp=-200
def update_temperature(new_temp):
    global highest_temp
    while new_temp!=-100:
        new_temp=float(input("Enter the daily temperatures for the week (-100 to stop): "))
        if new_temp>highest_temp:
            highest_temp=new_temp
    
    print("The highest temperature recorded this week is "+str(highest_temp))

update_temperature(-highest_temp)
    

# Exercise 3
total_sales=0
def display_total_sales():
    global total_sales
    print("Total Sales: " + str(total_sales))

def sell_item(item, quantity):
    global total_sales
    while item!=-1:
        item=int(input("Enter item to order (1.bread 2.pastry 3.cake or -1 to exit):"))
        if item==-1:
            break


        quantity=int(input("Enter the number of items: "))
        
        if item==1:
            sold=quantity*5
        elif item==2:
            sold=quantity*10
        elif item==3:
            sold=quantity*15
        else: 
            continue
        total_sales=total_sales+sold
    display_total_sales()
sell_item(0,0)


# Exercise 4
size=int(input("Enter the size of the leaves: "))
height=int(input("Enter the height of the trunk: "))

def draw_leaves():
    global size
    for i in range(1,2*size,2):
        print(" "*int((((2*size-1)-i)/2)) + "*"*i+ " " * int((((2*size-1)-i)/2)))

def draw_trunk(height):
    global size
    for i in range(height):
        print(" "*(size-1) + "|" +" "*(size-1))

def draw_tree(height):
    draw_leaves()
    draw_trunk(height)

draw_tree(height)
