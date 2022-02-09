def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    char = input()
    if char in ('1', '2', '3', '4'):
        num1 = float(input("Enter a value: "))
        num2 = float(input("Enter b value: "))
        if char== '1':
            print(add(num1, num2))
        elif char == '2':
            print(subtract(num1, num2))
        elif char == '3':
            print(multiply(num1, num2))
        elif char == '4':
            print(divide(num1, num2))
    else:
        print("Invalid Input")
        break;