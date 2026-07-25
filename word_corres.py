import random, time, sys
from tools import *  # noqa: F403

mots_921 = list(filter(lambda x: True if len(x) > 5 else False, mots_921))
word = random.choice(mots_921)
word = enlever_accents(word)
letters, propositions_color, good_answ, esp = (
    list(set(list(word))),
    [],
    [],
    "    " if len(word) <= 9 else "   ",
)


def affichage():
    clear()
    faire_titre_section("Word Correspondance Game!")
    print(word)
    print(letters)
    if good_answ:
        for i in range(len(propositions_color)):
            print(propositions_color[i], end=" ")
        print("\n")
    print(f" " * 28 + "_" * len(word))


while not sum(good_answ) == len(word):
    propositions_color, good_answ = [], []
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
        elif len(enter) != len(word):
            cprint(f"Word must be {len(word)} letters long!", ERROR)
            time.sleep(0.5)
            clear_lines(2)
            continue
        clear_lines(2)
        break
    good_answ = []
    for i in range(len(word)):
        if enter[i] == word[i]:
            propositions_color.append(f"{SUCCESS}{enter[i]}{RESET}")
            good_answ.append(1)
        elif enter[i] in letters:
            propositions_color.append(f"{WARNING}{enter[i]}{RESET}")
        else:
            propositions_color.append(f"{ERROR}{enter[i]}{RESET}")
    for i in range(len(propositions_color)):
        print(propositions_color[i], end=" ")
