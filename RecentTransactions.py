import random
import Menu
import Balance

def display():
    a = random.randint(50000, 500000)
    b = random.randint(50000, Balance.getBalance())
    c = random.randint(50000, Balance.getBalance())
    d = random.randint(50000, 500000)
    look = str(input("Would you like to look at your recent transactions?"))
    if look == "yes" or look == "y":
        print("Ok, here are your most recent transactions:\n",
              "Deposited $", a,
              "\nWithdrew $",b,
              "\nWithdrew $",c,
              "\nDeposited $",d)
        go_back = str(input("Would you like to go back to menu or exit?"))
        if go_back == "go back" or go_back == "back" or go_back == "menu":
            Menu.displayMenu()
        else:
            exit()
    else:
        Menu.displayMenu()
