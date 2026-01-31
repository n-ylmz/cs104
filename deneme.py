def func1(dict1):
    Newdict={}
    for i in dict1:
        if dict1[i]<=24:
            Newdict[i]="D"
        elif dict1[i]<=49:
            Newdict[i]="C"
        elif dict1[i]<=74:
            Newdict[i]="B"
        else:
            Newdict[i]="A"
    return Newdict

grade_list = {"Alice": 85, "Bob": 67, "Charlie" : 23, "Mike" :45}

r=func1(grade_list)
for i in r:
    print(i,r[i])
              

StoreA_sales = {"apple": 100, "banana": 200, "orange": 150, "grape": 300}
StoreB_sales = {"banana": 250, "kiwi": 100, "grape": 400}

def func2(dict2,dict3):
    Newdict2=dict2
    for i in dict3:
        if i in Newdict2:
            Newdict2[i]=Newdict2[i] + dict3[i]
        else:
            Newdict2[i]=dict3[i]
    return Newdict2

t=func2(StoreA_sales,StoreB_sales)
print(t)

m = [[3,1,2],[7,5,3],[4,6,9]]
def mat(list1):
    rlist=[]
    for minlist in list1:
        b=minlist[0]
        k=minlist[0]
        if b<minlist[1]:
            b=minlist[1]
        if b<minlist[2]:
            b=minlist[2]

        if k>minlist[1]:
            k=minlist[1]
        if k>minlist[2]:
            k=minlist[2]
        gtuple=(k,b)
        rlist.append(gtuple)
    return rlist

y=mat(m)
print(y)


