# Strong number
n=int(input("Enter a number:"))
s,temp=0,n
while(n):
    i=1
    fact=1
    rev=n%10
    while(i<=rev):
        fact=fact*i
        i=i+1
    s=s+fact
    n=n//10
if(s==temp):
    print("Strong number")
else:
    print("Not a strong number")