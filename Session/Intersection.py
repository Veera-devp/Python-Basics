'''def intersection(a,b):
    c=[value for value in a if value in b]
    return c
a= [10,20,30,40]
b= [30,40,50]
print(intersection(a,b))'''

def createList(n=5):
    a=[]
    for i in range(n):
        x=int(input("Enter values in list : "))
        a.append(x)
    return a
def intersection(a,b):
    c=[value for value in a if value in b]
    return c
size1=int(input("Enter Size of List 1 : "))
a=createList(size1)
print(a)
size2=int(input("Enter Size of List 2 : "))
b=createList(size2)
print(b)
intersection(a,b)