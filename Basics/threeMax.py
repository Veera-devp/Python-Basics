def maximum(x,y,z):
    if (x>=y) and (x>=z):
        max=x
    elif (y>=x) and (y>=z):
        max=y
    else:
        max=z
    return max
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(maximum(a, b, c))