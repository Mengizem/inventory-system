from util import Util


def main():
    print("Welcome to Inventory Management System")

    while (1):
        print("1) Enter '1' to display all data")
        print("2) Enter '2' to add new data")
        print("3) Enter '7' to exit app")
        print("Enter Your Choice :- ")

        n = int(input())
        if (n == 1):
            Util.display_all_data()
        elif (n == 2):
            Util.add_new_product()
        elif (n == 7):
            break
        else:
            print("Invalid Choice...!!!")


main()
