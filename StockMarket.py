import Balance

def options():
    option = str(input("Would you like to buy or sell stocks?"))
    if option == "buy":
        buyStock()
    elif option == "sell":
        sellStock()

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
    ticker = str(input("Please enter your ticker to sell."))
    quantity = int(input("How much stocks would you like to sell?"))
    stock_price = 150
    amount = (stock_price*quantity)
    Balance.amountToAdd(amount)
    print("You have just sold ", ticker," and the quantity = ", quantity, " total amount received is ", amount)
    print("Your account balance is: ", Balance.getBalance())


