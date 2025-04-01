import random

def roll_dice():
    """Simulates rolling a 6-sided die."""
    return random.randint(1, 6)

def play_game():
    print("🎲 Welcome to the Dice Game! 🎲")

    # Player 1 rolls the dice
    input("Player 1, press Enter to roll the dice...")
    player1_roll = roll_dice()
    print(f"Player 1 rolled: {player1_roll}")

    # Player 2 rolls the dice
    input("Player 2, press Enter to roll the dice...")
    player2_roll = roll_dice()
    print(f"Player 2 rolled: {player2_roll}")

    # Determine the winner
    if player1_roll > player2_roll:
        print("🎉 Player 1 wins! 🎉")
    elif player2_roll > player1_roll:
        print("🎉 Player 2 wins! 🎉")
    else:
        print("It's a tie! 🎲")

# Run the game
play_game()



# a dice game replication
# import random

# max_number = 6
# min_number = 1
#     def roll():
#     value = random.randint(min_number,max_number)

# while True:
#     response = input("Do you want to roll dice: [y/n]")
#     if response.lower() == 'y':
#         current_score = 0
#         current_score += value
#         print(f"you rolled a {roll()}")
#         print(f"you current score is : {current_score}")
#         if roll() == 1:
#             print("game over")
#             current_score = 0
#         else:
#             continue
#     elif response.lower()== 'n':
#         print("Game over")