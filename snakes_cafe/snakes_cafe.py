# When run, the program should print an intro message and the menu for the restaurant

menue = ["
   {"Appetizers": ["Wings", "Cookies", "Spring Rolls"]}, 
   {"Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]}, 
  {"Desserts": ["Ice Cream", "Cake", "Pie"]}, 
{"Drinks": ["Coffee", "Tea", "Unicorn Tears"]},
]

def printMenueIntro():
    print('**************************************')
    print('**    Welcome to the Snakes Cafe!   **')
    print('**    Please see our menu below.    **')
    print('**')
    print('** To quit at any time, type "quit" **')
    print('**************************************')
    for category in menue:
        for key, value in menue[category]:
            print(key)
            print('----------')
            for dish in value:
                print(dish)
    
    

def enterOrder():
    print('***********************************')
    print('** What would you like to order? **')
    print('***********************************')
    order=input('Enter Your Favorite Dish')
    count=0
    for category in menue:
        for key, value in menue[category]:
            for dish in value:
                if order==dish:
                    count+=1
    print('** {count} order of {order} have been added to your meal **')

def exitProgram():
    exitInput=input('Would you like to exit the program?(y/n)')
    if exitInput='y':
        exit()
    else:
        enterOrder()


printMenueIntro()
enterOrder()
exitProgram()


