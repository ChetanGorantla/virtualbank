# Menu.py
import Transactions
import Balance
import Interest

def helloMenu():
    print("This is a hello menu module")

def displayMenu():
    print("Menu:\n"
          "1. Balance Display\n"
          "2. Deposit Money\n"
          "3. Withdraw Money\n"
          "4. Interest\n")
    choice = str(input("Type your choice number. \n"))

    if choice == "1":
        print("Your balance is: ", Balance.balance)
        displayMenu()

    elif choice == "2":
        Transactions.depositMoney()

    elif choice == "3":
        Transactions.withdrawMoney()

    elif choice == "4":
        Interest.interestCalculation()
        Interest.interestMoney()
        displayMenu()






