# coffee machine project
# 3 hot flavours
# 1. expresso $1.50
# a. 50ml water
# b. 18g coffee
# 2. Latte $2.50
# a. 200ml water
# b. 24g coffee
# c. 150ml milk
# 3. cappuccino $3.00
# a. 250 ml water
# b. 24g coffee
# c. 100ml milk
# resources to manage at start: milk - 200ml, water-300ml and coffee - 100g
# coin operated - penny - 1 cent($0.01),dime- 10($0.10) cents,nickel - 5($0.05) cents and quarter($0.25)- 25 cents
# # program requirements
# a. print report
# b. check resources sufficient?
# c. process coins
# d. check transaction successful?
# e.make coffee[deduct resources]

from resource import MENU
from resource import resources

# reminder need to iterate over until it enters off
# initialising money as 0
money = 0


def total_money():
    return money


def monetary_value(q, d, n, p, cost):
    value = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    change = value - cost
    return change


def material(ing, resource, cost_choice,choice):
    global money
    c = amount(cost_choice)
    if c > 0:
        for i in ing:
            if i in resource:
                resource[i] -= ing[i]
        money += cost_choice
        print(f"Here is ${c:.2f} in change.")
        print(f"Here is your {choice} Enjoy!")
    else:
        print(f"Not enough money to buy {choice}, Money refunded. ")


def check_ingredients(ing, resource, cst, choice):
    count = 0
    cost_choice = cst
    coffee_choice = choice
    l = len(ing)
    for i in ing:
        if i in resource:
            if resource[i] < ing[i]:
                print(f"Sorry there is not enough {i}.")
                return False
            elif resource[i] > ing[i]:
                count += 1
    if count == l:
        material(ing, resource, cost_choice, coffee_choice)

    return True


def amount(cost):
    print("Please insert coins. ")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))
    return monetary_value(q, d, n, p, cost)


def check_resources(choice):
    menu = MENU[choice]
    ing = menu["ingredients"]
    cst = menu["cost"]
    check_ingredients(ing, resources, cst, choice)


def report_print():
    for i in resources:
        print(f"{i.title()}: ${resources[i]}")
    print(f"Money: ${total_money()}")


over = False
while not over:
    # asking user input
    user_choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()

    # checking user input with if and else
    if user_choice == "report":
        report_print()
    elif user_choice == "latte":
        check_resources(user_choice)
    elif user_choice == "cappuccino":
        check_resources(user_choice)
    elif user_choice == "espresso":
        check_resources(user_choice)
    elif user_choice == "off":
        print("Thank you coffee machine is off. ")
        over = True
    else:
        print("Error: Invalid choice. ")
