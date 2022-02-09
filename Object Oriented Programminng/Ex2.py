class Person:
    name="Brand"

    def __init__(self,aName):
        self.name=aName

def main():
    aPerson=Person("Raghava")
    print(aPerson.name)
if __name__ == '__main__':
    main()