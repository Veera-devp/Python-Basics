import csv
headers =[]
rows = []
with open("C:\\Users\\VeeraRaghavaSaiVarma\\Desktop\\Sample.csv","r") as csvfile:
    csvreader = csv.reader(csvfile)
    headers=next(csvreader)
    for header in headers:
        print(" ".join(header for header in headers))
    for row in csvreader:
        rows.append(row)
    print("No.of rows in file are: %d" %csvreader.line_num)
    for row in rows:
        print(" ".join(col for col in row))

