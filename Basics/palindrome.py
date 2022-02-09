def isPalindrome(n):
    rev= 0
    temp= 0
    while(n!=0):
        temp= n % 10
        rev=rev*10+temp
        n=int(n/10)
    return rev
num = int(input('Enter the number: '))
rev=isPalindrome(num)
if(num==rev):
  print(num,'is a Palindrome')
else:
  print(num,'is not a Palindrome')