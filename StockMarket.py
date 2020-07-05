import Balance
import Menu

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
    print("The current stock price is ",stock_price)
    if quantity > 100:
        print("You are purchasing more than 100 stocks so you get a 5% discount.")
        stock_price=stock_price-stock_price*0.05
    if quantity > 350:
        print("sorry, but you cannot buy more than 350 stocks.")
    else:
        amount = (stock_price*quantity)
        Balance.amountToDeduct(amount)
        print("You have just purchased ", ticker," and the quantity = ", quantity, " total amount paid is ", amount)
        print("Your account balance is: ", Balance.getBalance())
        Menu.displayMenu()
def sellStock():
    print("Sell my stocks station.")
    ticker = str(input("Please enter your ticker to sell."))
    quantity = int(input("How much stocks would you like to sell?"))
    stock_price = 150
    amount = (stock_price*quantity)
    Balance.amountToAdd(amount)
    print("You have just sold ", ticker," and the quantity = ", quantity, " total amount received is ", amount)
    print("Your account balance is: ", Balance.getBalance())
    Menu.displayMenu()


