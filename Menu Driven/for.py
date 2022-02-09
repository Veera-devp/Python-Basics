number=int(input("Enter a starting number :"))
roman=int(input("Enter a ending number : "))
Check=int(input("Enter a checking number : "))
print(range(number,roman))
for i in range(number,roman+1):
    if(i==Check):
        print(Check,"Found")
        break;
else:
    print(Check,"not found")