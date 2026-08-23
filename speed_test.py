from tools import *
from mots_francais import mots
import time, random

while True:
    TEXTE = list(random.choices(mots, k=6))
    errors_nb = float(0)
    clear()
    print('╔══════════════════════════╗')
    print('║   Typing speed test !    ║')
    print('╚══════════════════════════╝')

    print('\nYou have to rewrite the words there :')
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

    pourc = 100 - (100 * errors_nb) / len(TEXTE)
    temps_mots_min = (len(TEXTE) * 60) / tps
    print(f'pourc -> {pourc}% and  tps_mts_min -> {temps_mots_min}  erros -> {errors_nb}')
    input('')
