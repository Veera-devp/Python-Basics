class Client:
    name="Sai Varma"
    phone="6302667565"
    email="saikam.raghava@gmail.com"
    purchase=0

def main():
    firstClient=Client()
    print(firstClient.name)
    print(firstClient.phone)
    print(firstClient.email)
    firstClient.name="Raghava"
    firstClient.phone="6302667565"
    firstClient.email="rag2003@gmail.com"
    print(firstClient.name)
    print(firstClient.phone)
    print(firstClient.email)

if __name__ == '__main__':
    main()


