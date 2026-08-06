from tools import *
import random, time


def Red_or_Black_game(mode=''):
    familys, values, historique, stats, color, card, tour, mise, prediction = (
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
        {},
        "",
        [],
        1,
        0,
        "",
    )
    cards = [f"{value}{color}" for color in familys for value in values]

    def game(tour=1):
        nonlocal stats, color, card, mise, prediction
        random.shuffle(cards)
        card = cards.pop()
        historique.append(card)
        stats = {
            "Rouge": f'%{(len(list(filter(lambda x: True if "♥" in x or "♦" in x else False, cards))) * 100)// len(cards):.2f}',
            "Noir": f'%{(len(list(filter(lambda x: True if "♣" in x or "♠" in x else False, cards))) * 100)// len(cards):.2f}',
        }
        color = (
            f"{ROUGE_FLASH}Rouge{RESET}"
            if "♥" in card or "♦" in card
            else f"{NOIR}Noir{RESET}"
        )
        if tour != 1:
            while True:
                mise = input("Enter a mise:   ")
                if not mise.isdigit() or int(mise) > config["sold"]:
                    cprint("incorrect", ERROR)
                    time.sleep(0.3)
                    clear_lines(2)
                    continue
                mise = int(mise)
                prediction = input("Enter your prediction (R/N):   ").lower()
                if prediction in ["r", "red", "rouge", "1", "sang", "s", "b", "blood"]:
                    prediction = f"{ROUGE_FLASH}Rouge{RESET}"
                else:
                    prediction = f"{NOIR}Noir{RESET}"
                cprint(f"You chosed §{prediction}!", SOULIGN2)
                time.sleep(0.35)
                break

    def affichage():
        nonlocal stats, color, mise
        random_card = random.choice(cards)
        clear()
        hist_affichage = [
            f"{ROUGE_FLASH}{x}{RESET}" if "♥" in x or "♦" in x else f"{NOIR}{x}{RESET}"
            for x in historique
        ]
        hist_str = " ".join(hist_affichage)
        print("+--------------------------------------------------+\n")
        print(f"{' ' * 13}RED OR BLACK\n")
        for i in range(30):
            random_card = random.choice(cards)
            print(
                f"\r{' ' * 15}[ {ROUGE if "♥" in random_card or "♦" in random_card else NOIR}{random_card}{RESET} ] ",
                end="",
                flush=True,
            )
            time.sleep(0.02 + (i * 0.01))
        print(
            f"\r{' ' * 15}[ {ROUGE if "♥" in card or "♦" in card else NOIR}{card}{RESET} ]   \n"
        )
        print(f"{' ' * 6}{ROUGE_FLASH}Rouge{RESET}{' ' * 13}{NOIR}Noir{RESET}")
        print(f"{' ' * 6}{stats['Rouge']}{' ' * 11}{stats['Noir']}\n")
        print("----------------------------------------------\n")
        if tour >= 2:
            if prediction == color:
                config["sold"] += mise
                cprint(f"You predicted {prediction} and §you Won!!", SUCCESS)
                cprint(f"You won €{mise*2}!", VERT_FLASH)
            else:
                config["sold"] -= mise
                cprint(f"You predicted {prediction}  §(wrong...)!", ERROR)
                cprint(f"You lost €{mise}!", ROUGE_FLASH)
            input()
            mise = 0
            clear_lines(4)
            print("----------------------------------------------\n")

        print(f"mise : {mise} €")
        print(f"solde : {config['sold']} €\n")
        print(hist_str)
        print("\n+--------------------------------------------------+")

    while config["sold"] > 0:
        game(tour)
        affichage()
        tour += 1


Red_or_Black_game()
