import random
import Menu

def display():
    i = random.randint(50000, 500000)
    look = str(input("Would you like to look at your recent transactions?"))
    if look == "yes" or look == "y":
        print("Ok, here are your most recent transactions:\n",
              "Deposited $", i,
              "Withdrew $",i,
              "Withdrew $",i,
              "Deposited $",i)
        go_back = str(input("Would you like to go back to menu or exit?"))
        if go_back == "go back" or go_back == "back":
            Menu.displayMenu()
        else:
            exit()
    else:
        Menu.displayMenu()
