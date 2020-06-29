import Menu

def helloInsurance():
    print("Hello")

def insuranceType():
    type1 = "Car Insurance"
    type2 = "House Insurance"
    type3 = "Health Insurance"
    type4 = "Property Insurance"

    typeOfInsurance = str(input("What type of insurance would you like?\n You can have car, house, health, or property insurance.\n"
                                "1. Car Insurance\n"
                                "2. House Insurance\n"
                                "3. Health Insurance\n"
                                "4. Property Insurance\n"))
    if typeOfInsurance == "1":
        print("You now have ",type1)
        coverage1 = int(input("How much coverage would you like? The max is $10,000."))
        if coverage1 <10000 and coverage1 >0:
            print("You now have ", type1, " and $", coverage1, " coverage.")
            Menu.displayMenu()

        else:
            print("Please enter a valid number.")
            insuranceType()

    if typeOfInsurance == "2":
        print("You now have ",type2)
        coverage2 = int(input("How much coverage would you like? The max is $10,000."))
        if coverage2 <10000 and coverage2 >0:
            print("You now have ", type2, " and $", coverage2, " coverage.")
            Menu.displayMenu()
        else:
            print("Please enter a valid number.")
            insuranceType()

    if typeOfInsurance == "3":
        print("You now have ",type3)
        coverage3 = int(input("How much coverage would you like? The max is $10,000."))
        if coverage3 <10000 and coverage3 >0:
            print("You now have ", type3, " and $", coverage3, " coverage.")
            Menu.displayMenu()
        else:
            print("Please enter a valid number.")
            insuranceType()

    if typeOfInsurance == "4":
        print("You now have ",type4)
        coverage4 = int(input("How much coverage would you like? The max is $10,000."))
        if coverage4 <10000 and coverage4 >0:
            print("You now have ", type4, " and $", coverage4, " coverage.")
            Menu.displayMenu()
        else:
            print("Please enter a valid number.")
            insuranceType()