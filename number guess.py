import random, sys, time
from tools import *


def number_guess_game(minimum=0, maximum=100):
    clear()
    faire_titre_section("Number Guessing Game!")
    number_rand, guesses, my_number, choix ,  = int(random.randint(minimum, maximum)), 0, None, (1, 3)
    # print(f'Num is {number_rand}')
    def enter_num():
        nonlocal my_number, guesses
        while True:
            user_input = input(f"Please enter a number between {minimum} and {maximum}: ")
            if user_input.lower() in exit:
                cprint("Exiting the game.", WARNING)
                sys.exit()
            elif user_input.lower() == 're':
                cprint("Restarting the game.", WARNING)
                number_guess_game(minimum, maximum)
            elif user_input.strip() != user_input:
                high_low(cheat=True)
            try:
                my_number = int(user_input.strip())
            except ValueError:
                cprint("Invalid input. Please enter a valid number.", ERROR)
                time.sleep(0.5)
                clear_lines(2)
                continue

            if minimum <= my_number <= maximum:
                guesses += 1
                break

    def high_low(cheat=False):
        nonlocal number_rand, my_number, guesses
        if cheat:
            for _ in range(2):
                a = random.choice(choix)
                if a == 1:
                    print(f"{my_number} is too LOW! Try again!")
                    enter_num()

                else:
                    print(f"{my_number} is too HIGH! Try again!")
                    enter_num()
            end()
        if int(my_number) > number_rand:
            print(f"{my_number} is too High! Try again!")
        else:
            print(f"{my_number} is too Low! Try again!")

    def end():
        cprint("Congratulations! You guessed the number!", SUCCESS)
        cprint(f"You guessed {guesses} times!", WARNING)
        input("")
        sys.exit()

    while True:
        enter_num()
        if my_number == number_rand:
            end()
        high_low()

number_guess_game()
