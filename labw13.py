# Nazım Meriç Yılmaz, CS 104, Spring 2025, LAB Week 13

dict1={}
while True:
    city=input("Enter city name (or type 'done' to finish): ")
    if city=="done":
        break
    pop=int(input("Enter population: "))
    dict1[city]=pop

print(dict1)


def filesave(myDict,fname):
    file=open(fname, "w")
    for k,v in myDict.items():
        tempstr=k+", "+str(v)+"\n"
        file.write(tempstr)
    
    file.close()
    print("The data is saved.")

fileName=input("Enter the file name to save data (or type ‘cancel’): ")

if fileName!="cancel":
    filesave(dict1,fileName)




def print_triangle(n):
    if n>0:
        print("*"*n)
        print_triangle(n-1)

print_triangle(5)
    


thelist=["New York", "Los Angeles", "Chicago"]

def print_city_list(city_list):
    if len(city_list)>0:
        print(city_list[0])
        city_list.pop(0)
        print_city_list(city_list)

print_city_list(thelist)