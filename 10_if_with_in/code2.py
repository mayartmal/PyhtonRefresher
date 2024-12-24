number = 7
user_input = input("Input 'y' if you would like to play: ")

if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You are right")
    elif abs(number - user_number) in (1, -1):
        print("You were off by one")
    else:
        print("Sorry, it is wrong")
