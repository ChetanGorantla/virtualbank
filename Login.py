def helloLogin():
    print("This is a hello login module.")

def performLogin():
    print("Welcome to python bank")

    bank_id = str(input("Please enter your bank id"))
    pin = str(input("Please enter your pin"))
    if bank_id == "" or pin == "":
        print("Sorry, you did not enter the id or pin")
        performLogin()
    robo_id_value = "97531qetuo"

    print(robo_id_value)
    robo_id = str(input("Please enter what you see above so we know that you are not a robot"))
    if robo_id == robo_id_value:
        print("\n")

    else:
        print("Incorrect robo id \n")
        performLogin()

    if bank_id == 'DevajTheBoy' or bank_id == "Chetan" or bank_id == "Shashank" or bank_id == "Vivan":
        if pin == "1234":

            print("Thank you, you have successfully logged in")
            return True
        else:
            print("Sorry you have failed in typing the correct bank id or the correct pin")
            print("Please try login in again")

            return False

    else:
        print("Sorry you have failed in typing the correct bank id or the correct pin")
        print("Please try login in again")

        return False
