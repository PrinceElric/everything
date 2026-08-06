"""
===============================================================================
                        DOCUMENTATION DU FICHIER TOOLS.PY
===============================================================================

Ce fichier regroupe un ensemble de fonctions utilitaires destinées à simplifier
le développement de scripts Python. Il fournit des outils pour l'affichage
dans le terminal, la génération de données, la manipulation de chaînes de
caractères, la journalisation, l'automatisation ainsi que diverses opérations
sur le système.

-------------------------------------------------------------------------------
1. DÉPENDANCES ET PRÉREQUIS
-------------------------------------------------------------------------------

Bibliothèques standards utilisées :
    - os
    - time
    - sys
    - subprocess
    - random
    - string
    - msvcrt
    - json
    - hashlib
    - unicodedata
    - itertools
    - datetime
    - mots_francais

Bibliothèque externe (optionnelle) :
    - pyautogui
      Utilisée uniquement pour les fonctions d'automatisation de la souris.

      Installation :
          pip install pyautogui

-------------------------------------------------------------------------------
2. INITIALISATION
-------------------------------------------------------------------------------

Au chargement du module :

    • Le fichier temporaire "tempo diary.md" est automatiquement réinitialisé.

Variables globales :

    • PATH_TEMP
        Chemin du fichier temporaire.

    • _timers
        Dictionnaire utilisé par les fonctions de chronométrage.

-------------------------------------------------------------------------------
3. CONSTANTES
-------------------------------------------------------------------------------

Le module fournit de nombreuses constantes ANSI permettant de personnaliser
l'affichage dans le terminal :

    • Styles de texte
        GRAS
        ITALIC
        SOULIGN2
        ...

    • Couleurs classiques
        ROUGE
        VERT
        JAUNE
        BLEU
        NOIR
        BLANC
        ...

    • Couleurs haute intensité
        ROUGE_FLASH
        VERT_FLASH
        JAUNE_FLASH
        BLEU_FLASH
        NOIR_FLASH
        BLANC_FLASH
        ...

    • Couleurs de fond
        FOND_ROUGE
        FOND_BLEU
        FOND_BLANC
        ...

    • Styles prédéfinis
        ERROR
        WARNING
        SUCCESS
        STYLE_TITRE
        MENU_ACTIF
        ALERTE_CRITIQUE


Le module propose également des listes pour sortir des input des programmes:

• Continuer

• Exit

• Others

-------------------------------------------------------------------------------
4. DONNÉES
-------------------------------------------------------------------------------

mots_921

    Liste contenant aux alentours de 19000 mots français utilisée par certaines fonctions du
    module.

-------------------------------------------------------------------------------
5. FONCTIONS DISPONIBLES
-------------------------------------------------------------------------------

--- Terminal ---

• clear()
    Efface le terminal Windows.

• cprint(texte, color)
    Affiche un texte avec une couleur ANSI.

• slow_type(texte, tps_total=0, tps_btw_letters=0, color=LOG_DISCRET)
    Simule un effet de frappe caractère par caractère.

• loading_bar(tps, symbol="#", lenght=10)
    Affiche une barre de progression animée.

• clear_lines(n=1)
    Efface les dernières lignes du terminal.

• faire_titre_section(texte, symbole='-', largeur=60)
    Affiche un titre centré et décoré.

• menu_options(options)
    Affiche un menu interactif navigable au clavier.


-------------------------------------------------------------------------------

--- Text ---

• enlever_accents(texte: str)
    Supprime les accents d'une chaîne.

• formate_collections(*args)
    Améliore l'affichage des listes, tuples et ensembles.

• fullmaj(txt)
    Convertit un texte selon une table de correspondance personnalisée.

• format_number(n)
    Formate un nombre avec un séparateur de milliers.

• random_password(n=10, Maj=True, digits=True, punctuation=True, space=True, tiret_bas=False)
    Génère un mot de passe aléatoire.

• random_username(n=7, Maj=True, digits=True, punctuation=False, space=False, tiret_bas=True)
    Génère un nom d'utilisateur aléatoire.

• random_string(n=7, Maj=True, digits=True, punctuation=False, space=True, tiret_bas=False)
    Génère une chaîne aléatoire personnalisable.

• abreviation(word="")
    return word abrevated, first letter + len + last letter

• seq(txt="")
    return the max continue chaine of a carac in txt

• arc_en_ciel(txt, mode="normal")
    Affiche un texte avec des couleurs aléatoires pour chaque caractère.


-------------------------------------------------------------------------------

--- System ---

• copier_txt(texte)
    Copie un texte dans le presse-papiers Windows.

• detect_shutdown()
    Annule plusieurs fois une extinction programmée.

• shutdown_A()
    Exécute "shutdown -a".

• hach_word(word)
    Retourne le hash SHA-256 d'une chaîne.

• shutdown(temps=40, kill=False)
    shutdown le PC avec multiples parfeux et eggs, pwrd, escape and just death

• start_timer(nom="default", entrées=False)
    Démarre un chronomètre.

• stop_timer(nom="default", entrées=False)
    Arrête un chronomètre et affiche le temps écoulé.

• human_time(n)
    Convertit des secondes en HHh:MMmin:SSs.

• valid_input(type="int", phrase="")
    Force une saisie valide du type demandé.


-------------------------------------------------------------------------------

--- Journalisation (Logging) ---

• ecrire_log(message, type_log, chemin_fichier)
    Écrit un message horodaté dans un fichier Markdown.

• log_info(...)
    Écrit un message de niveau INFO.

• log_warning(...)
    Écrit un message de niveau WARNING.

• log_error(...)
    Écrit un message de niveau ERROR.

-------------------------------------------------------------------------------

--- Automatisation ---

• afk_mouse(n, kill)
    Déplace automatiquement la souris et effectue des clics.

-------------------------------------------------------------------------------

--- Crypto ---

• cesar()
    Lance un menu interactif pour chiffrer et déchiffrer du texte avec le chiffre de César.

• brute_force(password='')
    Force un mot de passe en testant les longueurs au fur et à mesure.

• morse(txt='')
    Renvoi l'entrée en morse.

• fibonacci()
    Répète la sequ de fibonacci et offre des options de séléctions de données.

--------------------------------------------------------------------------------------------------------------------------------------------------------------

--- Jeux ---

• pendu_game(mode="normal")
    Lance le jeu du pendu.
• paper_scissor_game()
    Lance le jeu du papier-ciseaux avec capacité de triche.
• number_guess_game(minimum=0, maximum=100)
    Lance le jeu du nombre à deviner avec capa de triche.
• code_names_game()
    Lance le jeu du code names.
• pile_face_game(load=True)
    Just pile/face game! great animation and cheat capa->J
• word_guess_game(mode="nul", lenght_word_min=6, max_guesses=10)
    The word_guess_game were you input word and make color on letter -> /help
• dice(face=6, n=1)
    Simule n lances de dés à n_faces faces.
• Tictac_toe_game()
    Simule le jeu du morpion avec diff styles de jeux.
• menu_game()
    Lance le menu de jeux.


--------------------------------------------------------------------------------------------------------------------------------------------------------------

--- Outils Spécifiques au Projet ---

• trouver_nom(objet)
    Recherche le nom global associé à un objet.

• fonct_mots()
    Permet de rechercher et d'ajouter des mots à la liste mots_921.

• kanekicount(number, base)
    Soustrait une valeur de base jusqu'à atteindre zéro.

• def match_color(color):
    Renvoie la couleur ANSI correspondante à un nom donné.


--------------------------------------------------------------------------------------------------------------------------------------------------------------

--- Executables ---

• start_timer()

• loading_bar(0.4, symbol="*", lenght=10, exe=True)

===============================================================================
"""

# -------------------------------------------------------------------------------
# 1. DÉPENDANCES ET PRÉREQUIS
# -------------------------------------------------------------------------------

import os, time, sys, subprocess, random, string, msvcrt, json, hashlib, unicodedata, itertools  # noqa: E401
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
try:
    from mots_francais import mots
