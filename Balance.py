from time import sleep
import Interest
import Transactions
import Menu
def helloBalance():
    print("This is a hello balance module.")
global balance
balance = 10000
def displayBalance(accountNumber):

    print("Your account number is: ", accountNumber)
    print("Your account balance is: ", balance)
    sleep(300)
def getBalance():
    return balance

def updateBalance(interest):
    global balance
    Interest.interestCalculation()
    balance = balance + interest

def amountToAdd(amount):
    global balance
    balance = balance + amount

def amountToDeduct(amount):
    global balance
    balance = balance - amount

print('hello, welcome starting initial security...')
