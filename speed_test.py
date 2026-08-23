from tools import *
from mots_francais import mots
import time, random

def typing_speed_game():
    while True:
        TEXTE = list(random.choices(mots, k=6))
        errors_nb = float(0)
        clear()
        cprint('   ╔══════════════════════════╗', VERT)
        cprint('   ║   Typing speed test !    ║', VERT)
        cprint('   ╚══════════════════════════╝', VERT)

        cprint('\nYou have to rewrite the words there :', WARNING)
        a = input('\nReady ?:   ')
        if a in exit:
            break
        clear_lines()
        print(f'{' '.join(TEXTE)}')
        start_timer('typing_user', True)
        typing_user = input('').split()
        tps = stop_timer('typing_user', True)
        if len(typing_user) != len(TEXTE):
            continue
        clear_lines()
        for i in range(len(TEXTE)):
            if TEXTE[i] != typing_user[i]:
                if enlever_accents(TEXTE[i]) == typing_user[i]:
                    errors_nb += 0.5
                    for j in range(len(typing_user[i])):
                        if typing_user[i][j] == TEXTE[i][j]:
                            print(f'{typing_user[i][j]}', end='')
                        else:
                            print(f'{WARNING}{typing_user[i][j]}{RESET}', end='')
                else:
                    errors_nb += 1
                    if len(typing_user[i]) != len(TEXTE[i]):
                        print(f'{ERROR}{typing_user[i]}{RESET}', end='')
                    else:
                        for j in range(len(typing_user[i])):
                            if typing_user[i][j] == TEXTE[i][j]:
                                print(f'{typing_user[i][j]}', end='')
                            else:
                                print(f'{ERROR}{typing_user[i][j]}{RESET}', end='')
            else:
                print(f'{typing_user[i]}', end='')
            print(' ', end='')

        pourc, temps_mots_min = 100 - (100 * errors_nb) / len(TEXTE), (len(TEXTE) * 60) / tps

        print(f'{LOG_DISCRET}\npourc -> {RESET}{VERT_FLASH if pourc >= 85 else WARNING if pourc >= 50 else ERROR}{pourc}%{RESET}\n{LOG_DISCRET}Errors -> {RESET}{VERT_FLASH if errors_nb <= 0.5 else WARNING if errors_nb <= 1.5 else ERROR}{errors_nb}{RESET}\n{LOG_DISCRET}tps_mts_min -> {RESET}{ALERTE_CRITIQUE if temps_mots_min <= 20 else WARNING if temps_mots_min <= 30 else VERT if temps_mots_min <= 45 else SUCCESS}{temps_mots_min}{RESET}')
        if temps_mots_min > config['higest_typing_speed'] and errors_nb <= 1:
            cprint(f'\nThe records was updated from {config['higest_typing_speed']}  to {temps_mots_min:.2f}', SUCCESS)
            config['higest_typing_speed'] = round(temps_mots_min, 2)
            print(save_config(config))
        else:
            cprint(f'\nThe record is {config['higest_typing_speed']}', WARNING)
        input('')
    input('')

