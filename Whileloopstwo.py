#RandomDrinkSelector
#This is useful to me because i am very undecisive when it comes to drinks to consume
import random
print("Hello, welcome to the random drink chooser thing")
drinks = []
drink = ""
while drink != 'done':
    drink = input("Please enter a drink (type 'done' when done): ")
    drinks.append(drink)
    print(f"{drink} has been added to the list")
    print(drinks)
    if drink == "done":
        drinks.remove("done")
        drinkstwo = "\n-".join(drinks)
        print(f"Your complete list is: \n-{drinkstwo}")
        option = input("Do you want a drink chosen from the list at random? (Y or N) ")
        if option == "N":
            break
        if option == "Y":
            randomone = random.choice(drinks)
            print(f"Your random drink is: {randomone}")