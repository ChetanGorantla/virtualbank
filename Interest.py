import Balance
from time import sleep

def interestCalculation():
    (int(Balance.getBalance()) * 2 * (1/20))



def interestMoney():
    print("Time to calculate your interest!")
    sleep(2)
    print("You have been a member of our bank for 2 years.")
    sleep(2)
    print("Your balance is ", int(Balance.getBalance()))
    sleep(2)
    print("The interest rate is 5%.")
    sleep(2)
    interest = (int(Balance.getBalance()) * 2 * (1/20))
    print("Therefore, your interest is ", interest)
    print("Congratulations! Because you looked at your interest, you have now gotten a free bonus in your balance! go check your balance to see!")

