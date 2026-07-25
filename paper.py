import random, time  # noqa: E401
from tools import *

faire_titre_section("Rock, Paper, Scissor Game")

choices, won, lose = ("rock", "paper", "scissor"), 0, 0

while True:
    computer = random.choice(choices)
    player = input("Enter your choice (q to quit): ")
    if player.lower() == 'q':
        break
    cheat = player != player.lower()

    if not player:
        player = random.choice(choices)
        print(f'Player chose {player.upper()}')
    else:
        player = player.lower()

    if player not in choices:
        cprint("You chose an invalid option", ERROR)
        time.sleep(0.7)
        clear_lines(2)
        continue

    if cheat:
        if player == "rock":
            computer = "scissor"
        elif player == "paper":
            computer = "rock"
        else:
            computer = "paper"

    print(f"the computer chose: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "paper":
        cprint("You lost!", ERROR)
        lose += 1
    elif player == "paper" and computer == "scissor":
        cprint("You lost!", ERROR)
        lose += 1
    elif player == "scissor" and computer == "rock":
        cprint("You lost!", ERROR)
        lose += 1
    else:
        cprint("You won!", SUCCESS)
        won += 1

print(f"{SUCCESS}you won {won} times,{RESET} {ERROR}and lost {lose} times{RESET}")
print(f"{SUCCESS}Good game!{RESET}" if won > lose else f"{ERROR}You will do it better next time!{RESET}")
input("Press enter to exit\n>>>    ")