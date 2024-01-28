import random

# options = ["rock", "paper", "sissor"]
# win = 0
# choice = input("Enter your choice: ").lower()

# while True:
#     option = random.choice(options)
#     if option == choice:
#         win = "tie"
#         break
#     elif choice == "paper" and option == "rock":
#         win = 1
#         break
#     elif choice == "rock" and option == "sissor":
#         win = 1
#         break
#     elif choice == "sissor" and option == "paper":
#         win = 1
#         break
#     else:
#         win = 0
#         break

# print(f"Computer played: {option}")   
# print()     
# if win == 1:
#     print("** player Wins **")
# elif win == 0:
#     print("** Computer Wins **")
# else:
#     print("tie")


# Youtube's ways -->

options = ("rock", "paper", "scissors")

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")


    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == 'rock' and computer == "scissors":
        print("You win!")
    elif player == 'paper' and computer == "rock":
        print("You win!")
    elif player == 'scissors' and computer == "paper":
        print("You win!")
    else:
        print("you lose!")

    play_again = input("play again? (y/n): ").lower()
    if not play_again == 'y':
        running = False

print("Thanks for playing")