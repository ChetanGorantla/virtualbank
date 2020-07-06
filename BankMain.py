# BankMain.py
import Login
import Menu
import Balance
import Transactions



print("welcome")

if (Login.performLogin() == True):
    Menu.showMenu()
    # Balance.displayBalance(accountNumber=0)
else:
    print("Please try again.")
    print("You have one try left.")
    if (Login.performLogin() == True):
        Menu.showMenu()