except Exception:
    mots = []
    json_path = os.path.join(current_dir, "mots_francais.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, encoding="utf-8") as f:
                mots = json.load(f)
        except Exception:
            mots = []
try:
    import pyautogui as pag
except ImportError:
    pag = None  # Évite le plantage si absent

# -------------------------------------------------------------------------------
# 2. INITIALISATION
# -------------------------------------------------------------------------------

# --- Réinitialisation automatique du fichier temporaire au démarrage ---
PATH_TEMP = r"C:\Users\elric\Desktop\vs code\all that\tempo diary.md"
try:
    with open(PATH_TEMP, "w", encoding="utf-8") as f:
        f.write("")  # On écrase avec du vide UNE SEULE FOIS au début !
except:  # Si le dossier existe pas encore, pas de crash  # noqa: E722
    pass

# -------------------------------------------------------------------------------
# 3. CONSTANTES
# -------------------------------------------------------------------------------

# --- Styles de texte ---
RESET = "\033[0m"
GRAS = "\033[1m"
ITALIC = "\033[3m"
SOULIGN2 = "\033[4m"
SURLIGN2_BLANC = "\033[7m"
NOIR_INVISIBLE = "\033[8m"
BARR2 = "\033[9m"

# --- Couleurs classiques ---
GRIS = "\033[2m"
ROUGE = "\033[31m"
VERT = "\033[32m"
JAUNE = "\033[33m"
BLEU = "\033[34m"
NOIR = "\033[30m"
BLANC = "\033[37m"
ROSE = "\033[35m"
CYAN = "\033[36m"

# --- Couleurs Haute Intensité ---
ROUGE_FLASH = "\033[91m"
VERT_FLASH = "\033[92m"
JAUNE_FLASH = "\033[93m"
BLEU_FLASH = "\033[94m"
NOIR_FLASH = "\033[90m"
BLANC_FLASH = "\033[97m"
ROSE_FLASH = "\033[95m"
CYAN_FLASH = "\033[96m"

# --- Couleurs de Fond ---
FOND_NOIR = "\033[40m"
FOND_ROUGE = "\033[41m"
FOND_VERT = "\033[42m"
FOND_JAUNE = "\033[43m"
FOND_BLEU = "\033[44m"
FOND_ROSE = "\033[45m"
FOND_CYAN = "\033[46m"
FOND_GRIS = "\033[100m"  # Fond sombre discret
FOND_BLANC = "\033[107m"  # Fond blanc haute luminosité

# --- Couleurs de Fond ---
FOND_NOIR = "\033[40m"
FOND_ROUGE = "\033[41m"
FOND_VERT = "\033[42m"
FOND_JAUNE = "\033[43m"
FOND_BLEU = "\033[44m"
FOND_ROSE = "\033[45m"
FOND_CYAN = "\033[46m"
FOND_GRIS = "\033[100m"  # Fond sombre discret

# --- Super Fusions  ---
ERROR = ROUGE_FLASH + GRAS + SOULIGN2
WARNING = JAUNE_FLASH + ITALIC
SUCCESS = VERT_FLASH + GRAS
STYLE_TITRE = "\033[30m" + FOND_CYAN + GRAS  # Texte Noir sur Fond Cyan
MENU_ACTIF = "\033[97m" + FOND_BLEU + GRAS  # Texte Blanc sur Fond Bleu
LOG_DISCRET = GRIS + ITALIC  # Gris et penché
ALERTE_CRITIQUE = "\033[97m" + FOND_ROUGE + GRAS  # Texte Blanc sur Fond Rouge


# listes de sortie d'input

continuer = ("continue", "c", "cont", "go", "next", "1", "y", "yes", "o", "oui")
exit = ("exit", "ex", "quitter", "quit", "q", "0", "n", "no", "non")
others = ("other", "o", "autre")
colors = (
    "BARR2",
    "SURLIGN2_BLANC",
    "NOIR_INVISIBLE",
    "SOULIGN2",
    "ITALIC",
    "GRAS",
    "RESET",
    "CYAN",
    "ROSE",
    "BLEU",
    "JAUNE",
    "VERT",
    "GRIS",
    "ROUGE",
    "NOIR",
    "BLANC",
    "CYAN_FLASH",
    "ROSE_FLASH",
    "BLEU_FLASH",
    "JAUNE_FLASH",
    "VERT_FLASH",
    "ROUGE_FLASH",
    "NOIR_FLASH",
    "BLANC_FLASH",
    "FOND_GRIS",
    "FOND_CYAN",
    "FOND_ROSE",
    "FOND_BLEU",
    "FOND_JAUNE",
    "FOND_VERT",
    "FOND_ROUGE",
    "FOND_NOIR",
    "ALERTE_CRITIQUE",
    "LOG_DISCRET",
    "MENU_ACTIF",
    "STYLE_TITRE",
    "SUCCESS",
    "WARNING",
    "ERROR",
)


# -------------------------------------------------------------------------------
# 4. DONNÉES
# -------------------------------------------------------------------------------

mots_921 = list(mots)


# -------------------------------------------------------------------------------
# 5. FONCTIONS DISPONIBLES
# -------------------------------------------------------------------------------

# -------------------------------------------------------------------------------

# --- Terminal ---


def clear():
    """Nettoie le terminal"""
    os.system("cls")


def cprint(texte, color):
    """Affiche texte coloré puis réinitialise style."""
    if '§' in texte and '!' in texte: # balises de repère
        texte = texte.replace('§', color).replace('!', RESET)
        print(texte)
        return
    print(f"{color}{texte}{RESET}")

def slow_type(texte, tps_total=0, tps_btw_letters=0.03, color=LOG_DISCRET):
    """Print string character by character with tiny delay. and color if you want"""
    for letter in texte:
        if tps_total:
            temps_de_latence = tps_total / len(texte)
            time.sleep(float(temps_de_latence))
            print(f"{color}{letter}{RESET}", end="", flush=True)
        elif tps_btw_letters:
            time.sleep(float(tps_btw_letters))
            print(f"{color}{letter}{RESET}", end="", flush=True)


def loading_bar(tps, symbol="#", lenght=10, exe=False):
    """Barre de progression avec étapes X/Y et pourcentage exact."""
    pourc1 = 100 / lenght
    for i in range(1, lenght + 1):
        pourcentage = i * pourc1
        barre = symbol * i
        vide = "." * (lenght - i)

        clear_lines()
        cprint(f"[{barre}{vide}]    {i}/{lenght}  ({pourcentage:.1f}%)", LOG_DISCRET)
        time.sleep(tps / lenght)

    clear_lines()
    slow_type(
        f"[{symbol * lenght}]    {lenght}/{lenght} (100.0%)",
        tps_total=0.4,
        color=VERT_FLASH,
    )
    time.sleep(0.3)
    if exe:
        clear()
    else:
        clear_lines()


def clear_lines(n=1):
    """Efface un nombre de lignes donne dans le terminal."""
    for _ in range(n):
        sys.stdout.write("\033[1F\033[2K")
    sys.stdout.flush()


def faire_titre_section(texte, symbole="-", largeur=60):
    """mettre texte et symbole, funct centre et fait une ligne de symbole de size largeur"""
    texte_grand = texte.upper()
    clear()
    print(symbole * largeur)
    print(f"{STYLE_TITRE}{texte_grand.center(largeur)}{RESET}")
    print(symbole * largeur)


def menu_options(options, titre="=== MENU INTERACTIF ==="):
    """enter a list of options, show a interactif select menu, return the option chose"""
    index, taille = 0, len(options)

    while True:
        clear()
        if not "=" in titre:
            titre = f"=== {titre.upper()} ==="
        print(titre)
        # Afficher options
        for i in range(taille):
            if i == index:
                print(f"{MENU_ACTIF} > {options[i]} {RESET}")
            else:
                print(f"   {options[i]}")

        # Attendre touche
        touche: bytes = msvcrt.getch()

        # Si touche spéciale (comme les vraies flèches)
        if touche in (b"\x00", b"\xe0"):
            touche = msvcrt.getch()  # Lire deuxième code
            if touche == b"H":  # Flèche Haut
                index = (index - 1) % taille
            elif touche == b"P":  # Flèche Bas
                index = (index + 1) % taille
        elif touche == b"\r":  # Touche Entrée
            return options[index]


# -------------------------------------------------------------------------------


# --- Text ---
def enlever_accents(texte: str) -> str:
    """remove accents and things like that from the text and return"""
    return "".join(
        c
        for c in unicodedata.normalize("NFD", texte)
        if unicodedata.category(c) != "Mn"
    )


def formate_collections(*args):
    """formate a collection into a str without the coast and komma-> ' '"""
    if isinstance(*args, list):
        return str(*args).replace("[", "").replace("]", "").replace("'", "")
    elif isinstance(*args, tuple):
        return str(*args).replace("(", "").replace(")", "").replace("'", "")
    elif isinstance(*args, set):
        return str(*args).replace("{", "").replace("}", "").replace("'", "")


def fullmaj(txt):
    """remake txt like the shift was turned on the other mode"""
    a = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + "1234567890"
        + "&é\"'(-è_çà)=^$ù*,;:!"
        + "°+¨£%µ?./§"
    )
    b = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + "&é\"'(-è_çà"
        + "1234567890°+¨£%µ?./§"
        + ")=^$ù*,;:!"
    )

    def MAJ(txt):
        texte_exit = ""
        for i in txt:
            if i == " ":
                texte_exit += " "
                continue
            c = a.index(i)
            d = b[c]
            texte_exit += d
        return texte_exit

    return MAJ(txt)


