from tools import *
import random, time

familys, values, historique = (
    ["♥", "♦", "♣", "♠"],
    [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    ],
    [],
)
cards = [f"{value}{color}" for color in familys for value in values]
for i in range(10):
    random.shuffle(cards)
    card = cards.pop()
    historique.append(card)
    stats = {
        "Rouge": f'%{(len(list(filter(lambda x: True if "♥" in x or "♦" in x else False, cards))) * 100)// 52}',
        "Noir": f'%{(len(list(filter(lambda x: True if "♣" in x or "♠" in x else False, cards))) * 100)// 52}',
    }
    print(card)
    color = (
        f"{ROUGE_FLASH}Rouge{RESET}"
        if "♥" in card or "♦" in card
        else f"{NOIR}Noir{RESET}"
    )
    print(color)
    print("$" + config["sold"])


def affichage():
    hist_affichage = [
        f"{ROUGE_FLASH}{x}{RESET}" if "♥" in x or "♦" in x else f"{NOIR}{x}{RESET}"
        for x in historique
    ]
    hist_str = " ".join(hist_affichage)
    print("+--------------------------------------------------+\n")
    print(f"{' ' * 13}RED OR BLACK\n")
    print(f"{' ' * 13}[ {card} ] -> {color}\n")
    print(f"{' ' * 6}{ROUGE_FLASH}Rouge{RESET}{' ' * 11}{NOIR}Noir{RESET}")
    print(f"{' ' * 7}{stats['Rouge']}{' ' * 12}{stats['Noir']}")
    print(hist_str)


affichage()
