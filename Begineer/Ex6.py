marks={ "A":100,"B":99,"C":98,"D":97}
r='true'
while r!='false':
    a = (input("Enter name :"))
    if a in marks:
        print("Name:", a, "\nMarks are :", marks[a])
    else:
        print("No student found")
        r='false'
        exit()