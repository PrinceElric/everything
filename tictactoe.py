from tools import *
import time, random


def tictactoe_game(game_style="solo"):
    faire_titre_section("TicTacToe Game!")
    time.sleep(0.4)
    clear()

    vars = {"grille": [[" " for _ in range(3)] for _ in range(3)], "tour": 0}

    def afficher_grille():
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(vars["grille"][i][j], end="  ")
                else:
                    print(vars["grille"][i][j], end=" | ")
            print()

    def verifier_victoire(symbole):
        # Vérifie les lignes
        for ligne in vars["grille"]:
            if all(cell == symbole for cell in ligne):
                return True

        # Vérifie les colonnes
        for col in range(3):
            if all(vars["grille"][row][col] == symbole for row in range(3)):
                return True

        # Vérifie les diagonales
        if all(vars["grille"][i][i] == symbole for i in range(3)) or all(
            vars["grille"][i][2 - i] == symbole for i in range(3)
        ):
            return True

        return False

    slow_type("Bienvenue dans le jeu TicTacToe!\n", color=WARNING)

    def est_grille_pleine():
        return all(cell != " " for ligne in vars["grille"] for cell in ligne)

    def coup_joueur():
        while True:
            try:
                pos = input("Entrez votre coup (1-9): ")
                num = int(pos)
                if num < 1 or num > 9:
                    print("Veuillez entrer un nombre entre 1 et 9.")
                    continue
                ligne = (num - 1) // 3
                col = (num - 1) % 3
                if vars["grille"][ligne][col] != " ":
                    print("Cette case est déjà occupée!")
                    continue
                if game_style == "multi":
                    symbole = (
                        f"{ROUGE}X{RESET}"
                        if vars["tour"] % 2 == 0
                        else f"{BLEU}O{RESET}"
                    )
                    vars["grille"][ligne][col] = symbole
                else:
                    vars["grille"][ligne][col] = f"{ROUGE}X{RESET}"
                break
            except ValueError:
                print("Entrée invalide!")

    def coup_ia():
        cases_libres = [
            (i, j) for i in range(3) for j in range(3) if vars["grille"][i][j] == " "
        ]
        if cases_libres:
            ligne, col = random.choice(cases_libres)
            if game_style == "ia":
                symbole = (
                    f"{ROUGE}X{RESET}" if vars["tour"] % 2 == 0 else f"{BLEU}O{RESET}"
                )
                vars["grille"][ligne][col] = symbole
            else:
                vars["grille"][ligne][col] = f"{BLEU}O{RESET}"

    while (
        not verifier_victoire(f"{ROUGE}X{RESET}")
        and not verifier_victoire(f"{BLEU}O{RESET}")
        and not est_grille_pleine()
    ):
        afficher_grille()
        if game_style == "solo":
            if vars["tour"] % 2 == 0:
                coup_joueur()
            else:
                coup_ia()
        elif game_style == "multi":
            coup_joueur()
        elif game_style == "ia":
            coup_ia()
            time.sleep(0.7)
        vars["tour"] += 1
        time.sleep(0.5)
        clear()
    afficher_grille()
    if game_style == "multi":
        if verifier_victoire(f"{ROUGE}X{RESET}"):
            slow_type("Le joueur 1 (X) a gagné! 🎉\n", color=WARNING)
        elif verifier_victoire(f"{BLEU}O{RESET}"):
            slow_type("Le joueur 2 (O) a gagné! 🎉\n", color=WARNING)
        else:
            slow_type("Match nul!\n", color=WARNING)

    elif game_style == "solo":
        if verifier_victoire(f"{ROUGE}X{RESET}"):
            slow_type("Vous avez gagné! 🎉\n", color=WARNING)
        elif verifier_victoire(f"{BLEU}O{RESET}"):
            slow_type("L'IA a gagné! 🎉\n", color=WARNING)
        else:
            slow_type("Match nul!\n", color=WARNING)

    else:  # game_style == 'ia'
        if verifier_victoire(f"{ROUGE}X{RESET}"):
            slow_type("L'IA 1 (X) a gagné! 🎉\n", color=WARNING)
        elif verifier_victoire(f"{BLEU}O{RESET}"):
            slow_type("L'IA 2 (O) a gagné! 🎉\n", color=WARNING)
        else:
            slow_type("Match nul!\n", color=WARNING)


tictactoe_game(
    game_style="ia"
)  # Change to 'multi' for two players or 'ia' for AI vs AI
