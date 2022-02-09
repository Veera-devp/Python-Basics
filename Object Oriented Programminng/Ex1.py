times=int(input('Enter how many you want to store: '))
names_array = []
while times!=0:
    temp=input()
    names_array.append(temp)
    times-=1
print_times=int(input('Enter how many you want to print: '))
while print_times!=0:
    print(names_array[print_times], end=" ")
    print_times-=1