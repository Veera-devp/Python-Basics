def printRepeating(a,n):
    mp=[0]*100
    for i in range(0,n):
        mp[a[i]]+=1
    for i in range(0,n):
        if (mp[a[i]]>1):
            print(a[i],end=" ")
            mp[a[i]]=0
a= [12, 10, 9, 45,2, 10, 10, 45]
n = len(a)
printRepeating(a, n)