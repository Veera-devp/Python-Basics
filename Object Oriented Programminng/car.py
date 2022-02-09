class Watch:

    def __init__(self,brand,release):
        self.brand = brand
        self.release= release
    def display(self):
        print(self.brand, self.release)

brand = input("Enter brand")
rele = input("Enter release date")
a=Watch(brand, rele)
a.display()