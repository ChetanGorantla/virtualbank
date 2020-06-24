def helloAccountaccess():
    print("This is a hello account access module.")

def performAccountaccess():

    print("Something important is that in a certain time point we will ask you for a access settings pin and tis is a very important pin if you enter the pin so many times incorrectly then the computer might go to sleep for a minute and we will also not know anything you saved on your bank account or we will not know your balance and etc.")

    passcode = str(input("Please enter your passcode for more security reasons."))
    phone_number = str(input("Please enter your phone number for more security reasons."))
    access_settings_pin = str(input("Please enter your settings pin so we can access to all the things you have saved and how much money you have and etc."))

    if passcode == "" or phone_number == "" or access_settings_pin == "":
        print("Sorry you did not enter the passcode, phone number or the access settings.")


    elif passcode == "987654321" and  phone_number == "123-456-789" and  access_settings_pin == "987-654-321":

        print("Thank you, you have entered the information correctly.")

        return True

    else:
        print("You have entered the incorrect information please try again.")

        return False