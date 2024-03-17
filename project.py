from connect_db import Database
import person
import product

def main():
    service = input("""
    1. Person
    2. Product
            >>>""")


    if service == "1":
        return person.person()

    elif service == "2":
        return product.product()

    else:
        print("Error")
        return main()


if __name__ == "__main__":
    main()