def format_number(n):
    """Formate un nombre en le sequencant en pattern de 3"""
    return f"{n:,}".replace(",", "'")


def random_password(
    n=10, Maj=True, digits=True, punctuation=True, space=True, tiret_bas=False
):
    """make a password of size n with or without Maj, digit and punct°"""
    char, txt_password = string.ascii_lowercase, ""
    if Maj:
        char += string.ascii_uppercase
    if digits:
        char += string.digits
    if punctuation:
        char += string.punctuation
    if space:
        char += " "
    if tiret_bas:
        char += "_"
    while True:
        try:
            txt_password = "".join(random.choices(char, k=n))
            return txt_password
        except:  # noqa: E722
            pass


def random_username(
    n=7, Maj=True, digits=True, punctuation=False, space=False, tiret_bas=True
):
    "" "based on the original random_password, chages the parameter to make a username valid''"
    return random_password(n, Maj, digits, punctuation, space, tiret_bas)


def random_string(
    n=7, Maj=True, digits=True, punctuation=False, space=True, tiret_bas=False
):
    "" "based on the original random_password, chages the parameter to make a valid normal string''"
    return random_password(n, Maj, digits, punctuation, space, tiret_bas)


def abreviation(word=""):
    """return word abrevated, first letter + len + last letter"""
    if not word:
        word = str(input("Enter a word!:    ")).lower().strip()
    if not word.isalpha() and " " not in word:
        cprint("Invalid enter!", ERROR)
        abreviation()
    if len(word.split()) != len(word):
        texte = ""
        for i in word.split():
            texte += i[0] + str(len(i)) + i[len(i) - 1] + " "
        return texte
    if len(word) > 2:
        return word[0] + str(len(word)) + word[len(word) - 1]
    else:
        return word


def seq(txt=""):
    """return the max continue chaine of a carac in txt"""
    if not txt:
        txt = input()
    max_len = 1
    cur_len = 1

    for i in range(1, len(txt)):
        if txt[i] == txt[i - 1]:
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        else:
            cur_len = 1

    return max_len


