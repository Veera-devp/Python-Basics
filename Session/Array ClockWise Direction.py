def rotate(a, n):
    i=0
    j=n-1
    while i!=j:
        a[i],a[j]=a[j],a[i]
        i=i+1
    pass
a= [1, 2, 3, 4, 5]
n = len(a)
for i in range(0, n):
    print(a[i], end=' ')
rotate(a, n)
print("\nRotated array is : ")
for i in range(0, n):
    print(a[i],end=' ')