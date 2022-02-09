print("------Menu------")
print("1.Bitwise AND")
print("2.Bitwise OR")
print("3.Bitwise XOR")
print("4.Left Shift")
print("5.Right Shift")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
while True:
     ch=int(input("Enter the option u want"))

     if(ch==1):
           x=a&b
           print(x)
     elif(ch==2):
           x=a|b
           print(x)
     elif(ch==3):
           x=a^b
           print(x)
     elif(ch==4):
           x=a>>b
           print(x)
     elif(ch==5):
           x=a<<b
           print(x)
     else:
           break;
           print("Invalid data")
