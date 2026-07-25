import sys, random, time  # noqa: E401, F401

sys.path.append(r"C:\Users\elric\Desktop\vs code\all that")
from tools import *  # noqa: F403


def pendu_game(mode="normal"):
    global mots_921

    def start():
        global mots, count_down, mots_921, letter, letters, count_pendu, false_answers, pendu_etapes, word
        mots = mots_921.copy()
        mots, letter, letters, count_pendu, false_answers, count_down = (
            list(filter(lambda x: True if len(x) > 5 else False, mots_921)),
            "",
            [],
            0,
            [],
            6,
        )
        word = random.choice(mots)
        word = enlever_accents(word).lower()
        pendu_etapes = (
            " +---+\n     \n     \n     \n     ",
            " +---+\n |   \n     \n     \n     ",
            " +---+\n |   \n O   \n     \n     ",
            " +---+\n |   \n O   \n/|   \n     ",
            " +---+\n |   \n O   \n/|\\  \n     ",
            " +---+\n |   \n O   \n/|\\  \n/    ",
            " +---+\n |   \n O   \n/|\\  \n/ \\  ",
        )

    def show_word(mode="normal"):
        global count_down, word, letters
        if not letters and mode == "normal":
            print("_" * len(word))
            return
        elif not letters and mode == "facile":
            letters.append(word[0])
        elif not letters and mode == "tr_facile":
            letters.append(word[0])
            letters.append(word[-1])
        elif not letters and mode == "difficile":
            count_down = 4
        elif mode == "debug":
            print(f"word is {VERT_FLASH + SOULIGN2}{word}{RESET}")
        print("".join(i if i in letters else "_" for i in word))
        print()

    def enter_letter():
        global letter, false_answers, word, count_pendu
        while True:
            remaining_attempts = max(0, count_down - len(false_answers))
            cprint(f"Attempts left: {remaining_attempts}", WARNING)
            if false_answers:
                print(
                    f"{ROUGE_FLASH}False guesses:   {', '.join(false_answers)}{RESET}"
                )
            letter = input("enter a letter or a full word:    ").strip().lower()
            normalized_input = enlever_accents(letter)

            if normalized_input in ["exit", "quit", "ex"]:
                clear()
                sys.exit()
            elif normalized_input == "re":
                clear()
                run()
            elif normalized_input == word:
                verif_game(True)
                return
            if len(normalized_input) != 1 or not normalized_input.isalpha():
                cprint("JUST ONE LETTER OR A FULL WORD!", ERROR)
                time.sleep(0.5)
                if false_answers:
                    clear_lines(3)
                else:
                    clear_lines(2)
                continue

            clear_lines(1)
            if normalized_input in letters or normalized_input in false_answers:
                print("Answer already gave!")
                time.sleep(1)
                clear()
                return
            if normalized_input in word:
                print(f"enter a letter or a full word:    {VERT_FLASH}{GRAS}{normalized_input}{RESET}")
                print(f"{normalized_input} {SUCCESS}is in the word!{RESET}")
                letters.append(normalized_input)
            else:
                print(f"enter a letter or a full word:    {ROUGE_FLASH}{GRAS}{normalized_input}{RESET}")
                print(f"{normalized_input} {ERROR}not in the word!{RESET}")
                count_pendu += 1
                false_answers.append(normalized_input)
            time.sleep(1)
            return

    def show_pendu(level: int = 0) -> None:
        print()
        for line in pendu_etapes[level].split("\n"):
            print(line)
        match level:
            case 0:
                clear_lines(3)
            case 1:
                clear_lines(2)
            case 2 | 3:
                clear_lines(1)
        print()

    def verif_game(full_word=False):
        if not full_word:
            if len(false_answers) >= count_down:
                print(f"Answer was {FOND_VERT}{word}{RESET}")
                cprint(
                    f"You gave {len(false_answers)} bad answers!", ROUGE_FLASH + SOULIGN2
                )
                cprint(f"You had {len(letters)} good answers!", SUCCESS)
                cprint("But...", ROUGE_FLASH)
                cprint("You lost!", ERROR)
                end()
            elif len(letters) == len(set(word)):
                print(f"Answer was {FOND_VERT}{word}{RESET}")
                cprint("You found all the letters!", VERT_FLASH + SOULIGN2)
                cprint("And...", VERT)
                cprint("You won", SUCCESS)
                end()
            return
        cprint(f"You guessed the word!, it was good {word}", SUCCESS)
        print(
            f"{VERT}You gave {len(letters)} good answers {ROUGE}and {len(false_answers)} bad answers!{RESET}"
        )
        cprint("You won!", SUCCESS)
        end()

    def end():
        choice = input("New round? (y/n)\n").strip().lower()
        if choice in ["y", "yes", "o", "oui", "1"]:
            run()
        else:
            sys.exit()

    def main(mode="normal"):
        while True:
            global count_pendu
            clear()
            show_pendu(count_pendu)
            verif_game()
            show_word(mode)
            enter_letter()

    def run(mode="normal"):
        start()
        main(mode)

    run(mode)

pendu_game('')