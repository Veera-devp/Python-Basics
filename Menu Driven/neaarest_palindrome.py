def check_palindrome(n):
    temp = n
    rev =0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if(rev==temp):
        return True
    else:
        return False
n=int(input("Enter a value : "))
i = n
while(1):
    if(check_palindrome(i)):
        print(i)
        break
    i=i+1
