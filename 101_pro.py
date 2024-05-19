import random
response = str("y")
while response == "y":
    no = random.randint(1,6)
    if no == 1:
        print("The number on the dice is 1")
    elif no == 2:
        print("The number on the dice is 2")
    elif no == 3:
        print("The number on the dice is 3")
    elif no == 4:
        print("The number on the dice is 4")
    elif no == 5:
        print("The number on the dice is 5")
    else:
        print("The number on the dice is 6")
    response = input("Press y to continue and n to exit ")
    print("\n")
