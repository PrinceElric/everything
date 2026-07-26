import random, time, sys, string
from tools import *  # noqa: F403


def word_guess_game(mode='nul', lenght_word_min=6, max_guesses=10):
    global mots_921
    mots_921 = list(
        filter(lambda x: True if len(x) >= lenght_word_min else False, mots_921)
    )
    word = random.choice(mots_921)
    word = enlever_accents(word)
    (
        letters,
        propositions_color,
        good_answ,
        esp,
        total_props,
        guesses,
        alphabet,
        letters_red,
        letters_yellow,
        letters_green,
    ) = (
        list(set(list(word))),
        [],
        0,
        "    " if len(word) <= 9 else "   ",
        [],
        0,
        string.ascii_lowercase,
        [],
        [],
        [],
    )

    def affichage():
        clear()
        faire_titre_section("Word Correspondance Game!")
        print("")
        for i in alphabet:
            if i in letters_green:
                print(f"{SUCCESS}{i}{RESET}", end=" ")
            elif i in letters_yellow:
                print(f"{WARNING}{i}{RESET}", end=" ")
            elif i in letters_red:
                print(f"{ERROR}{i}{RESET}", end=" ")
            else:
                print(i, end=" ")
        print("\n")
        if mode == "debug":
            print(f" " * 28 + {word})
        for prop in total_props:
            print(f"{esp}{prop}", end="\n")
        if max_guesses - guesses <= 3:
            print('\n')
            if max_guesses - guesses != 1:
                cprint(f'Just {max_guesses - guesses} guesses left!', WARNING)
            else:
                cprint('Just 1 attempt left!!', WARNING)
                cprint('Be really carefull!', WARNING)
        print(f" " * 28 + "_" * len(word))

    def test_word():
        nonlocal good_answ, propositions_color, guesses, enter, guesses
        guesses += 1
        enter, propositions_color, good_answ = str(enter), [], 0
        for i in range(len(word)):
            if enter[i] == word[i]:
                propositions_color.append(f"{SUCCESS}{enter[i]}{RESET}")
                if not enter[i] in letters_green:
                    letters_green.append(enter[i])
                    if enter[i] in letters_yellow:
                        letters_yellow.remove(enter[i])
                good_answ += 1
            elif enter[i] in letters:
                propositions_color.append(f"{WARNING}{enter[i]}{RESET}")
                if not enter[i] in letters_yellow and enter[i] not in letters_green:
                    letters_yellow.append(enter[i])
            else:
                propositions_color.append(f"{ERROR}{enter[i]}{RESET}")
                if not enter[i] in letters_red:
                    letters_red.append(enter[i])
        total_props.append(" ".join(propositions_color))

    while not good_answ == len(word) and not guesses >= 10:
        while True:
            affichage()
            enter = (
                input(f"Enter word of {WARNING}{len(word)} letters:{esp}{RESET}")
                .lower()
                .strip()
            )
            if enter.lower() in exit:
                cprint("Exiting the game.", WARNING)
                sys.exit()
            elif enter.lower() == "re":
                cprint("Restarting the game.", WARNING)
                exec(open(__file__).read())
            elif enter == "1":
                cprint(f"The word was: {SURLIGN2_BLANC}{word}", ERROR)
                sys.exit()
            elif enter in ["-help", "/help"]:
                cprint("Type '1' to reveal the word and exit.", WARNING)
                cprint("Type 're' to restart the game.", WARNING)
                cprint("Type 'help' to receive help with the word", WARNING)
                time.sleep(2)
                clear_lines(4)
                continue
            elif not enter.isalpha():
                cprint("Word must only contain letters!", ERROR)
                time.sleep(0.5)
                clear_lines(2)
                continue
            elif enter == "help":
                enter = "".join(
                    list(random.choices(string.ascii_lowercase, k=len(word)))
                )
                clear_lines()
                print(
                    f"Enter word of {WARNING}{len(word)} letters:{esp}{RESET}", end=""
                )
                slow_type(enter, 1, color=LOG_DISCRET)
                time.sleep(0.5)
            elif len(enter) != len(word):
                cprint(f"Word must be {len(word)} letters long!", ERROR)
                time.sleep(0.5)
                clear_lines(2)
                continue
            clear_lines(2)
            break
        test_word()
        if good_answ >= len(word):
            affichage()
            clear_lines(2)
            print(f"{SUCCESS}{esp}{' '.join(list(word))}{RESET}", end="\n")
            cprint(f"Congratulations! You found the word: {word}", SUCCESS)
            sys.exit()
        elif guesses >= max_guesses:
            affichage()
            clear_lines()
            cprint(f"Sorry but you lost!\n{VERT_FLASH}The word was {word}", ERROR)
            sys.exit()


word_guess_game()