def arc_en_ciel(txt, mode="normal"):
    """print txt with random color for each letter, mode can be normal, gras, italic, underline, surligne or ANSI"""
    textee = []
    for i in txt:
        if i == " ":
            textee.append(" ")
            continue
        if mode == "normal":
            textee.append(f"\033[38;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "gras":
            textee.append(f"\033[1;38;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "italic":
            textee.append(f"\033[3;38;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "underline":
            textee.append(f"\033[4;38;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "surligne":
            textee.append(f"\033[48;5;{random.randint(16, 231)}m{i}{RESET}")
        elif mode == "ansi":
            textee.append(f"{match_color(random.choice(colors))}{i}{RESET}")

    return "".join(textee)


# -------------------------------------------------------------------------------

# --- System ---


def copier_txt(texte):
    """copie texte dans presse-papier, subprocess"""
    subprocess.run(["clip"], input=texte, text=True, check=True)


def detect_shutdown():
    """shutdown -a two times with sleep of 0.4 btw the two"""
    for _ in range(2):
        os.system("shutdown -a")
        time.sleep(0.4)


def shutdown_A():
    """shutdown -a"""
    os.system("shutdown -a")


def hach_word(word):
    """genere the hach of a word and return a 64 carac string in hexadecimal"""
    return hashlib.sha256(word.encode()).hexdigest()


def shutdown(temps=40, kill=False):
    """Arrêt du PC avec protection par mot de passe et bien d'autres."""

    def load_config(chemin="config.json"):
        """Charge la configuration JSON en toute sécurité. Renvoie un dict vide si échec."""
        if not os.path.exists(chemin):
            return {
                "password": "199e4be985e52e949b9628336ec91b740b03d6911c0096a5156370f118ea6405"
            }
        try:
            with open(chemin, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {
                "password": "199e4be985e52e949b9628336ec91b740b03d6911c0096a5156370f118ea6405"
            }

    def save_config(data, chemin="config.json"):
        """Sauvegarde les données dans un fichier JSON. Renvoie un booléen de succès."""
        try:
            with open(chemin, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception:
            return False
        copier_txt("shutdown -a")

    config = load_config()
    password_reel = config["password"]

    def launch_shutdown(temps):
        shutdown_A()
        clear()
        os.system(f"shutdown -s -t {temps}")

    def temps_stay():
        return timer - (time.time() - debut)

    def force_shutdown(timer=6, mode_normal=True, password=""):

        launch_shutdown(timer)
        print(f"{ALERTE_CRITIQUE}shutdown executed{RESET}")
        timer_final, cancelled = max(0, timer - 1.5), False
        if mode_normal:
            if password == "":
                shutdown()
        while timer_final >= 0:
            print(f"{ALERTE_CRITIQUE}\rtime left {timer_final:.2f}s{RESET}", end="")
            time.sleep(0.01)
            timer_final -= 0.01
            if mode_normal and timer_final < 1 and password == " ":
                print(f"{SUCCESS}\rtime left {timer_final:.2f}s{RESET}", end="")
                shutdown_A()
                cancelled = True
                break
        if not cancelled:
            for _ in range(10):
                os.system("start")
        elif mode_normal:
            cmd = subprocess.Popen(
                "cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            cmd.kill()
            try:
                number = int(
                    input(f"\n{SUCCESS}Which number to finish ?:{RESET}\n>>>  ")
                )
            except:  # noqa: E722
                print("GO TO HELL!")
                launch_shutdown(0)
            else:
                if number not in [3, 7]:
                    print("GO TO HELL!")
                    launch_shutdown(0)

    shutdown_A()
    clear()
    if kill:
        force_shutdown(mode_normal=False)
        return

    print(f"{ALERTE_CRITIQUE}Attention, votre PC va s'éteindre dans 1 minute!{RESET}")
    time.sleep(0.5)

    timer = temps
    os.system(f"shutdown -s -t {timer}")
    print(f"{GRAS}shutdown executed{RESET}")
    debut = time.time()
    cmd = subprocess.Popen("cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(0.7)
    cmd.kill()
    print(f"{WARNING}Arrêt planifié. {RESET}")
    hide_password = "*******160$"
    print(f"password is {hide_password}")
    password = input("what is the password ?\n").strip()

    if hach_word(password) == password_reel:
        shutdown_A()
        print(f"{SUCCESS}operation cancelled with {temps_stay():.3f}s left{RESET}")
    else:
        clear()
        print(f"{ERROR}WRONG PASSWORD{RESET}\n")

        now = temps_stay()
        t = now - 3
        while now >= t and now > 0:
            print(f"\r{ERROR}{now:.2f}s left{RESET}", end="")
            now -= 0.01
            time.sleep(0.01)

        clear()
        print(f"password is {hide_password}")
        password = input("\nOne more chance:  ")
        if password == " ":
            pass  # mot de passe spécial
        else:
            password = password.strip()
            if password:
                password = hach_word(password)

        if password == password_reel:
            shutdown_A()
            print(f"{SUCCESS}operation cancelled with {temps_stay():.2f}s left{RESET}")
        else:
            print(f"{ALERTE_CRITIQUE}WRONG AGAIN!!\nJUST GO TO HELL GUY!{RESET}")
            time.sleep(0.5)
            clear()

            force_shutdown(password=password)
            print("")
    cmd = subprocess.Popen("cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(0.7)
    cmd.kill()
    clear()
    print(f"{SUCCESS}Arrêt annulé.{RESET}")
    detect_shutdown()
    clear()


# shutdown(kill=True)

_timers = {}


def start_timer(nom="default", entrees=False):
    """Démarre ou réinitialise un chrono avec un nom donné."""
    global _timers
    start = time.process_time() if not entrees else time.perf_counter()
    _timers[nom] = start


def stop_timer(nom="default", entrees=False):
    """Arrête chrono et affiche/renvoie le temps écoulé."""
    global _timers
    if nom not in _timers:
        print(f"{ERROR}Erreur : Chrono '{nom}' non démarré.{RESET}")
        return None

    fin = time.process_time() if not entrees else time.perf_counter()
    duree = fin - _timers[nom]
    # print(f"[{nom}] {duree:.6f} s")
    return duree


def human_time(seconds: float) -> str:
    """Convertit un temps en secondes vers un format lisible."""
    if seconds is None or seconds <= 0:
        return "0s"

    if seconds < 1:
        return f"{seconds * 1000:.2f} ms"

    units = [
        ("d", 86400),
        ("h", 3600),
        ("m", 60),
        ("s", 1),
    ]

    parts = []
    total_seconds = int(seconds)

    for unit, unit_seconds in units:
        if total_seconds >= unit_seconds:
            value = total_seconds // unit_seconds
            total_seconds %= unit_seconds
            parts.append(f"{value}{unit}")

    return " ".join(parts)


def valid_input(type="int", phrase="", info=False):
    """Demande une entrée d'un type précis et boucle tant que l'entrée est invalide."""
    if type == "str":
        phrase = phrase or "enter a string"
        return input(f"{SOULIGN2}{phrase}:{RESET}    ").strip()

    elif type in ["int", "float"]:
        phrase = phrase or "enter a number"
        while True:
            if info:
                entree = input(f"{phrase}").strip().rstrip(")")
            else:
                entree = input(f"{SOULIGN2}{phrase}:{RESET}    ").strip()
            try:
                return int(entree) if type == "int" else float(entree)
            except ValueError:
                print(f"{ERROR}Incorrect enter, try again{RESET}")
                time.sleep(0.5)
                clear_lines(2)

    elif type == "bool":
        phrase = phrase or "enter True/Yes or False/No"
        if info:
            entree = input(f"{phrase}").strip().rstrip(")").lower()
        else:
            entree = input(f"{SOULIGN2}{phrase}:{RESET}    ").strip().lower()
        return entree in continuer

    print(f"{ERROR}INCORRECT TYPE!!!{RESET}")
    return None


# -------------------------------------------------------------------------------

# --- Journalisation (Logging) ---


def ecrire_log(
    message,
    type_log="INFO",
    chemin_fichier=r"C:\Users\elric\Desktop\vs code\all that\données.md",
):
    """Graver message avec date et étiquette [INFO/WARNING/ERROR]"""
    type_log = type_log.upper()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne_log = f"[{date_str}] [{type_log}] {message}\n"

    if (
        chemin_fichier in ["données", "donnée", "donnee", "donnees"]
        or chemin_fichier == r"C:\Users\elric\Desktop\vs code\all that\données.md"
    ):
        chemin_fichier = r"C:\Users\elric\Desktop\vs code\all that\données.md"
    elif chemin_fichier in ["temp", "tempo", "diary", "temporaire"]:
        chemin_fichier = r"C:\Users\elric\Desktop\vs code\all that\tempo diary.md"

    elif "\\" not in chemin_fichier and not chemin_fichier.endswith(".md"):
        print(f"{ERROR}Fichier name not valid : {chemin_fichier}{RESET}")
        return

    with open(chemin_fichier, "a", encoding="utf-8") as f:
        f.write(ligne_log)


def log_info(message, fichier=r"C:\Users\elric\Desktop\vs code\all that\données.md"):
    ecrire_log(message, "INFO", fichier)


def log_warning(message, fichier=r"C:\Users\elric\Desktop\vs code\all that\données.md"):
    ecrire_log(message, "WARNING", fichier)


def log_error(message, fichier=r"C:\Users\elric\Desktop\vs code\all that\données.md"):
    ecrire_log(message, "ERROR", fichier)


# -------------------------------------------------------------------------------

# --- Automatisation ---


def afk_mouse(n=0, kill=False):
    """move mouse randomly and click, forever or in range n (len or digit)"""
    pag.FAILSAFE = False

    def main():
        x = random.randint(0, 1920)
        y = random.randint(0, 1200)
        pag.moveTo(x, y, 0.5)
        time.sleep(0.5)
        pag.click()

    def kill_terminal():
        x, y = 1745, 666
        pag.moveTo(x, y, 0.5)
        time.sleep(0.5)
        pag.click()

    if not kill:
        if not n:
            while True:
                main()
        else:
            try:
                n = int(n)
            except:  # noqa: E722
                n = len(n)
            finally:
                for _ in range(n):
                    main()
    else:
        kill_terminal()


# -------------------------------------------------------------------------------

# --- Crypto ---


def cesar_code():
    """Encrypt a text with Cesar! Multiple options into"""
    letzte, sequ_of_possibl, alpha = "", {}, string.ascii_lowercase

    def math(txt, n, decrypt=True):
        nonlocal alpha
        text = ""
        for i in txt:
            if i in alpha:
                a = alpha.find(i)
                if decrypt:
                    a = (a - n) % len(alpha)
                else:
                    a = (a + n) % len(alpha)
                text += alpha[a]
            elif i.isascii() and i.lower() != i:
                i_lower = i.lower()
                a = alpha.find(i_lower)
                if decrypt:
                    a = (a - n) % len(alpha)
                else:
                    a = (a + n) % len(alpha)
                text += alpha[a].upper()
            elif i.isdigit():
                if decrypt:
                    a = (int(i) - n) % 10
                else:
                    a = (int(i) + n) % 10
                text += str(a)
            elif i == " ":
                text += " "
            else:
                text += i
        return text

    def encrypt():
        nonlocal letzte, alpha
        txt = input("enter a text to encrypt:  \n")
        n = int(
            input(
                "enter a key of encryption *NOTE! This is using the Ceaser cipher (or 0 to make it random)\n"
            )
        )
        if n == 0:
            n = random.randint(1, len(alpha) - 1)
        if txt == "":
            txt = "".join(random.choices(alpha, k=50))
        elif "last" in txt:
            txt = letzte
        apr = math(txt, n, decrypt=False)
        letzte = apr
        print(f"here the text : {txt} in Cesar with key of {n}:\n {apr}")

    def decrypt(txt):
        nonlocal letzte
        n = int(input("enter a key of decryption \n"))
        if "last" in txt:
            txt = letzte
        apr = math(txt, n, decrypt=True)
        letzte = apr
        print(f"the text :  {txt} decrypted in key {n} is : \n {apr}")

    def decrypt_without_key(txt, sign="elric"):
        nonlocal letzte, sequ_of_possibl
        if "last" in txt:
            txt = letzte
        for n in range(1, len(alpha) + 1):
            apr = math(txt, n, decrypt=True)
            if sign in apr:
                sequ_of_possibl[n] = apr
                letzte = apr
                break
        for cle, valeur in sequ_of_possibl.items():
            print(f"possible key :  {cle}")
            print(f"text would pass from {txt} to : {valeur}")

    while True:
        choice = menu_options(
            [
                "1. encrypt a text",
                "2. decrypt a text",
                "3. decrypt without key",
                "4. Exit",
            ]
        )
        match choice:
            case "1. encrypt a text":
                encrypt()
            case "2. decrypt a text":
                text = input("enter a text to decrypt: \n")
                decrypt(text)
            case "3. decrypt without key":
                text = input("enter a text to decrypt: \n")
                kff = input("enter the sign that you know is in this text:  \n")
                while kff == " ":
                    print("not valid sign !!")
                    kff = input(
                        "pls, enter the sign that you know is in this text:  \n"
                    )
                if kff != "":
                    decrypt_without_key(text, kff)
                else:
                    decrypt_without_key(text)
            case "4. Exit":
                cprint("thank you!", FOND_VERT)
                break
        input(">>>   ")
    input("")


def brute_force(password=""):
    """brutforce un pwrd"""

    def brute(target_password, max_length=6):
        # Les caractères possibles : lettres minuscules, majuscules et chiffres
        characters, attempts = (
            string.ascii_lowercase + string.ascii_uppercase + string.digits,
            0,
        )
        start_timer()

        for length in range(
            1, max_length + 1
        ):  # On teste toutes les longueurs de 1 jusqu'à max_length
            print(f"\nTest des combinaisons de longueur {length}...")

            for combo in itertools.product(characters, repeat=length):
                attempts += (
                    1  # itertools.product génère toutes les combinaisons possibles
                )
                guess = "".join(combo)

                if guess == target_password:
                    print(f"\nMot de passe trouvé : '{guess}'")
                    print(f"   Tentatives : {attempts:,}")
                    print(f"   Temps écoulé : {print(f'{stop_timer():.2f}')} secondes")
                    return guess
        print("Mot de passe non trouvé dans la limite fixée.")
        return None

    if not password:
        password = input("Entre un mot de passe court à deviner : ")

    brute(password, max_length=len(password))
    input("")


def morse(txt=""):
    """convert iterable to morse code"""
    if not txt:
        txt = input("enter a sequence to put in morse:\n>>>   ")
    words, morse = tuple(txt), ""
    char_to_dots = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": " ",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }

    def in_morse():
        nonlocal morse
        for abc in words:
            if abc.isalpha():
                abc = abc.upper()
                morse += char_to_dots[abc] + " "
            else:
                morse += char_to_dots[abc] + " "

    in_morse()
    print(f"text in morse :\n{morse}")
    input("")
    return morse


def fibonacci():
    """Remake the fibonacci sequ and few data selections options"""

    def fibonacci_place(n):
        if n <= 0:
            return f"{ROUGE}the number must be greater than 0{RESET}"
        fib1, fib2, count = 1, 1, 2
        if n == 1:
            return f"the number is at the {VERT}1st or 2nd place{RESET}"
        while fib2 < n:
            fib1, fib2, count = fib2, fib1 + fib2, count + 1
        if fib2 == n:
            return f"the number is at the {VERT}{count}th place{RESET}"
        else:
            return f"{ROUGE}the number isn't in the Fibonacci sequence{RESET}"

    def fibonnacci_index_num(n):
        if n <= 0:
            return None
        fib1, fib2 = 1, 1
        if n == 1 or n == 2:
            return 1
        for _ in range(3, n + 1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2

    while True:
        choice = menu_options(
            [
                "1. Find number in place n in the Fibonacci sequence",
                "2. Find if n is the sequence",
                "3. Quit",
            ]
        )
        if choice == "1. Find number in place n in the Fibonacci sequence":
            try:
                n = int(input("Enter a index of the Fibonacci sequence :\nPlace: "))
                result = fibonnacci_index_num(n)
                if result is None:
                    cprint("the index must be greater than 0!", ERROR)
                else:
                    print(
                        f"To the place {n} of the Fibonacci sequence there is the #"
                        f"{VERT}{format_number(result)}{RESET}"
                    )
            except ValueError:
                cprint("please enter a valid integer", ERROR)
            input("")
            clear()
        elif choice == "2. Find if n is the sequence":
            try:
                n = int(
                    input(
                        "Enter a number to check if he's in the sequence and at wich place:\nNumber to check:  "
                    )
                )
                print(fibonacci_place(n))
            except ValueError:
                cprint("please enter a valid integer", ERROR)
            input("")
            clear()
        elif choice == "3. Quit":
            return


def A1Z26(direct: str = False):
    """Here the mythical encodage in A1_Z26 to in and out code."""

    def in_A1Z26(*args):
        alphab, char = string.ascii_lowercase, ""
        for word in list(*args):
            for letter in word:
                letter = letter.lower()
                if letter not in alphab:
                    if not letter == word[-1]:
                        char += letter + "-"
                    else:
                        char += letter
                    continue
                ind = alphab.index(letter) + 1
                if not letter == word[-1]:
                    char += str(ind) + "-"
                else:
                    char += str(ind)
            char += "  "
        return char

    def out_A1Z26(*args):
        alphab = string.ascii_lowercase
        result_words = []
        for word in list(*args):
            tokens = word.split("-") if word else []
            decoded = ""
            for token in tokens:
                token = token.strip()
                if not token:
                    continue
                if token.isdigit():
                    n = int(token)
                    if 1 <= n <= 26:
                        decoded += alphab[n - 1]
                    else:
                        decoded += token
                else:
                    decoded += token
            result_words.append(decoded)
        return " ".join(result_words)

    if direct and direct == "in_A1Z26()":
        text = input("\nEnter the text to encode:  ").strip().split()
        return in_A1Z26(text)
    elif direct and direct == "out_A1Z26()":
        text = input("\nEnter the text to decode:  ").strip().split("  ")
        return out_A1Z26(text)

    choix = menu_options(["1. Encode to A1-Z26", "2. Decode from A1-Z26", "3. Exit"])
    match choix:
        case "1. Encode to A1-Z26":
            text = input("\nEnter the text to encode:  ").strip().split()
            return in_A1Z26(text)

        case "2. Decode from A1-Z26":
            text = input("\nEnter the text to decode:  ").strip().split("  ")
            return out_A1Z26(text)

        case "3. Exit":
            return


# -------------------------------------------------------------------------------

# --- Jeux ---


def pendu_game(mode="normal"):
    """launch mytique pendu_game. Multiple mode"""
    global mots_921
    mots = mots_921.copy()
    mots, letter, letters, count_pendu, false_answers, count_down = (
        list(filter(lambda x: True if len(x) > 5 else False, mots_921)),
        "",
        [],
        0,
        [],
        6,
    )
    word = random.choice(mots)
    word = enlever_accents(word).lower()
    pendu_etapes = (
        " +---+\n     \n     \n     \n     ",
        " +---+\n |   \n     \n     \n     ",
        " +---+\n |   \n O   \n     \n     ",
        " +---+\n |   \n O   \n/|   \n     ",
        " +---+\n |   \n O   \n/|\\  \n     ",
        " +---+\n |   \n O   \n/|\\  \n/    ",
        " +---+\n |   \n O   \n/|\\  \n/ \\  ",
    )

    def start():
        global mots_921
        mots_921 = list(filter(lambda x: True if len(x) > 5 else False, mots_921))
        nonlocal mots, count_down, letter, letters, count_pendu, false_answers, pendu_etapes, word
        mots = mots_921.copy()
        letter, letters, count_pendu, false_answers, count_down = (
            "",
            [],
            0,
            [],
            6,
        )
        if not mots:
            raise ValueError(
                "La liste des mots du pendu est vide. Vérifiez que mots_francais.py ou mots_francais.json est présent."
            )
        word = random.choice(mots)
        word = enlever_accents(word).lower()
        pendu_etapes = (
            " +---+\n     \n     \n     \n     ",
            " +---+\n |   \n     \n     \n     ",
            " +---+\n |   \n O   \n     \n     ",
            " +---+\n |   \n O   \n/|   \n     ",
            " +---+\n |   \n O   \n/|\\  \n     ",
            " +---+\n |   \n O   \n/|\\  \n/    ",
            " +---+\n |   \n O   \n/|\\  \n/ \\  ",
        )

    def show_word(mode="normal"):
        nonlocal count_down, word, letters
        if not letters and mode == "normal":
            print("_" * len(word))
            return
        elif not letters and mode == "facile":
            letters.append(word[0])
        elif not letters and mode == "tr_facile":
            letters.append(word[0])
            letters.append(word[-1])
        elif not letters and mode == "difficile":
            count_down = 4
        elif mode == "debug":
            print(f"word is {VERT_FLASH + SOULIGN2}{word}{RESET}")
        print("".join(i if i in letters else "_" for i in word))
        print()

    def enter_letter():
        nonlocal letter, false_answers, word, count_pendu
        while True:
            remaining_attempts = max(0, count_down - len(false_answers))
            cprint(f"Attempts left: {remaining_attempts}", WARNING)
            if false_answers:
                print(
                    f"{ROUGE_FLASH}False guesses:   {', '.join(false_answers)}{RESET}"
                )
            letter = input("enter a letter or a full word:    ").strip().lower()
            normalized_input = enlever_accents(letter)

            if normalized_input in ["exit", "quit", "ex"]:
                clear()
                sys.exit()
            elif normalized_input == "re":
                clear()
                run()
            elif normalized_input == word:
                verif_game(True)
                return
            if len(normalized_input) != 1 or not normalized_input.isalpha():
                cprint("JUST ONE LETTER OR A FULL WORD!", ERROR)
                time.sleep(0.5)
                if false_answers:
                    clear_lines(3)
                else:
                    clear_lines(2)
                continue

            clear_lines(1)
            if normalized_input in letters or normalized_input in false_answers:
                cprint("Answer already gave!", WARNING)
                time.sleep(1)
                clear()
                return
            if normalized_input in word:
                print(
                    f"enter a letter or a full word:    {VERT_FLASH}{GRAS}{normalized_input}{RESET}"
                )
                print(f"{normalized_input} {SUCCESS}is in the word!{RESET}")
                letters.append(normalized_input)
            else:
                print(
                    f"enter a letter or a full word:    {ROUGE_FLASH}{GRAS}{normalized_input}{RESET}"
                )
                print(f"{normalized_input} {ERROR}not in the word!{RESET}")
                count_pendu += 1
                false_answers.append(normalized_input)
            time.sleep(1)
            return

    def show_pendu(level: int = 0) -> None:
        print()
        for line in pendu_etapes[level].split("\n"):
            print(line)
        match level:
            case 0:
                clear_lines(3)
            case 1:
                clear_lines(2)
            case 2 | 3:
                clear_lines(1)
        print()

    def verif_game(full_word=False):
        if not full_word:
            if len(false_answers) >= count_down:
                print(f"Answer was {FOND_VERT}{word}{RESET}")
                cprint(
                    f"You gave {len(false_answers)} bad answers!",
                    ROUGE_FLASH + SOULIGN2,
                )
                cprint(f"You had {len(letters)} good answers!", SUCCESS)
                cprint("But...", ROUGE_FLASH)
                cprint("You lost!", ERROR)
                end()
            elif len(letters) == len(set(word)):
                print(f"Answer was {FOND_VERT}{word}{RESET}")
                cprint("You found all the letters!", VERT_FLASH + SOULIGN2)
                cprint("And...", VERT)
                cprint("You won", SUCCESS)
                end()
            return
        cprint(f"You guessed the word!, it was good {word}", SUCCESS)
        print(
            f"{VERT}You gave {len(letters)} good answers {ROUGE}and {len(false_answers)} bad answers!{RESET}"
        )
        cprint("You won!", SUCCESS)
        end()

    def end():
        choice = input("New round? (y/n)\n").strip().lower()
        if choice in ["y", "yes", "o", "oui", "1"]:
            run()
        else:
            return

    def main(mode="normal"):
        while True:
            nonlocal count_pendu
            clear()
            show_pendu(count_pendu)
            verif_game()
            show_word(mode)
            enter_letter()

    def run(mode="normal"):
        faire_titre_section("Pendu Game")
        start()
        main(mode)

    run(mode)


def paper_scissor_game():
    """Execut legendary paper_scissor-game with cheat capa"""
    faire_titre_section("Rock, Paper, Scissor Game")

    choices, won, lose = ("rock", "paper", "scissor"), 0, 0

    while True:
        computer = random.choice(choices)
        player = input("Enter your choice (q to quit): ")
        if player.lower() == "q":
            break
        cheat = player != player.lower()

        if not player:
            player = random.choice(choices)
            print(f"Player chose {player.upper()}")
        else:
            player = player.lower()

        if player not in choices:
            cprint("You chose an invalid option", ERROR)
            time.sleep(0.7)
            clear_lines(2)
            continue

        if cheat:
            if player == "rock":
                computer = "scissor"
            elif player == "paper":
                computer = "rock"
            elif player == "scissor":
                computer = "paper"

        print(f"the computer chose: {computer}")

        if player == computer:
            print("It's a tie")
        elif player == "rock" and computer == "paper":
            cprint("You lost!", ERROR)
            lose += 1
        elif player == "paper" and computer == "scissor":
            cprint("You lost!", ERROR)
            lose += 1
        elif player == "scissor" and computer == "rock":
            cprint("You lost!", ERROR)
            lose += 1
        else:
            cprint("You won!", SUCCESS)
            won += 1

    print(f"{SUCCESS}you won {won} times,{RESET} {ERROR}and lost {lose} times{RESET}")
    print(
        f"{SUCCESS}Good game!{RESET}"
        if won > lose
        else f"{ERROR}You will do it better next time!{RESET}"
    )
    input("Press enter to exit\n>>>    ")


def number_guess_game(minimum=0, maximum=100):
    """start number_guess_game, with a cheat capa!"""
    faire_titre_section("Number Guessing Game!")
    (
        number_rand,
        guesses,
        my_number,
        choix,
    ) = (
        int(random.randint(minimum, maximum)),
        0,
        None,
        (1, 3),
    )

    # print(f'Num is {number_rand}')
    def enter_num():
        nonlocal my_number, guesses
        while True:
            user_input = input(
                f"Please enter a number between {minimum} and {maximum}: "
            )
            if user_input.lower() in exit:
                cprint("Exiting the game.", WARNING)
                sys.exit()
            elif user_input.lower() == "re":
                cprint("Restarting the game.", WARNING)
                number_guess_game(minimum, maximum)
            elif user_input.strip() != user_input:
                high_low(cheat=True)
            try:
                my_number = int(user_input.strip())
            except ValueError:
                cprint("Invalid input. Please enter a valid number.", ERROR)
                time.sleep(0.5)
                clear_lines(2)
                continue

            if minimum <= my_number <= maximum:
                guesses += 1
                break

    def high_low(cheat=False):
        nonlocal number_rand, my_number, guesses
        if cheat:
            for _ in range(2):
                a = random.choice(choix)
                if a == 1:
                    print(f"{my_number} is too LOW! Try again!")
                    enter_num()

                else:
                    print(f"{my_number} is too HIGH! Try again!")
                    enter_num()
            end()
        if int(my_number) > number_rand:
            print(f"{my_number} is too High! Try again!")
        else:
            print(f"{my_number} is too Low! Try again!")

    def end():
        cprint("Congratulations! You guessed the number!", SUCCESS)
        cprint(f"You guessed {guesses} times!", WARNING)
        input("")
        sys.exit()

    while True:
        enter_num()
        if my_number == number_rand:
            end()
        high_low()


def code_names_game():
    """reprodution of code_names"""
    faire_titre_section(code_names_game)

    def afficher_grille(grille, mode="joueur"):
        """Affiche la grille selon le mode : 'joueur' (brut) ou 'maitre' (avec filtres)"""
        for e in range(5):
            for i in range(5):
                mot = grille[e][i]
                if mode == "maitre":
                    if mot in accepted_prop:
                        print(f"{NOIR_INVISIBLE}{mot:<15}{RESET}", end="")
                    elif mot in mots_rouges:
                        print(f"{ROUGE}{mot:<15}{RESET}", end="")
                    elif mot in mots_verts:
                        print(f"{VERT}{mot:<15}{RESET}", end="")
                    else:
                        print(f"{mot:<15}", end="")

                else:
                    if mot in accepted_prop:
                        print(f"{NOIR_INVISIBLE}{mot:<15}{RESET}", end="")
                    else:
                        print(f"{mot:<15}", end="")
            print("")

    def repetition_aceptation_rep(props):
        """augmente le nb de rep gave (de 1) et ajoute la proposition a une liste pour ensuite les masquer (next turn)"""
        nonlocal nb_rep_gave, accepted_prop
        nb_rep_gave += 1
        accepted_prop.append(props)

    mots = random.choices(mots_921, k=25)
    while len(set(mots)) != len(mots):
        mots = random.choices(mots_921, k=25)
    accepted_prop, rouge, vert, pts, mots2, nb_rep_gave = (
        [],
        (range(3)),
        (range(5)),
        0,
        mots.copy(),
        0,
    )
    random.shuffle(mots)
    random.shuffle(mots2)
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
        clear()
        afficher_grille(matrice, mode="maitre")

        key_word = (
            input("Enter a word for the person can devine:\n>>>   ").strip().lower()
        )
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
                    print(f"{ROUGE}Incorrect enter{RESET}")
                    reponses.remove(i)
                    continueeee = 1
            if continueeee == 1:
                continue
            if "q" in reponses:
                reponses.pop()
                break
            for i in reponses:
                if i not in mots:
                    print(f"{ROUGE}Incorrect enter{RESET}")
                    print(
                        f"{ROUGE}{GRAS}IMPORTANT : Les answers entered have been deleted bc you made a mistake!{RESET}"
                    )
                    reponses = []
                    continueeee = 1
            if continueeee == 1:
                continue
            print("Element succesfuly added to the answers, what's the next ?")

        clear()
        nb_rep = 0
        print("The answers are: ", end="")
        for i in reponses:
            nb_rep += 1
            print(i, end="   ")
        print("")
        print(f"There are {nb_rep} rep at total")
        input("")
        clear()

        propositions, nb_rep_gave, nb_good_answ, pts_before = "", 0, 0, pts

        while True:
            clear()
            print(
                f"The player selected {nb_rep} words to find, the keyword is: {key_word}\n {VERT}GOOD LUKE{RESET}"
            )
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
                print(f"{ROUGE}Propostion invalid{RESET}")
                print("The proposition isn't in the table, pls select an other one")
                input("")
                continue
            if propositions in mots_rouges:
                cprint(f"You lost!", ROUGE)
                cprint(f"the answers were : {reponses}", VERT + SOULIGN2)
                sys.exit(f"See you next time, you had {pts}pts")
            if propositions in mots_verts and propositions in reponses:
                pts += 1
                cprint(f"You won 1pts, you are now to {pts}pts!", VERT)
                repetition_aceptation_rep(propositions)
                nb_good_answ += 1
            elif propositions in reponses:
                cprint(
                    f"{VERT}Very well answer but you didn't make points{RESET}", VERT
                )
                cprint(f"You have {pts}!", VERT)
                repetition_aceptation_rep(propositions)
                nb_good_answ += 1
            else:
                print(f"{ROSE} Not good Answer,{RESET} keep schearching")
                repetition_aceptation_rep(propositions)
            input("")

        clear()
        print(
            f"The player selected the {nb_rep} reponses\n He found {nb_good_answ} good answers, and made {pts - pts_before}pts!"
        )
        input("Next round ?\n")

    cprint("You won!", VERT + SOULIGN2 + GRAS + ITALIC)
    print(f"You had {pts}pts !")


def pile_face_game(load=True):
    """just pile/face game! great animation and cheat capa->J"""
    faire_titre_section("Pile ou Face Game")
    choix = ("pile", "face")
    while True:
        reponse = input(">>>   ")
        if reponse.lower() in exit:
            break
        elif reponse.strip() != reponse:
            if load:
                loading_bar(1)
            slow_type("And it's...", 1, color=LOG_DISCRET)
            cprint(" FACE", LOG_DISCRET)
        else:
            if load:
                loading_bar(1)
            slow_type("And it's...", 1, color=LOG_DISCRET)
            choi = random.choice(choix)
            cprint(f" {choi}", LOG_DISCRET)


def word_guess_game(mode="nul", lenght_word_min=6, max_guesses=10):
    """the word_guess_game were you input word and make color on letter -> /help"""
    global mots_921
    mots_921 = list(
        filter(lambda x: True if len(x) >= lenght_word_min else False, mots_921)
    )
    word = random.choice(mots_921)
    word = enlever_accents(word)
    (
        letters,
        propositions_color,
        good_answ,
        esp,
        total_props,
        guesses,
        alphabet,
        letters_red,
        letters_yellow,
        letters_green,
    ) = (
        list(set(list(word))),
        [],
        0,
        "    " if len(word) <= 9 else "   ",
        [],
        0,
        string.ascii_lowercase,
        [],
        [],
        [],
    )

    def affichage():
        clear()
        faire_titre_section("Word Guessing Game!")
        print("")
        for i in alphabet:
            if i in letters_green:
                print(f"{SUCCESS}{i}{RESET}", end=" ")
            elif i in letters_yellow:
                print(f"{WARNING}{i}{RESET}", end=" ")
            elif i in letters_red:
                print(f"{ERROR}{i}{RESET}", end=" ")
            else:
                print(i, end=" ")
        print("\n")
        if mode == "debug":
            print(f" " * 28 + {word})
        for prop in total_props:
            print(f"{esp}{prop}", end="\n")
        if max_guesses - guesses <= 3:
            print("\n")
            if max_guesses - guesses != 1:
                cprint(f"Just {max_guesses - guesses} guesses left!", WARNING)
            else:
                cprint("Just 1 attempt left!!", WARNING)
                cprint("Be really carefull!", WARNING)
        print(f" " * 28 + "_" * len(word))

    def test_word():
        nonlocal good_answ, propositions_color, guesses, enter, guesses
        guesses += 1
        enter, propositions_color, good_answ = str(enter), [], 0
        for i in range(len(word)):
            if enter[i] == word[i]:
                propositions_color.append(f"{SUCCESS}{enter[i]}{RESET}")
                if not enter[i] in letters_green:
                    letters_green.append(enter[i])
                    if enter[i] in letters_yellow:
                        letters_yellow.remove(enter[i])
                good_answ += 1
            elif enter[i] in letters:
                propositions_color.append(f"{WARNING}{enter[i]}{RESET}")
                if not enter[i] in letters_yellow and enter[i] not in letters_green:
                    letters_yellow.append(enter[i])
            else:
                propositions_color.append(f"{ERROR}{enter[i]}{RESET}")
                if not enter[i] in letters_red:
                    letters_red.append(enter[i])
        total_props.append(" ".join(propositions_color))

    while not good_answ == len(word) and not guesses >= 10:
        while True:
            affichage()
            enter = (
                input(f"Enter word of {WARNING}{len(word)} letters:{esp}{RESET}")
                .lower()
                .strip()
            )
            if enter.lower() in exit:
                cprint("Exiting the game.", WARNING)
                return
            elif enter.lower() == "re":
                cprint("Restarting the game.", WARNING)
                time.sleep(0.3)
                word_guess_game()
            elif enter == "1":
                cprint(f"The word was: {SURLIGN2_BLANC}{word}", ERROR)
                return
            elif enter in ["-help", "/help"]:
                cprint("Type '1' to reveal the word and exit.", WARNING)
                cprint("Type 're' to restart the game.", WARNING)
                cprint("Type 'help' to receive help with the word", WARNING)
                time.sleep(2)
                clear_lines(4)
                continue
            elif not enter.isalpha():
                cprint("Word must only contain letters!", ERROR)
                time.sleep(0.5)
                clear_lines(2)
                continue
            elif enter == "help":
                enter = "".join(
                    list(random.choices(string.ascii_lowercase, k=len(word)))
                )
                clear_lines()
                print(
                    f"Enter word of {WARNING}{len(word)} letters:{esp}{RESET}", end=""
                )
                slow_type(enter, 1, color=LOG_DISCRET)
                time.sleep(0.5)
            elif len(enter) != len(word):
                cprint(f"Word must be {len(word)} letters long!", ERROR)
                time.sleep(0.5)
                clear_lines(2)
                continue
            clear_lines(2)
            break
        test_word()
        if good_answ >= len(word):
            affichage()
            clear_lines(2)
            print(f"{SUCCESS}{esp}{' '.join(list(word))}{RESET}", end="\n")
            cprint(f"Congratulations! You found the word: {word}", SUCCESS)
            choice = input("New game?:  ")
            if choice in continuer:
                word_guess_game()
            return
        elif guesses >= max_guesses:
            affichage()
            clear_lines()
            cprint(f"Sorry but you lost!\n{VERT_FLASH}The word was {word}", ERROR)
            choice = input("New game?:  ")
            if choice in continuer:
                word_guess_game()
            return


def dice(n_faces=6, n=1):
    """simule n lances de dés à n_faces faces"""
    simulation, total = 0, 0
    for i in range(n):
        simulation = random.randint(1, n_faces)
        slow_type(f"{i+1} -> {simulation}\n", 0.20)
        total += simulation
    print("\n")
    slow_type(f"total = {total}", 0.05)
    input("")
    return total


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

            if cases_libres and len(cases_libres) < 7:
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

        slow_type("Bienvenue dans le jeu TicTacToe!\n", color=WARNING, tps_total=1)
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


def menu_game():
    """the game jeux!!"""
    while True:
        faire_titre_section("Games Menu")
        choice = menu_options(
            [
                "1. Pendu Game",
                "2. Rock, Paper, Scissor Game",
                "3. Number Guessing Game",
                "4. Code Names Game",
                "5. Pile ou Face Game",
                "6. Word guessing Game",
                "7. Dice simulator Game",
                "8. Tic Tac Toe Game",
                "9. Exit",
            ]
        )
        match choice:
            case "1. Pendu Game":
                mode = menu_options(
                    [
                        "1. Normal",
                        "2. Facile",
                        "3. Très Facile",
                        "4. Difficile",
                        "5. Debug",
                        "6. Exit",
                    ]
                )
                match mode:
                    case "1. Normal":
                        pendu_game("normal")
                    case "2. Facile":
                        pendu_game("facile")
                    case "3. Très Facile":
                        pendu_game("tr_facile")
                    case "4. Difficile":
                        pendu_game("difficile")
                    case "5. Debug":
                        pendu_game("debug")
                    case "6. Exit":
                        break
            case "2. Rock, Paper, Scissor Game":
                paper_scissor_game()
            case "3. Number Guessing Game":
                number_guess_game()
            case "4. Code Names Game":
                code_names_game()
            case "5. Pile ou Face Game":
                pile_face_game()
            case "6. Word guessing Game":
                word_guess_game()
            case "7. Dice simulator Game":
                face, dices = input("How many face (6 by def):    "), input(
                    "How many dice? (1 by def):    "
                )
                face, dices = int(face) if face else 6, int(dices) if dices else 1
                dice(face, dices)
            case "8. Tic Tac Toe Game":
                tictactoe_game()
            case "9. Exit":
                return


# -------------------------------------------------------------------------------

# --- Outils du projet ---


def trouver_nom(objet):
    """return name of the given variable"""
    for nom, valeur in globals().items():
        if valeur is objet:
            return nom
    return None


# pas a jour du tout avec la new versions de mots_921 !!
def fonct_mots():
    """fonct for the var mots_921 which search if given name is into"""
    global mots_921
    nom = trouver_nom(mots_921)
    print(f"{nom} = {len(mots_921)}")
    if nom != "mots_" + str(len(mots_921)):
        print(f"{ERROR}Problem with the name of {nom}{RESET}")
    word = "science"
    while True:
        word = input("Enter a word:    ").lower()
        if word == "clear":
            clear()
            fonct_mots()
        elif word == "quit":
            sys.exit()
        if word in mots_921:
            print(f"{ERROR}{word} is present!{RESET}")
            continue
        else:
            print(f"{SUCCESS}{word} isn't present!{RESET}")
            accept_enter = input(f"do you want the word :  {word}, to be add?\n>>>  ")
            if accept_enter == "clear":
                clear()
                fonct_mots()
            elif accept_enter.lower() == "quit":
                sys.exit()
            if accept_enter:
                mots_921.append(word)
                mots_921 = sorted(mots_921)
                index_debut = mots_921.index(word) - 1
                index_fin = mots_921.index(word) + 2
                print(mots_921[index_debut:index_fin])
                a = str(mots_921[index_debut:index_fin])
                a = a.lstrip("[")
                a = a.rstrip("]")
                copier_txt(a)
                print(f"ligne: {65 +  index_debut // 10}")


def kanekicount(number, base):
    n = 0
    while number > base:
        number, n = number - base, n + 1
        print(f"{number}    {n}")


def match_color(color):
    match color:
        case "BARR2":
            color = BARR2
        case "SURLIGN2_BLANC":
            color = SURLIGN2_BLANC
        case "GRAS":
            color = GRAS
        case "ITALIC":
            color = ITALIC
        case "SOULIGN2":
            color = SOULIGN2
        case "NOIR_INVISIBLE":
            color = NOIR_INVISIBLE
        case "RESET":
            color = RESET
        case "CYAN":
            color = CYAN
        case "ROSE":
            color = ROSE
        case "BLEU":
            color = BLEU
        case "JAUNE":
            color = JAUNE
        case "VERT":
            color = VERT
        case "GRIS":
            color = GRIS
        case "ROUGE":
            color = ROUGE
        case "CYAN_FLASH":
            color = CYAN_FLASH
        case "ROSE_FLASH":
            color = ROSE_FLASH
        case "BLEU_FLASH":
            color = BLEU_FLASH
        case "JAUNE_FLASH":
            color = JAUNE_FLASH
        case "VERT_FLASH":
            color = VERT_FLASH
        case "ROUGE_FLASH":
            color = ROUGE_FLASH
        case "NOIR_FLASH":
            color = NOIR_FLASH
        case "BLANC_FLASH":
            color = BLANC_FLASH
        case "FOND_GRIS":
            color = FOND_GRIS
        case "FOND_CYAN":
            color = FOND_CYAN
        case "FOND_ROSE":
            color = FOND_ROSE
        case "FOND_BLEU":
            color = FOND_BLEU
        case "FOND_JAUNE":
            color = FOND_JAUNE
        case "FOND_VERT":
            color = FOND_VERT
        case "FOND_ROUGE":
            color = FOND_ROUGE
        case "FOND_NOIR":
            color = FOND_NOIR
        case "ALERTE_CRITIQUE":
            color = ALERTE_CRITIQUE
        case "LOG_DISCRET":
            color = LOG_DISCRET
        case "MENU_ACTIF":
            color = MENU_ACTIF
        case "STYLE_TITRE":
            color = STYLE_TITRE
        case "SUCCESS":
            color = SUCCESS
        case "WARNING":
            color = WARNING
        case "ERROR":
            color = ERROR
    return color


# -------------------------------------------------------------------------------

# --- Executables ---


loading_bar(0.4, symbol="*", lenght=10, exe=True)
start_timer()
