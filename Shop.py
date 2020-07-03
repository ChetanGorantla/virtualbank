import Menu
import Balance

def startShop():
    enter = str(input("Would you like to enter the shop?"))
    if enter == "yes" or enter == "y":
        print("You have entered the store. Here, you can buy merch and piggy banks!")
        type1 = str(input("What would you like to buy:\n"
                          "1. Merch\n"
                          "2. Piggy Banks\n"))
        if type1 == "1":
            choice1 = str(input("What type of merch would you like to buy?\n"
                                "1. Sweaters\n"
                                "2. Hats\n"
                                "3. T-Shirts\n"))
            if choice1 == "1":
                buy11 = str(input("This is $20. Would you still like to buy it?"))
                if buy11 == "yes":
                    Balance.amountToDeduct(20)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if choice1 == "2":
                buy12 = str(input("This is $7. Would you still like to buy it?"))
                if buy12 == "yes":
                    Balance.amountToDeduct(7)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if choice1 == "3":
                buy13 = str(input("This is $15. Would you still like to buy it?"))
                Balance.amountToDeduct(15)
                if buy13 == "yes":
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()


        else:
            color = str(input("What color Piggy Bank would you like to buy? We have blue, red, and green."))
            if color == "blue":

                buy21 = str(input("This is $10. Would you still like to buy it?"))
                if buy21 == "yes":
                    Balance.amountToDeduct(10)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if color == "red":

                buy22 = str(input("This is $10. Would you still like to buy it?"))
                if buy22 == "yes":
                    Balance.amountToDeduct(10)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if color == "green":

                buy23 = str(input("This is $10. Would you still like to buy it?"))
                if buy23 == "yes":
                    Balance.amountToDeduct(10)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()
