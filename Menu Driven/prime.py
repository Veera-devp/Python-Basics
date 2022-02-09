n=int(input("Enter a number : "))
'''k=n//2
if (n>1):
    for i in range(2,k+1):
        if (n%i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")'''
flag = 0
if(n==1):
    flag=1
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
if(flag==1):
    print("Not a prime number")
else:
    print("Prime number")