try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
    print("a/b=%d"%c)
except Exception as e:
    print("Can't divide by zero")
else:
    print("Printing from else block")