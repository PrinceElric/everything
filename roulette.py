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
        0: "vert",
        1: "rouge",
        2: "noir",
        3: "rouge",
        4: "noir",
        5: "rouge",
        6: "noir",
        7: "rouge",
        8: "noir",
        9: "rouge",
        10: "noir",
        11: "noir",
        12: "rouge",
        13: "noir",
        14: "rouge",
        15: "noir",
        16: "rouge",
        17: "noir",
        18: "rouge",
        19: "rouge",
        20: "noir",
        21: "rouge",
        22: "noir",
        23: "rouge",
        24: "noir",
        25: "rouge",
        26: "noir",
        27: "rouge",
        28: "noir",
        29: "noir",
        30: "rouge",
        31: "noir",
        32: "rouge",
        33: "noir",
        34: "rouge",
        35: "noir",
        36: "rouge",
    }
    numero = random.choice(ROULETTE_EUROPEENNE)
    couleur = COULEURS_ROULETTE[numero]

    def roulette_animation(resultat):
        nonlocal ROULETTE_EUROPEENNE, COULEURS_ROULETTE, couleur
        print(f'{' ' * 18}↓')
        for i in range(30):
            numero = random.choice(ROULETTE_EUROPEENNE)

            couleur = COULEURS_ROULETTE[numero]

            if couleur == "rouge":
                affichage = f"{ROUGE_FLASH}{numero}{RESET}"
            elif couleur == "noir":
                affichage = f"{NOIR}{numero}{RESET}"
            else:
                affichage = f"{VERT_FLASH}{numero}{RESET}"

            print(f"\r{' ' * 16}[ {affichage:^5} ] ", end="", flush=True)

            time.sleep(0.02 + i * 0.008)

        print(
            f"\r{' ' * 16}[ {ROUGE_FLASH if COULEURS_ROULETTE[numero] == 'rouge' else NOIR if COULEURS_ROULETTE[numero] == 'noir' else VERT}{resultat}{RESET} ] ",
            flush=True,
        )

    roulette_animation(numero)


roulette_game()
