def suum(n):
    k=n
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+r
        n=n//10
    return sum
def fancy(n):
    p=n
    pp=n%10
    count,count1=0,0
    flag=0
    while(n!=0):
        count+=1
        n=n//10
    while(p!=0):
        r=p%10
        if(r==pp):
            count1=count1+1
        p=p//10
    if(count==count1):
        flag=1
    else:
        flag=0
    return flag
n=int(input())
q=suum(n)
luck=suum(q)
f=fancy(n)
if(luck==9):
    print("Lucky number")
else:
    print("Not a lucky number")
if(f==1):
    print("Fancy")
else:
    print("Not fancy")