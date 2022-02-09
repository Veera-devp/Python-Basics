#sum = lambda a,b:a+b
#prod = lambda a,b:a*b
#print(sum(76,38))
#print(prod(63,28))

def myfun(n):
    return lambda a:a*n
double=myfun(2)
triple=myfun(3)
print(double(11))
print(triple(12))