marks={"Prasad":99,"Murali":98,"Mahesh":97,"Sai":96}
str=(input("Enter a Student name:"))
for dir in marks:
    if str==dir :
        print("Marks:",marks[dir])
        break
else:
    print("Not Found in list")