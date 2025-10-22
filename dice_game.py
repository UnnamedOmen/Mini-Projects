import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    print("""
\nRules:
Each turn you can roll the dice as much as you want.
Every roll will be added to your total score at the end of the turn.
However, if you roll a 1, the score you earned this turn will be erased and your turn ended.
(Only the points earned during that turn are erased. Your total score will stay the same.)
First to 50 points wins, good luck!""")
    players = input("\nEnter the number of players (2-4): ")
    if players.isdigit():          # isdigit() checks if the input is actually a number
        players = int(players)     # if players is actually a number, convert it to an int. This prevents crashing if the input is something other than a number
        if 2 <= players <= 4:      # players must be greater than or equal to 2 AND be less than or equal to 4
            break
        else:
            print("Must be between 1 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn!")
        print(f"Your total score is: {player_scores[player_idx]}")
        current_score = 0
        
        while True:
            should_roll = input("\nWould you like to roll (y)?")
            if should_roll.lower().strip() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")

            print(f"Your score is: {current_score}.")

        player_scores[player_idx] += current_score
        print(f"Your total score is {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print(f"Player number {winning_idx} wins with a score of {max_score}!")