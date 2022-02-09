def factorial(fact):
    if fact==0:
        return 1
    else:
        return fact*factorial(fact-1)
fact=int(input("Input a number to compute the factiorial : "))
print(factorial(fact))