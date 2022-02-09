file = open('example.txt', 'r')
#print(file.read())
#data=file.read()
#print(data)
lines = file.readlines()
for line in lines[ : 5]:
    print(line)