import random, time  # noqa: E401

print("rock, paper, scissor game !")

is_running = True
choices = ("rock", "paper", "scissor")
won = 0
lose = 0

while is_running:
    computer = random.choice(choices)
    player = input("Enter your choice(q to quit): ")
    if player == 'q':
        is_running = False
        break
    cheat = player != player.lower()

    if not player:
        player = random.choice(choices)
        print(f'Player chose {player.upper()}')
    else:
        player = player.lower()

    while player not in choices:
        print("You chose an invalid option")
        player = input("Enter your choice: ")
        cheat = player != player.lower()
        player = player.lower()

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
        print("You lost!")
        lose += 1
    elif player == "paper" and computer == "scissor":
        print("You lost!")
        lose += 1
    elif player == "scissor" and computer == "rock":
        print("You lost!")
        lose += 1
    else:
        print("You win!")
        won += 1

print(f"you won {won} times, and lost {lose} times")
print("good game" if won > lose else "you will do it better next time!")
time.sleep(5)