'''n = int(input('Enter number of rows : '))
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(j,end=' ')
        j=j+1
    i=i+1
    print()'''

'''-----------------------------------------'''

'''n = int(input('Enter number of rows : '))
i = 1
while (i<=n):
    j=1
    while (j<=i):
        print(j, end=" ")
        j+=1
    i+=1
    print()'''

'''-----------------------------------------'''

n = int(input('Enter number of rows : '))
i=1
j=0
while(i<=n):
    k=0
    while(k<i):
        print(j,end=" ")
        j+=1
        k+=1
    i+=1
    print()
