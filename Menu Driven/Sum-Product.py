#Sum_product
number=int(input("Enter a value to check Sum-product : "))
product,sum,count=1,0,0
temp=number
while(number>0):
    sub=number%10
    count+=1;
    sum=sum+sub
    product=product*sub
    number=number//10
print("The count of your number is",count)
print("Sum = ",sum)
print("Product = ",product)
if(sum*product==temp):
    print("Acceepts rule of Sum-product")
else:
    print("Dosen't accepts the rule of Sum-product")