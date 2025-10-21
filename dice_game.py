import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():          # isdigit() checks if the input is actually a number
        players = int(players)     # if players is actually a number, convert it to an int. This prevents crashing if the input is something other than a number
        if 2 <= players <= 4:      # players must be greater than or equal to 2 AND be less than or equal to 4
            break
        else:
            print("Must be between 1 - 4 players.")
    else:
        print("Invalid, try again.")

print(players)