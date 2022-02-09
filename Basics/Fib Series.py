def fibonacci(number):
   if number<=1:
       return number
   else:
       return(fibonacci(number-1)+fibonacci(number-2))
series=int(input("Enter a number : "))
if series<=0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(series):
       print(fibonacci(i))