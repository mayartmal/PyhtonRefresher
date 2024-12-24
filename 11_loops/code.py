number = 7

while True:
    user_input = input("Do you want play more? ")
    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You are right")
    elif abs(number - user_number) == 1:
        print("You were off by one")
    else:
        print("Sorry, it is wrong")


print("Game over")
