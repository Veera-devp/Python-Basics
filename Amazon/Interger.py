intToroman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
integer = int(input("Enter a number: "))
print_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
for x in print_order:
    if integer != 0:
        q=integer//x
        if q!=0:
            for y in range(q):
                print(intToroman[x], end="")
        integer = integer%x