import Balance
import Menu
import Login

def atmSecurity():
    print("Before you use the ATM, you need to enter your bank id and pin. ")
    bank_id = str(input("Please enter your bank id "))
    pin = str(input("Please enter your pin "))
    if bank_id == "" or pin == "":
        print("Sorry, you did not enter the id or pin")
        atmSecurity()

    i = Login.random.randint(1000, 4000)
    print(i)

    robo_id = int(input("Please enter what you see above so we know that you are not a robot"))
    if robo_id == i:
        print("\n")

    else:
        print("Incorrect robo id. \n")
        atmSecurity()

    if bank_id == 'DevajTheBoy' or bank_id == "Chetan" or bank_id == "Shashank" or bank_id == "Vivan":
        if pin == "1234":

            print("Thank you, you have successfully logged in")
            atmTransaction()
        else:
            print("Sorry you have failed in typing the correct bank id or the correct pin")
            print("Please try login in again")

            atmSecurity()

    else:
        print("Sorry you have failed in typing the correct bank id or the correct pin")
        print("Please try login in again")

        atmSecurity()

def atmTransaction():
    atmType = str(input("Would you like to deposit or withdraw money?"))
    if atmType == "withdraw":
        atmWithdrawMoney = int(input("How much money would you like to withdraw?"))
        if atmWithdrawMoney <= Balance.getBalance() and atmWithdrawMoney > 0:
            Balance.amountToDeduct(atmWithdrawMoney)
            print("You have successfully withdrew $", atmWithdrawMoney)
            Menu.displayMenu()
        else:
            print("You cannot withdraw that amount of money. Please enter a number within your balance.")
            atmTransaction()

    elif atmType == "deposit":
        atmDepositMoney = int(input("How much money would you like to deposit?"))
        if atmDepositMoney <= 500000 and atmDepositMoney > 0:
            Balance.amountToAdd(atmDepositMoney)
            print("You have successfully deposited $", atmDepositMoney)
            Menu.displayMenu()
        else:
            print("You cannot deposit that amount of money. Please enter a number within $1-$500,000.")
            atmTransaction()
    else:
        print("You can only deposit or withdraw money. Please try again.")
        atmTransaction()