class Person:
    name="Raghava Sai Varma"
    phone=6302667565
    mailID="2000030902@kluniversity.in"
    def sayName(self):
        print("My name is...",self.name)
        print("CatchUp my phone :)",self.phone)
        print("You can also mail to :)", self.mailID)
def main():
    aPerson=Person()
    aPerson.sayName()
    aPerson.name="Veera"
    aPerson.sayName()

if __name__ == '__main__':
  main()