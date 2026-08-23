from tools import *
from mots_francais import mots
import time, random

while True:
    TEXTE = list(random.choices(mots, k=6))
    errors_nb = float(0)
    clear()
    cprint('   ╔══════════════════════════╗', VERT)
    cprint('   ║   Typing speed test !    ║', VERT)
    cprint('   ╚══════════════════════════╝', VERT)

    cprint('\nYou have to rewrite the words there :', WARNING)
    input('\nReady ?:   ')
    clear_lines()
    print(f'{' '.join(TEXTE)}')
    start_timer('typing_user', True)
    typing_user = input('').split()
    tps = stop_timer('typing_user', True)
    if len(typing_user) != len(TEXTE):
        continue
    for i in range(len(TEXTE)):
        if TEXTE[i] != typing_user[i]:
            if enlever_accents(TEXTE[i]) == typing_user[i]:
                errors_nb += 0.5
            else:
                errors_nb += 1

    pourc, temps_mots_min = 100 - (100 * errors_nb) / len(TEXTE), (len(TEXTE) * 60) / tps

    print(f'{LOG_DISCRET}pourc -> {RESET}{VERT_FLASH if pourc >= 85 else WARNING if pourc >= 50 else ERROR}{pourc}%{RESET}\n{LOG_DISCRET}tps_mts_min -> {RESET}{ALERTE_CRITIQUE if temps_mots_min <= 20 else WARNING if temps_mots_min <= 30 else VERT if temps_mots_min <= 45 else SUCCESS}{temps_mots_min}{RESET}\n{LOG_DISCRET}Errors -> {RESET}{VERT_FLASH if errors_nb <= 0.5 else WARNING if errors_nb <= 1.5 else ERROR}{errors_nb}{RESET}')
    input('')
