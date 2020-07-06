# Menu.py
import Transactions
import Balance
import Interest
import Loan
import StockMarket
import ATM
import Insurance
import RecentTransactions
import Shop
from time import sleep


def helloMenu():
    print("This is a hello menu module")

def pressAnyKey():
    input("Press any key to continue.")

def showMenu():
    anwser =str(input("would you like to see the main menu?"))
    if anwser == "yes":
        print('ok entering...')
        sleep(1)
        displayMenu()
    else:
       print("exiting...")
       sleep(1)
       exit()

def displayMenu():
    print("Menu:\n"
          "1. Balance Display\n"
          "2. Deposit Money\n"
          "3. Withdraw Money\n"
          "4. Interest\n"
          "5. Loans\n"
          "6. Donate Money\n"
          "7. Stocks\n"
          "8. ATM\n"
          "9. Insurance\n"
          "10. Recent Transactions\n"
          "11. Shop\n"
          "0. Exit")
    choice = str(input("Type your choice number. \n"))

    if choice == "1":
        print("Your balance is: ", Balance.balance)
        pressAnyKey()
        displayMenu()

    elif choice == "2":
        Transactions.depositMoney()
        pressAnyKey()
        displayMenu()

    elif choice == "3":
        Transactions.withdrawMoney()
        pressAnyKey()
        displayMenu()

    elif choice == "4":
        Interest.interestCalculation()
        Interest.interestMoney()
        pressAnyKey()
        displayMenu()

    elif choice == "5":
        Loan.performLoan()
        pressAnyKey()
        displayMenu()

    elif choice == "6":
        Transactions.donateMoney()
        pressAnyKey()
        displayMenu()

    elif choice == "7":
        StockMarket.options()
        pressAnyKey()
        displayMenu()

    elif choice == "8":
        ATM.atmSecurity()
        pressAnyKey()
        displayMenu()

    elif choice == "9":
        Insurance.insuranceType()
        pressAnyKey()
        displayMenu()

    elif choice == "10":
        RecentTransactions.display()
        pressAnyKey()
        displayMenu()

    elif choice == "11":
        Shop.startShop()
        pressAnyKey()
        displayMenu()

    elif choice == "0":
        print("Goodbye...")
        exit()

    else:
        print("Please enter a valid thing to do.")
        displayMenu()
