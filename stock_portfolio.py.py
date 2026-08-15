# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker!")
print("\nAvailable stocks:")
print("AAPL, TSLA, GOOGL, MSFT, AMZN")

# Ask how many different stocks the user wants to enter
number_of_stocks = int(input("\nHow many stocks do you want to enter? "))

for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment value:", investment)

    else:
        print("Stock not available in our list.")

print("\nTotal Investment Value:", total_investment)
print("Thank you for using Stock Portfolio Tracker!")