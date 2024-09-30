Menu = {
    "expresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 100,
    },
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 100,
            "coffee" : 15,
        },
        "cost" : 150,
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost" : 200,
    }
}
resource = {
    "water" : 5000,
    "milk" : 2000,
    "coffee": 500
}
profit = 0

def check_resource(order):
    for item in order :
        if order[item]>resource[item]:
            print("Sorry insufficient {item}")
            return False
    return True
        
def process_payment(cost):
    total = 0
    print("Enter the coins:")
    coin_5 = int(input("How many Rs5 coins?"))
    coin_10 = int(input("How many Rs10 coins?"))
    coin_20 = int(input("How many Rs20 coins?"))
    total = 5*coin_5 + 10*coin_10 + 20*coin_20
    if total >= cost:
        change = total - cost 
        global profit
        profit += cost
        print(f"Change : Rs{change}.")
        return True
    else :
        more = cost - total
        print(f"More Rs.{more} required.")
        print(f"Sorry insufficient money ...money refunded.")
        return False
    
def make_coffee(coffee,ingredients):
    global resource
    for item in ingredients:
        resource[item] -= ingredients[item]
    print(f"Here is your {coffee}...have a great day !!")
    
coffee_type = {}
is_on = True
while is_on :
    choice = input("What would you like to have ?(latte/expresso/cappuccino):").lower()
    if choice == "off" :
        is_on = False
    elif choice == "report" :
        print(f"water = {resource["water"]}ml\nmilk = {resource["milk"]}ml\ncoffee = {resource["coffee"]}gm")
        print("Money : Rs.",profit)
    elif ( (choice == "latte") or (choice == "expresso") or (choice == "cappuccino")):
        coffee_type = Menu[choice]
        print(coffee_type)
        if (check_resource(coffee_type["ingredients"])) == True:
           if (process_payment(coffee_type["cost"])) == True:
               make_coffee(choice,coffee_type["ingredients"])
    else :
        print("Invalid...not available...")

