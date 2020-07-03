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

def donateMoney():
    donateAmount = int(input("How much money would you like to donate?"))
    if donateAmount > 0 and donateAmount < 500000:
        if donateAmount <= Balance.getBalance():
            place1 = "Covid-19 Relief"
            place2 = "Pennies for the Poor"
            place3 = "Cancer Research Center"

            donatePlace = str(input("What charity would you like to donate to?\n"
                                    "1. Covid-19 Relief\n"
                                    "2. Pennies for the Poor\n"
                                    "3. Cancer Research Center\n"))
            if donatePlace == "1":
                Balance.amountToDeduct(donateAmount)
                print("You have successfully donated $ ", donateAmount," to ", place1, " charity.")
                Menu.displayMenu()

            elif donatePlace == "2":
                Balance.amountToDeduct(donateAmount)
                print("You have successfully donated $ ", donateAmount," to ", place2, " charity.")
                Menu.displayMenu()

            elif donatePlace == "3":
                Balance.amountToDeduct(donateAmount)
                print("You have successfully donated $ ", donateAmount," to ", place3, " charity.")
                Menu.displayMenu()

            else:
                print("Please enter an available charity to donate to!")
                donateMoney()
        else:
            print("You do not have enough money in your account to donate. You have $", Balance.getBalance(), " but you want to donate $", donateAmount)
            donateMoney()

    else:
        print("You cannot donate that amount of money. Please try again within the range of $0-$500,000.")
        donateMoney()




