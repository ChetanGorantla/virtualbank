# Login.py
def helloLogin():
    print("This is a hello login module.")

def performLogin():
    print("Welcome to python bank")

    bank_id = str(input("Please enter your bank id"))
    bank_account_number = str(input("Please enter your bank account number"))


    if bank_id == 'DevajTheBoy' or bank_id == "Chetan" or bank_id == "Shashank" or bank_id == "Vivan":
        bank_account_number = "987654321"
        print("Thank you, you have successfully logged in")
        return True

    else:
        print("Sorry you have failed in typing the correct bank id or the correct bnk account number")
        print("Please try login in again")
        return False
