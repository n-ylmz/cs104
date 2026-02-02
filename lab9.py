# Nazım Meriç Yılmaz, CS 104, Spring 2025, LAB Week 10

# Exercise 1
def get_common_elements(liste1,liste2):
    finalset=set(liste1)&set(liste2)
    return finalset
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = get_common_elements(list1,list2)

print(common)

# Exercise 2

def char_frequency(text):
    fdict = {}
    for i in text:
        if i in fdict:
            fdict[i] += 1
        else:
            fdict[i] = 1
    return fdict

text = input("Enter a string: ")

r = char_frequency(text)
print(r)

# Exercise 3
dicti={}
k=0
while True:
    
    k=input("Enter item name (or 'done' to finish): ")
    
    if k!="done":
        q=int(input("Enter the quantity: "))
        dicti[k]=q
    else:
        break

print(dicti)


# Exercise 4
while True:
    item=input("Enter an item to check (or type 'exit' to quit): ")
    if item!="exit":
        if item in dicti:
            if dicti[item]==0:
                print("This item is out of stock.")
            else:
                print("The number of items left: "+ str(dicti[item]))
        else:
            print("This item is not found in the inventory.")
    else:
        break

            