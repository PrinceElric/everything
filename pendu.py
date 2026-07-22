import sys, random, time, unicodedata  # noqa: E401, F401

sys.path.append(r"C:\Users\elric\Desktop\vs code\all that")
from tools import *  # noqa: F403

def start():
    global mots, mots_921, letter, letters, count_pendu, false_answers, count_pendu, pendu_etapes, word
    mots = mots_921.copy()  # noqa: F405
    mots, letter, letters, count_pendu, false_answers = (
        list(filter(lambda x: True if len(x) > 5 else False, mots_921)),  # noqa: F405
        "",
        [],
        0,
        [],
    )  # noqa: F405
    word = mots[random.randrange(0, len(mots))]  # noqa: F405
    word = enlever_accents(word)  # noqa: F405
    pendu_etapes = (
        " +---+\n |   \n     \n     \n     ",
        " +---+\n |   \n O   \n     \n     ",
        " +---+\n |   \n O   \n/|   \n     ",
        " +---+\n |   \n O   \n/|\\  \n     ",
        " +---+\n |   \n O   \n/|\\  \n/    ",
        " +---+\n |   \n O   \n/|\\  \n/ \\  ",
    )

def show_word(mode='normal'):
    if not letters and mode == 'normal':
        print("_" * len(word))
        return
    elif not letters:
        print(word[0] +( "_" * (len(word)-1)))
        return
    print(''.join(i if i in letters else '_' for i in word))
    print()


def enter_letter():
    global letter, false_answers, word, count_pendu
    while True:
        if false_answers:
            print(
                f'{ROUGE_FLASH}False letters:   {str(false_answers).replace('[', '').replace(']', '').replace("'", '')}{RESET}'  # noqa: F405
            )  # noqa: F405
        letter = input("enter a letter:    ").strip().lower()
        if letter in ["exit", "quit", "ex"]:
            clear()  # noqa: F405
            sys.exit()
        elif letter == 're':
            clear()  # noqa: F405
            word = random.choice(mots)  # noqa: F405
            word = enlever_accents(word)  # noqa: F405
            main()  # noqa: F405
        if letter == word:
            verif(True)
        if len(letter) != 1 or not letter.isalpha():
            cprint("JUST ONE LETTER!", ERROR)  # noqa: F405
            time.sleep(0.5)
            clear_lines(2)  # noqa: F405
            continue
        break
    clear_lines(1)  # noqa: F405
    if letter in letters or letter in false_answers:
        print('Answer already gave!')
        time.sleep(1)
        main()
    if letter in word:
        print(f"enter a letter:    {VERT_FLASH}{GRAS}{letter}{RESET}")  # noqa: F405
        print(f"{letter} {SUCCESS}is in the word!{RESET}")  # noqa: F405
        letters.append(letter)

    else:
        print(f"enter a letter:    {ROUGE_FLASH}{GRAS}{letter}{RESET}")  # noqa: F405
        print(f"{letter} {ERROR}not in the word!{RESET}")  # noqa: F405
        count_pendu += 1
        false_answers.append(letter)
    time.sleep(1)


def show_pendu(level: int = 0) -> None:
    print()
    for line in pendu_etapes[level].split("\n"):
        print(line)
    match level:
        case 0:
            clear_lines(3)  # noqa: F405
        case 1:
            clear_lines(2)  # noqa: F405
        case 2 | 3:
            clear_lines(1)  # noqa: F405
    print()


def verif(full=False):
    if not full:
        if len(false_answers) >= 5:
            print(f'Answer was {FOND_VERT}{word}{RESET}')  # noqa: F405
            cprint(f'You gave {len(false_answers)} bad answers!', ROUGE_FLASH+SOULIGN2)  # noqa: F405
            cprint(f'You had {len(letters)} good answers!', SUCCESS)  # noqa: F405
            cprint('But...', ROUGE_FLASH)  # noqa: F405
            cprint('You lost!', ERROR)  # noqa: F405
            end()
        elif len(letters) == len(set(word)):
            print(f'Answer was {FOND_VERT}{word}{RESET}')  # noqa: F405
            cprint('You found all the letters!', VERT_FLASH + SOULIGN2)  # noqa: F405
            cprint('And...', VERT)  # noqa: F405
            cprint('You won', SUCCESS)  # noqa: F405
            end()
        return
    cprint(f'You guessed the word!, it was good {word}', SUCCESS)  # noqa: F405
    cprint(f'You gave {len(letters)} good answers and {len(false_answers)} bad answers!', VERT)  # noqa: F405
    cprint('You won!', SUCCESS)  # noqa: F405
    end()


def end():
    choice = input('New round?\n')
    if choice:
        run()
    else:
        sys.exit()

def run(mode='normal'):
    start()
    def main(mode='normal'):
        while True:
            global count_pendu
            clear()  # noqa: F405
            show_pendu(count_pendu)
            verif()
            # print(word)  #uncomment to debug and test
            show_word(mode)
            enter_letter()
    main(mode)

run('non')
