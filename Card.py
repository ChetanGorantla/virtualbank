import Balance

def card():

    cardType = str(input("What type of card would you like to get?\n"
                         "1. Credit Card\n"
                         "2. Debit Card\n"))
    if cardType == "1":
        creditCardAmount = int(input("How much money would you like to place in your Credit Card?"))
        if creditCardAmount < Balance.getBalance() and creditCardAmount > 0:
            print("You now have a Credit Card with $", creditCardAmount, " in it.")



    elif cardType == "2":
        debitCardAmount = int(input("How much money would you like to place in your Debit Card?"))
        if debitCardAmount < Balance.getBalance() and debitCardAmount > 0:
            print("You now have a Debit Card with $", debitCardAmount, " in it.")

def getCreditCardAmount():
    return 