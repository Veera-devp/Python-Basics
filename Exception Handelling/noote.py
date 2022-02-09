# Create a file and read the file content and diaplay in console by verifying its all possible exception handling conditions
# Example file not found, modes of operations.

try:
    klu1=open("filoe.txt", "r+")
    try:
        klu1.write("Raghava is a badboy")
    finally:
        klu1.close()
except IOError:
    print("")
else:
    print("The file opened successfully")
    klu1.close()
