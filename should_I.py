import random

while True:
    print("Should I do coursera courses?")
    user = input("Press enter to see")
    if user == "":
        computer_choice = random.choice(["Yes", "No"])
        print(f"Computer: {computer_choice}")


# Got yes 4 times in a row. Guess its a sign