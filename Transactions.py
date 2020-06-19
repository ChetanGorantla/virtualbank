# Transactions.py

import Balance
from time import sleep
import Menu

def helloTransaction():
    print("This is a hello transaction module.")

def withdrawMoney():
    withdrawAmount = int(input("How much money would you like to withdraw? \n"))
    print("You are withdrawing: ", withdrawAmount)
    if Balance.getBalance() < withdrawAmount:
        print("Error: You cannot withdraw that amount of money. You must withdraw less than or equal to the amount of money you have. ")
        sleep(1)
        withdrawMoney()

    elif withdrawAmount <= 0:
        print("Error: You cannot withdraw that amount of money. You must withdraw between your amount and zero. ")
        sleep(1)
        withdrawMoney()

    elif withdrawAmount == str:
        print("Error: You cannot withdraw that amount. Please enter a number.")
        sleep(1)
        withdrawMoney()

    elif withdrawAmount <= Balance.getBalance() and withdrawAmount > 0:
        Balance.amountToDeduct(withdrawAmount)
        print("You have successfully withdrew $", withdrawAmount)
        print("Your new balance is ", Balance.getBalance())
        sleep(1)
        Menu.displayMenu()

def depositMoney():
    depositAmount = int(input("How much money would you like to deposit? \n"))
    print("You are depositing: ", depositAmount)
    if Balance.getBalance() <= 0:
        print("Error: You cannot deposit that amount of money. You must deposit a natural number such as 1, 2, 3, or 4, but not 0 or a decimal. You can go as high as 100 or 100,000!")
        sleep(1)
        Menu.displayMenu()

    elif Balance.getBalance() >= 500000:
        print("Error: You cannot deposit that amount of money. You must deposit between between 0 and 500,000 dollars.")
        sleep(1)
        Menu.displayMenu()

    else:
        Balance.amountToAdd(depositAmount)
        print("You have successfully deposited ", depositAmount)
        print("Your new balance is ", Balance.getBalance())
        sleep(1)
        Menu.displayMenu()



