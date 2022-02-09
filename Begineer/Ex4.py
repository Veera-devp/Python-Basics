#Write a program to find the sum of n natural numbers
n=int(input("Enter a number: "))
sum=0
for i in range(n+1):
    sum=sum+i
print("Sum is:",sum)