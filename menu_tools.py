from tools import *
import tools as ts
import time


def menu_principal():
    def menu_CONSTANTES():
        faire_titre_section("CONSTANTES Menu!")
        time.sleep(0.7)
        constante = menu_options(["1. ANSI colors", "2. Listes", "3. Exit"])
        match constante:
            case "1. ANSI colors":
                # menu des colors
                pass
            case "2. Listes":
                print(f"\nContinue = {continuer}")
                print(f"Exit     = {exit}")
                input("")
                menu_CONSTANTES()
            case "3. Exit":
                return

    while True:
        principal = menu_options(
            ["1. Show CONSTANTES", "2. Show DONNÉES", "3. Show FONCTIONS", "4. Exit"]
        )
        match principal:
            case "1. Show CONSTANTES":
                menu_CONSTANTES()
            case "2. Show DONNÉES":
                # menu de mots_921 avec des infos...
                pass
            case "3. Show FONCTIONS":
                # menu le + imp avec les fonct
                pass
            case "4. Exit":
                return


faire_titre_section("Tools Menu!")
time.sleep(0.7)
menu_principal()
