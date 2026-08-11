from tools import *
import random, time, sys


def roulette_game():
    ROULETTE_EUROPEENNE = [
        0,
        32,
        15,
        19,
        4,
        21,
        2,
        25,
        17,
        34,
        6,
        27,
        13,
        36,
        11,
        30,
        8,
        23,
        10,
        5,
        24,
        16,
        33,
        1,
        20,
        14,
        31,
        9,
        22,
        18,
        29,
        7,
        28,
        12,
        35,
        3,
        26,
    ]
    COULEURS_ROULETTE = {
        0: "VERT",
        1: "ROUGE",
        2: "NOIR",
        3: "ROUGE",
        4: "NOIR",
        5: "ROUGE",
        6: "NOIR",
        7: "ROUGE",
        8: "NOIR",
        9: "ROUGE",
        10: "NOIR",
        11: "NOIR",
        12: "ROUGE",
        13: "NOIR",
        14: "ROUGE",
        15: "NOIR",
        16: "ROUGE",
        17: "NOIR",
        18: "ROUGE",
        19: "ROUGE",
        20: "NOIR",
        21: "ROUGE",
        22: "NOIR",
        23: "ROUGE",
        24: "NOIR",
        25: "ROUGE",
        26: "NOIR",
        27: "ROUGE",
        28: "NOIR",
        29: "NOIR",
        30: "ROUGE",
        31: "NOIR",
        32: "ROUGE",
        33: "NOIR",
        34: "ROUGE",
        35: "NOIR",
        36: "ROUGE",
    }
    numero = random.choice(ROULETTE_EUROPEENNE)
    couleur = COULEURS_ROULETTE[numero]
    compte = 0

    def roulette_animation(resultat):
        nonlocal ROULETTE_EUROPEENNE, COULEURS_ROULETTE, couleur, compte
        for num in ROULETTE_EUROPEENNE:
            compte += 1
            print(f'[ {match_color(COULEURS_ROULETTE[num])}{num}{RESET}]', end=' ')
            if compte == 12 or compte == 24:
                print('\n')
        print(f'\n{' ' * 32}↓')
        for i in range(30):
            numero = random.choice(ROULETTE_EUROPEENNE)

            couleur = COULEURS_ROULETTE[numero]

            if couleur == "ROUGE":
                affichage = f"{ROUGE_FLASH}{numero}{RESET}"
            elif couleur == "NOIR":
                affichage = f"{NOIR}{numero}{RESET}"
            else:
                affichage = f"{VERT_FLASH}{numero}{RESET}"

            print(f"\r{' ' * 30}[ {affichage:^5} ] ", end="", flush=True)

            time.sleep(0.02 + i * 0.008)

        print(
            f"\r{' ' * 30}[ {ROUGE_FLASH if COULEURS_ROULETTE[numero] == 'ROUGE' else NOIR if COULEURS_ROULETTE[numero] == 'NOIR' else VERT}{resultat}{RESET} ] ",
            flush=True,
        )

    roulette_animation(numero)


roulette_game()
