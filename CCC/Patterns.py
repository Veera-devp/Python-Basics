'''lines = int(input())
for line in range(1, lines+1):
    print('* '*line)'''
number = int(input('Enter a number: '))
if number == 1:
    print('1 is neither prime nor composite')
else:
    n = number-1
    fact_count = 0
    while n != 1:
        if number%n == 0:
            fact_count += 1
            break
        n -= 1
    if fact_count == 0:
        status = 'is a prime number'
    else:
        status = 'is not a prime number'
print(number,''+status)
