import sys
import tools
def paper():
    import random
    import time


    print("\n" * 50)
    print("rock, paper, scissor game !")

    is_running = True
    choices = ("rock", "paper", "scissor")
    won = 0
    lose = 0

    while is_running:
        computer = random.choice(choices)
        player = input("Enter your choice: ")

        cheat = player != player.lower()

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

        is_running = bool(input("Press Enter to continue or any key to quit: "))
        is_running = not is_running
    print(f"you won {won} times, and lost {lose} times")
    print("good game" if won > lose else "you will do it better next time!")
    time.sleep(1)


def number_guesss():
    import random

    print("\n" * 50)

    def numberr():
        global number
        while not number.isdigit():
            number = input(f"Please enter a number between {mini} and {maxi}: ")
        while not mini < int(number) < maxi:
            number = input(f"Please enter a number between {mini} and {maxi}: ")
        number = int(number)

    def high_low():
        global number_rand, number, guesses
        if number > number_rand:
            print(f"{number} is too high! Try again!")
            guesses += 1
            number = input(f"Please enter a number between {mini} and {maxi}: ")
            numberr()
        else:
            print(f"{number} is too low! Try again!")
            guesses += 1
            number = input(f"Please enter a number between {mini} and {maxi}: ")
            numberr()

    mini = 1
    maxi = 100
    cheat = False
    print("Welcome to the Number Guessing Game!")
    number_rand = random.randint(mini, maxi)
    number_rand = int(number_rand)
    number = input(f"Please enter a number between {mini} and {maxi}: ")
    guesses = 1
    if " " in number:
        cheat = True
    else:
        numberr()
    if cheat:
        for i in range(2):
            choi = (1, 2)
            a = random.choice(choi)
            if a == 1:
                print(f"{number} is too LOW! Try again!")
                number = input(f"Please enter a number between {mini} and {maxi}: ")
            else:
                print(f"{number} is too HIGH! Try again!")
                number = input(f"Please enter a number between {mini} and {maxi}: ")
            guesses += 1
    else:
        while number != number_rand:
            high_low()
    print("Congratulations! You guessed the number!")
    print(f"You guessed {guesses} times!")
    input("")


def f_50():
    import random

    print("\n" * 50)
    choix = ("pile", "face")
    piece = random.choice(choix)
    print(f" you chose {piece.upper()}")
    is_running = True
    while is_running:
        a = input("do you want to play again (y/n)? ")
        if a == " " or a.lower() == "y" or a == "":
            piece = random.choice(choix)
            print(f" you chose {piece.upper()}")
            is_running = True
        else:
            print("no problem, see you again")
            is_running = False
            input("")


print("welcome to the game store")
print("which game do you want to play ?:")
print("1) rock paper scissor")
print("2) guess a number")
print("3) flip a coin")
print('4. to quit')
game = input(">>>   ")
if game == "1":
    print("paper")
    paper()
elif game == "2":
    number_guesss()
elif game == "3":
    f_50()
else:
    print("please enter a valid input")
    sys.exit()
is_running = True
while is_running:
    print("\n" * 50)
    print("do you want to play again ?")
    print("1) rock paper scissor")
    print("2) guess a number")
    print("3) flip a coin")
    game = input(">>>   ")
    if game == "1":
        paper()
        is_running = True
    elif game == "2":
        number_guesss()
        is_running = True
    elif game == "3":
        f_50()
        is_running = True
    elif game == '4':
        print("thank for playing")
        is_running = False
    else:
        
        tools.shutdown()
