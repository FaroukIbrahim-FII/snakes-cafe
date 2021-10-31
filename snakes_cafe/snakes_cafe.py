
list = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""

print(list)

menu = ["wings", "cookies", "spring rolls", "salmon", "steak", "meat tornado",
        "a literal garden", "ice cream", "cake", "pie", "coffee", "tea", "unicorn tears"]

def orders():
    orderList = []
    userInput= input('> ').lower()
    while userInput.lower() != "quit":
        if userInput.lower() in menu:
            orderList.append(userInput)
            afterInput = f"** {orderList.count(userInput)} order of {userInput} have been added to your meal **"
            print(afterInput)
            userInput = input("> ").lower()
        else:
            print("Please enter an item from the list")
            userInput = input("> ").lower()
if __name__ == '__main__':
    orders()