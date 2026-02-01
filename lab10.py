# Nazım Meriç Yılmaz, CS 104, Spring 2025, LAB Week 10

numberlist = []
expenses = []
toplam  = 0
miktar = 0
option = str(input("Do you want to load expenses from expenses.csv? (y/n):"))
if option == "y":
    f = open("expenses.csv", "r")
    for line in f:
        print(line.strip(","))
    f.close()

elif option == "n":
    while not miktar == -1:
        miktar = float(input("Enter amount: "))
        toplam += miktar
        numberlist.append(miktar)
        if not miktar == -1:
            description = str(input("Enter expense description: "))
            expenses.append((description, miktar))
        if miktar == -1:
            toplam += 1

    print(f"Expenses: {expenses}")
    print(f"Total spent: [{toplam}]")

    f = open("expenses.csv", "a",)

    for desc, value in expenses:
        f.write(f"{desc},{value}\n")
    f.close()
    print("Expenses saved to expenses.csv.")