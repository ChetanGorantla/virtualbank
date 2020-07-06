import Menu
import Balance

def startShop():
    enter = str(input("Would you like to enter the shop?"))
    if enter == "yes" or enter == "y":
        print("You have entered the store. Here, you can buy merch and piggy banks!")
        type1 = str(input("What would you like to buy:\n"
                          "1. Merchandise\n"
                          "2. Piggy Banks\n"
                          "3. Checkbooks\n"))
        if type1 == "1":
            choice1 = str(input("What type of merchandise would you like to buy?\n"
                                "1. Sweaters\n"
                                "2. Hats\n"
                                "3. T-Shirts\n"))
            if choice1 == "1":
                buy = str(input("This is $20. Would you still like to buy it?"))
                if buy == "yes" or buy == "y" or buy == "Yes" or buy == "Y":
                    Balance.amountToDeduct(20)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if choice1 == "2":
                buy = str(input("This is $7. Would you still like to buy it?"))
                if buy == "yes" or buy == "y" or buy == "Yes" or buy == "Y":
                    Balance.amountToDeduct(7)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if choice1 == "3":
                buy = str(input("This is $15. Would you still like to buy it?"))
                Balance.amountToDeduct(15)
                if buy == "yes" or buy == "y" or buy == "Yes" or buy == "Y":
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()


        elif type1 == "2":
            color = str(input("What color Piggy Bank would you like to buy? We have blue, red, and green."))
            if color == "blue":

                buy = str(input("This is $10. Would you still like to buy it?"))
                if buy == "yes" or buy == "y" or buy == "Yes" or buy == "Y":
                    Balance.amountToDeduct(10)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if color == "red":

                buy = str(input("This is $10. Would you still like to buy it?"))
                if buy == "yes" or buy == "y" or buy == "Yes" or buy == "Y":
                    Balance.amountToDeduct(10)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if color == "green":

                buy = str(input("This is $10. Would you still like to buy it?"))
                if buy == "yes" or buy == "y" or buy == "Yes" or buy == "Y":
                    Balance.amountToDeduct(10)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

        elif type1 == "3":
            texture = str(input("What texture would you like your checkbook to be? We have 1. standard, 2. classic, and 3. new textures."))
            if texture == "1":
                price = 10
                buy = str(input("This is $"+ str(price) +" Would you still like to buy it?"))
                if buy == "yes" or buy == "y" or buy == "Yes" or buy == "Y":
                    Balance.amountToDeduct(price)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if texture == "2":
                price = 15
                buy = str(input("This is $" + str(price) + " Would you still like to buy it?"))

                if buy == "yes" or buy == "y" or buy == "Yes" or buy == "Y":
                    Balance.amountToDeduct(15)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

            if texture == "3":
                price = 20
                buy = str(input("This is $" + str(price) + " Would you still like to buy it?"))
                if buy == "yes" or buy == "y" or buy == "Yes" or buy == "Y":
                    Balance.amountToDeduct(10)
                    print("You have successfully bought this product. Thank you and have a nice day.")
                    Menu.displayMenu()
                else:
                    print("Ok, that's fine.")
                    startShop()

    else:
        print("Ok. Have a nice day!")
        Menu.displayMenu()
