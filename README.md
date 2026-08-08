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

• clear()

• loading_bar(0.4, symbol="*", lenght=10, exe=True)

• start_timer()


--------------------------------------------------------------------------------------------------------------------------------------------------------------

--- Divers ---

•
===============================================================================
