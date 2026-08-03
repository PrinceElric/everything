from tools import *
import time

faire_titre_section("TicTacToe Game!")
time.sleep(0.4)
clear()

vars = {
    "grille" : [[" " for _ in range(3)] for _ in range(3)]
}
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
    if all(vars["grille"][i][i] == symbole for i in range(3)) or all(vars["grille"][i][2-i] == symbole for i in range(3)):
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
            vars["grille"][ligne][col] = "X"
            break
        except ValueError:
            print("Entrée invalide!")

def coup_ia():
    import random
    cases_libres = [(i, j) for i in range(3) for j in range(3) if vars["grille"][i][j] == " "]
    if cases_libres:
        ligne, col = random.choice(cases_libres)
        vars["grille"][ligne][col] = "O"

tour = 0
while not verifier_victoire("X") and not verifier_victoire("O") and not est_grille_pleine():
    afficher_grille()
    if tour % 2 == 0:
        coup_joueur()
    else:
        coup_ia()
    tour += 1

afficher_grille()
if verifier_victoire("X"):
    slow_type("Vous avez gagné! 🎉\n", color=WARNING)
elif verifier_victoire("O"):
    slow_type("L'IA a gagné!\n", color=WARNING)
else:
    slow_type("Match nul!\n", color=WARNING)
