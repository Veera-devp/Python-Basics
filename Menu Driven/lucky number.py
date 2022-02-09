# Sam Considers '4' as his lucky number he also considers any number containing '4' is also a lucky number
# Check given number is a lucky number
n=int(input("Enter a number : "))
flag=0
while(n!=0):
    r=n%10
    if(r==4):
        flag=1
        break
    n=n//10
if(flag==1):
    print(n,"is a lucky number for sam")
else:
    print("Not a lucky number for sam")
'''temp,s,flag=n,0,0
while(n>0):
    d=n%10
    if(d==4):
        flag=1
        break
    n=n//10
if(flag==1):
    print("Lucky")
else:
    print("Unlucy")'''