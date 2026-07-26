import random, time, sys, string
import pyautogui as pag
from tools import *  # noqa: F403

mots_921 = list(filter(lambda x: True if len(x) > 5 else False, mots_921))
word = random.choice(mots_921)
word = enlever_accents(word)
letters, propositions_color, good_answ, esp, total_props, guesses = (
    list(set(list(word))),
    [],
    0,
    "    " if len(word) <= 9 else "   ",
    [],
    0,
)


def affichage():
    clear()
    faire_titre_section("Word Correspondance Game!")
    for prop in total_props:
        print(f"{esp}{prop}", end="\n")
    print(f" " * 28 + "_" * len(word))


def test_word():
    global good_answ, propositions_color, guesses, enter
    guesses += 1
    enter, propositions_color, good_answ = str(enter), [], 0
    for i in range(len(word)):
        if enter[i] == word[i]:
            propositions_color.append(f"{SUCCESS}{enter[i]}{RESET}")
            good_answ += 1
        elif enter[i] in letters:
            propositions_color.append(f"{WARNING}{enter[i]}{RESET}")
        else:
            propositions_color.append(f"{ERROR}{enter[i]}{RESET}")
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
        elif not enter.isalpha():
            cprint("Word must only contain letters!", ERROR)
            time.sleep(0.5)
            clear_lines(2)
            continue
        elif enter == "capa":
            cprint("Type '1' to reveal the word and exit.", WARNING)
            cprint("Type 're' to restart the game.", WARNING)
            time.sleep(1.5)
            clear_lines(3)
            continue
        elif enter == "help":
            enter = "".join(list(random.choices(string.ascii_lowercase, k=len(word))))
            pag.write(enter)
            time.sleep(0.7)
            for _ in range(len(enter)):
                pag.press('delete')
                time.sleep(0.1)
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
    elif guesses >= 10:
        affichage()
        clear_lines()
        cprint(f'Sorry but you lost!\n{VERT_FLASH}The word was {word}', ERROR)
        sys.exit()
