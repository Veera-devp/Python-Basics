dic = { }
while True :
      name = input("Enter employee name :-")
      sl = int(input("Enter employee salary :-"))
      dic[name] = sl
      user = input("Do you want to quit then enter yes :-")
      if user == "yes" :
            break
print(dic)