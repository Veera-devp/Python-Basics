def minus(a,b):
    for i in a:
        if i not in b:
            print(i,end=' ')
a=[10,20,30,40]
b=[30,40,50,60]
minus(a,b)