import Balance

def buyStock():
    print("Check out our latest stocks!")
    ticker = str(input("Please enter your ticker"))
    quantity = int(input("How much stocks would you like to buy?"))
    stock_price = 100
    amount = (stock_price*quantity)
    Balance.amountToDeduct(amount)
    print("You have just purchased ", ticker," and the quantity = ", quantity, " total amount paid is ", amount)
    print("Your account balance is: ", Balance.getBalance())
def sellStock():
    print("Sell my stocks station.")

