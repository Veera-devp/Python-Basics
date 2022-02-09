n=int(input("Enter a number : "));
s=0;
harshad=n;
while(n>0):
    rev=n%10;
    s=s+rev;
    n=n//10;
if (harshad%s==0):
    print(harshad,"is a harshad number");
else:
    print(harshad,"is not a harshad number");