smallPizza = 100
MediumPizza = 200
LargePizza = 300
smallPizzaPeperoni = 30
largePizzaPeperoni = 50
extraCheesForAnySizePizza = 20
bill = 0

# Loop from 0 to 4
for i in range(1):
    pizza = input("What size of pizza do you want?\n Type s For small pizza, m For Medium pizza, l For large pizza \n Type your answer:")
    if pizza == "s" or pizza == "S":
        bill = smallPizza
        print(f"\nYour bill is {bill}")
    elif pizza == "m" or pizza == "M":
        bill = MediumPizza
        print(f"\nYour bill is {bill}\n")
    elif pizza == "l" or pizza == "L":
        bill = LargePizza
        print(f"\nYour bill is {bill}\n")
    else:
        print("You have not made a Valid Selection")
        break
    pepeAnswer = input(
        "Do you want Peperoni?\n Type y for Yes and N for No \n Type your answer:"
    )
    if pepeAnswer == "y" or pepeAnswer == "Y":
        peperoni = input(
            "What size of peperoni do you want?\n Type s for smallPizzaPeperoni, l for largePizzaPeperoni \n Type your answer:"
        )
        if peperoni == "s" or peperoni == "S":
            bill += smallPizzaPeperoni
            print(f"\nYour bill is now {bill}\n")
        elif peperoni == "l" or peperoni == "L":
            bill += largePizzaPeperoni
            print(f"\nYour bill is now {bill}\n")
        else:
            print("You have not made a Valid Selection")
            break
    else:
        bill = bill
    chees = input(f"Do you want extra chees? Extra chess will cost extra {extraCheesForAnySizePizza}\n Type y for Yes, n for No \n Type your answer:")
    if chees == "y" or chees == "Y":
        bill += extraCheesForAnySizePizza
        print(f"\nYour total bill is {bill}")
    elif chess == "n" or chees == "N":
        print(f"\nYour total bill is {bill}")
    print("Enjoy your Snack")
