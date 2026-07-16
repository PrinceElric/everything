from random import shuffle, choices  # noqa: F401
import sys
from tools import *  # noqa: F403


def afficher_grille(grille, mode="joueur"):
    """Affiche la grille selon le mode : 'joueur' (brut) ou 'maitre' (avec filtres)"""
    for e in range(5):
        for i in range(5):
            mot = grille[e][i]
            if mode == "maitre":
                if mot in accepted_prop:
                    print(f"{NOIR_INVISIBLE}{mot:<15}{RESET}", end="")  # noqa: F405
                elif mot in mots_rouges:
                    print(f"{ROUGE}{mot:<15}{RESET}", end="")  # noqa: F405
                elif mot in mots_verts:
                    print(f"{VERT}{mot:<15}{RESET}", end="")  # noqa: F405
                else:
                    print(f"{mot:<15}", end="")

            else:
                if mot in accepted_prop:
                    print(f"{NOIR_INVISIBLE}{mot:<15}{RESET}", end="")  # noqa: F405
                else:
                    print(f"{mot:<15}", end="")
        print("")


def repetition_aceptation_rep(props):
    """augmente le nb de rep gave (de 1) et ajoute la proposition a une liste pour ensuite les masquer (next turn)"""
    global nb_rep_gave, accepted_prop
    nb_rep_gave += 1
    accepted_prop.append(props)


mots = choices(mots_921, k=25)  # noqa: F405
while len(set(mots)) != len(mots):
    mots = choices(mots_921, k=25)  # noqa: F405
accepted_prop, rouge, vert, pts, mots2, nb_rep_gave = (
    [],
    (range(3)),
    (range(5)),
    0,
    mots.copy(),
    0,
)
shuffle(mots)
shuffle(mots2)
matrice, matrice2 = (
    (mots[:5]),
    (mots[5:10]),
    (mots[10:15]),
    (mots[15:20]),
    (mots[20:]),
), ((mots2[:5]), (mots2[5:10]), (mots2[10:15]), (mots2[15:20]), (mots2[20:]))
mots_rouges = [matrice[4][i] for i in rouge]
mots_verts = [matrice[0][i] for i in vert] + [matrice[1][i] for i in vert[:2]]
while not set(accepted_prop) == set(mots_verts):
    clear()  # noqa: F405
    afficher_grille(matrice, mode="maitre")

    key_word = input("Enter a word for the person can devine:\n>>>   ").strip().lower()
    reponses = []

    while True:
        continueeee = 0
        reponses.append(
            input("What are the answers ?(q to quit)(enter for each one):   ")
            .lower()
            .strip()
        )
        for i in mots_rouges:
            if i in reponses:
                print(f"{ROUGE}Incorrect enter{RESET}")  # noqa: F405
                reponses.remove(i)
                continueeee = 1
        if continueeee == 1:
            continue
        if "q" in reponses:
            reponses.pop()
            break
        for i in reponses:
            if i not in mots:
                print(f"{ROUGE}Incorrect enter{RESET}")  # noqa: F405
                print(
                    f"{ROUGE}{GRAS}IMPORTANT : Les answers entered have been deleted bc you made a mistake!{RESET}"  # noqa: F405
                )  # noqa: F405
                reponses = []
                continueeee = 1
        if continueeee == 1:
            continue
        print("Element succesfuly added to the answers, what's the next ?")

    clear()  # noqa: F405
    nb_rep = 0
    print("The answers are: ", end="")
    for i in reponses:
        nb_rep += 1
        print(i, end="   ")
    print("")
    print(f"There are {nb_rep} rep at total")
    input("")
    clear()  # noqa: F405

    propositions, nb_rep_gave, nb_good_answ, pts_before = "", 0, 0, pts

    while True:
        clear()  # noqa: F405
        print(
            f"The player selected {nb_rep} words to find, the keyword is: {key_word}\n {VERT}GOOD LUKE{RESET}"  # noqa: F405
        )  # noqa: F405
        afficher_grille(matrice2)

        if nb_rep_gave == nb_rep:
            break
        propositions = (
            input(
                f"Which answer propose you ?(again {nb_rep - nb_rep_gave} to enter):\n>>> "
            )
            .lower()
            .strip()
        )
        if propositions not in mots:
            print(f"{ROUGE}Propostion invalid{RESET}")  # noqa: F405
            print("The proposition isn't in the table, pls select an other one")
            input('')
            continue
        if propositions in mots_rouges:
            print(f"{ROUGE}You lost!{RESET}")  # noqa: F405
            print(f"{VERT}{SOULIGN2}the answers were : {reponses}{RESET}")  # noqa: F405
            sys.exit(f"See you next time, you had {pts}pts")
        if propositions in mots_verts and propositions in reponses:
            pts += 1
            print(f"{VERT}You won 1pts, you are now to {pts}pts!{RESET}")  # noqa: F405
            repetition_aceptation_rep(propositions)
            nb_good_answ += 1
        elif propositions in reponses:
            print(
                f"{VERT}Very well answer but you didn't make points{RESET}"  # noqa: F405
            )  # noqa: F405
            print(f"{VERT}You have {pts}!{RESET}")  # noqa: F405
            repetition_aceptation_rep(propositions)
            nb_good_answ += 1
        else:
            print(f"{ROSE} Not good Answer,{RESET} keep schearching")  # noqa: F405
            repetition_aceptation_rep(propositions)
        input("")

    clear()  # noqa: F405
    print(
        f"The player selected the {nb_rep} reponses\n He found {nb_good_answ} good answers, and made {pts - pts_before}pts!"
    )
    input("Next round ?\n")

print(f"{VERT}{SOULIGN2}{GRAS}{ITALIC}You won!{RESET}")  # noqa: F405
print(f"You had {pts}pts !")
