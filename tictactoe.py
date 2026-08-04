from tools import *
import time, random


def tictactoe_game():
    def game_style_selection():
        choix = menu_options(
            [
                "1. Solo (Joueur contre IA)",
                "2. Multi (Joueur contre Joueur)",
                "3. IA vs IA",
            ]
        )
        while True:
            if choix == "1. Solo (Joueur contre IA)":
                return "solo"
            elif choix == "2. Multi (Joueur contre Joueur)":
                return "multi"
            elif choix == "3. IA vs IA":
                return "ia"

    tictactoe_game_style = game_style_selection()

    def launch_tic_tac_toe(game_style="solo"):
        faire_titre_section("TicTacToe Game!")
        time.sleep(0.3)
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

        def est_grille_pleine():
            return all(cell != " " for ligne in vars["grille"] for cell in ligne)

        def coup_joueur():
            while True:
                try:
                    pos = input("Entrez votre coup (1-9): ")
                    num = int(pos)
                    if num < 1 or num > 9:
                        cprint("Veuillez entrer un nombre entre 1 et 9.", color=ERROR)
                        time.sleep(0.34)
                        clear_lines()
                        continue
                    ligne = (num - 1) // 3
                    col = (num - 1) % 3
                    if vars["grille"][ligne][col] != " ":
                        cprint("Cette case est déjà occupée!", color=ERROR)
                        time.sleep(0.34)
                        clear_lines()
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
                    cprint("Entrée invalide!")
                    time.sleep(0.34)
                    clear_lines()

        def coup_ia():
            cases_libres = [
                (i, j)
                for i in range(3)
                for j in range(3)
                if vars["grille"][i][j] == " "
            ]
            symbole = f"{ROUGE}X{RESET}" if vars["tour"] % 2 == 0 else f"{BLEU}O{RESET}"
            adversaire = (
                f"{BLEU}O{RESET}"
                if symbole == f"{ROUGE}X{RESET}"
                else f"{ROUGE}X{RESET}"
            )

            def trouver_coup_gagnant(symbole_recherche):
                for ligne, col in cases_libres:
                    vars["grille"][ligne][col] = symbole_recherche
                    gagne = verifier_victoire(symbole_recherche)
                    vars["grille"][ligne][col] = " "
                    if gagne:
                        return ligne, col
                return None

            if cases_libres:
                # Priorité à l'attaque : si l'IA peut gagner immédiatement, elle joue cette case.
                coup_attaque = trouver_coup_gagnant(symbole)
                if coup_attaque:
                    ligne, col = coup_attaque
                    vars["grille"][ligne][col] = symbole
                    slow_type("L'IA joue pour gagner!\n", color=WARNING)
                    return

                # Défense : si l'adversaire peut gagner au prochain tour, bloquer.
                coup_defense = trouver_coup_gagnant(adversaire)
                if coup_defense:
                    ligne, col = coup_defense
                    vars["grille"][ligne][col] = symbole
                    slow_type("L'IA bloque votre mouvement!\n", color=WARNING)
                    return

                slow_type("L'IA réfléchit...\n", color=WARNING)
                time.sleep(0.3)
                cases_vip, cases_centre = [(0, 0), (0, 2), (2, 0), (2, 2)], [
                    (1, 1)
                ]  # Coins and centre
                # Priorité aux cases vips, puis au centre, sinon choix aléatoire
                for ligne, col in cases_vip:
                    if vars["grille"][ligne][col] == " ":
                        vars["grille"][ligne][col] = symbole
                        return
                for ligne, col in cases_centre:
                    if vars["grille"][ligne][col] == " ":
                        vars["grille"][ligne][col] = symbole
                        return

                ligne, col = random.choice(cases_libres)
                vars["grille"][ligne][col] = symbole

        slow_type("Bienvenue dans le jeu TicTacToe!\n", color=WARNING)
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

        continue_choice = menu_options(["1. Rejouer", "2. Quitter"])
        if continue_choice == "1. Rejouer":
            mode_change = menu_options(["1. Garder le mode", "2. Le changer"])
            if mode_change == "1. Garder le mode":
                launch_tic_tac_toe(game_style)
            else:
                tictactoe_game_style = game_style_selection()
                launch_tic_tac_toe(game_style=tictactoe_game_style)
        else:
            slow_type("Merci d'avoir joué! À bientôt!\n", color=WARNING)
            time.sleep(0.67)
            clear()

    launch_tic_tac_toe(game_style=tictactoe_game_style)


tictactoe_game()
