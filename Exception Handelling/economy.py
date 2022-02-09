try:
    klu1=open("../../ExamplesForLoop/Exception Handelling/filoe.txt", "r+")
    try:
        klu1.write("Raghava is a badboy")
    finally:
        klu1.close()
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    klu1.close()