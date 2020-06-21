import Balance
import Menu

def loanMoney():

    loanTimes = 0
    if loanTimes == 0:
        loanCreate = str(input("Would you like to take out a loan?"))

        if loanCreate in("y", "yes", "Yes"):
            loanAmount = int(input("How much money would you like to take out a loan for? \n You can only take out a loan for a maximum of $500,000."))
            if loanAmount >= 500001:
                print("You can only take out a loan for a maximum of $500,000.")
                Menu.displayMenu()
            elif loanAmount <= 0:
                print("You cannot take out a loan of $0.")
                Menu.displayMenu()
            elif loanAmount == str:
                print("Please enter a natural number such as 1, 100, or 1000.")
                Menu.displayMenu()
            elif loanAmount == float:
                print("Please enter a natural number such as 1, 100, or 1000.")
                Menu.displayMenu()
            else:

                Balance.balance = Balance.balance + loanAmount

                print("You have successfully taken out a loan of $", loanAmount)
                print("Please pay back the amount as soon as possible.")
                Menu.displayMenu()
        else:
            Menu.displayMenu()

def performLoan():
    borrow = str(input(" did you borrow in the past?"))
    if borrow == "yes":
        when = str(input("When did you borrow it?"))
        why = str(input("For what need did you borrow it?"))
        when_money = str(input("When were you supposed to give the money back?"))
        did = str(input("Did you give the money back?"))
        time = str(input("What time did you borrow it?"))
        problem = str(input("If you did not give the money back on the correct time what was the problem?"))
        punishments = str(input("If you did not give the money back we will take that item away that you used that money with.(example: you buy a car with money that you borrowed from us and then you do not give the money back then we will take your car away."))
        punishment = str(input("Or we will decide to give you another loan with more cost to pay."))
    else:
        print("Ok, what loan would you like to take?")
        loanMoney()


