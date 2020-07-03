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


def helloMenu():
    print("This is a hello menu module")

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
        displayMenu()

    elif choice == "2":
        Transactions.depositMoney()

    elif choice == "3":
        Transactions.withdrawMoney()

    elif choice == "4":
        Interest.interestCalculation()
        Interest.interestMoney()
        displayMenu()

    elif choice == "5":
        Loan.performLoan()

    elif choice == "6":
        Transactions.donateMoney()

    elif choice == "7":
        StockMarket.buyStock()

    elif choice == "8":
        ATM.atmSecurity()

    elif choice == "9":
        Insurance.helloInsurance()

    elif choice == "10":
        RecentTransactions.display()

    elif choice == "11":
        Shop.startShop()

    elif choice == "0":
        exit()

    else:
        print("Please enter a valid thing to do.")
        displayMenu()







