from tools import *
import random, time, sys
mise, cheat = 0, True
ROULETTE_EUROPEENNE = [
    0,
    32,
    15,
    19,
    4,
    21,
    2,
    25,
    17,
    34,
    6,
    27,
    13,
    36,
    11,
    30,
    8,
    23,
    10,
    5,
    24,
    16,
    33,
    1,
    20,
    14,
    31,
    9,
    22,
    18,
    29,
    7,
    28,
    12,
    35,
    3,
    26,
]
COULEURS_ROULETTE = {
    0: "vert",
    1: "rouge",
    2: "noir",
    3: "rouge",
    4: "noir",
    5: "rouge",
    6: "noir",
    7: "rouge",
    8: "noir",
    9: "rouge",
    10: "noir",
    11: "noir",
    12: "rouge",
    13: "noir",
    14: "rouge",
    15: "noir",
    16: "rouge",
    17: "noir",
    18: "rouge",
    19: "rouge",
    20: "noir",
    21: "rouge",
    22: "noir",
    23: "rouge",
    24: "noir",
    25: "rouge",
    26: "noir",
    27: "rouge",
    28: "noir",
    29: "noir",
    30: "rouge",
    31: "noir",
    32: "rouge",
    33: "noir",
    34: "rouge",
    35: "noir",
    36: "rouge",
}
# while True:
#     mise = input("Enter a mise:   ").strip().lower()
#     if mise in exit:
#         print(f"DEBUG après journal : mise = {mise!r}")
#         input()
#         # return

#     if mise == "capa":
#         clear()
#         print("\n" * 17)
#         print(f"\t{'code':<15}{'utilisation'}\nMISE:")
#         slow_type(
#             f"\t{'n':<15}{'just mise the number n'}\n\t{'all':<15}{'mise all the sold'}\n\t{'all - n':<15}{'mise the all sold - n€'}\n\t{'last':<15}{'mise the last montant mised'}\n\t{'last +/- n':<15}{'last_mise + ou - n€'}\n\t{'half':<15}{'mise half of the sold'}\n\t{'half +/- n':<15}{'half of the sold +/- n€'}\n\t{'r':<15}{'random mise btw 11 and sold'}\n\t{'r n1':<15}{'mise and random amount btw n1 and sold'}\n\t{'r n1 n2':<15}{'mise and random amount btw n1 and n2'}\n",
#             tps_btw_letters=0.008,
#         )
#         print("\nPREDICT:")
#         slow_type(
#             f"\t{'ex, n, no, q':<15}{'revient au choix de la mise'}\n\t{'last':<15}{'re-enter the last_prediction'}\n\t{'ra, al':<15}{'choose random prediction'}\n\t{'ch, not':<15}{'enter the opposite of the last_prediction'}\n\t{'logic, best':<15}{'chose the best option by the stat, if equals -> random'}\n\t{'r, blood, red':<15}{'prediction = ROUGE'}\n\t{'any else':<15}{'prediction = NOIR'}",
#             tps_btw_letters=0.008,
#         )
#         print("\n" * 2)
#         input()
#         clear()
#         continue
#     elif cheat and hach_word(mise) == config["code"]:
#         cheat_use += 1
#         clear_lines()
#         print(arc_en_ciel("secret"))
#         time.sleep(0.5)
#         clear_lines()
#         print("\n" * 2)
#         print(f"\t{'dark code':<15}{'utilisation'}\nMISE:")
#         slow_type(
#             f"\t{A1Z26(txtt='19-15-12-4  +-/-*  14', choix="2. Decode from A1-Z26"):<15}{A1Z26(txtt='1-16-16-12-9-17-21-5  +  15-21  *  14  19-21-18  12-5  19-15-12-4', choix="2. Decode from A1-Z26")}\n\t{A1Z26(txtt='3-1-18-4  ', choix="2. Decode from A1-Z26"):<15}{A1Z26(txtt='1-6-6-9-3-8-5  12-5-19  9-14-6-15-19  4-5  3-1-18-4  1-3-21-20-512-12-5 ', choix="2. Decode from A1-Z26")}\n\t{A1Z26(txtt='3-8-(-1-14-7-5-) ', choix="2. Decode from A1-Z26"):<15}{A1Z26(txtt='18-5-18-15-12-12  12-1  3-1-18-20-5  (-5-14  3-12-5-1-14-1-14-20  12-5  20-15-21-20-)  ', choix="2. Decode from A1-Z26")}\n\t{A1Z26(txtt='9-14-6-/-6-21-12-12  14 ', choix="2. Decode from A1-Z26"):<15}{A1Z26(txtt='16-5-18-13-5-20  4-5  13-9-19-5-18  2-9-5-14  1-21  4-5-19-19-21-19  4-21  19-15-12-4-,  13-9-19-5  =  14-. ', choix="2. Decode from A1-Z26")}\n",
#             tps_btw_letters=0.008,
#         )
#         print("\nPREDICT:")
#         slow_type(
#             f"\t{A1Z26(txtt='16-5-18-6-5-3-20 / -18-9-7-8-20  ', choix="2. Decode from A1-Z26").replace('20', 't'):<15}{A1Z26(txtt='16-18-5-4-9-3-20  12-1  2-15-14-14-5  22-1-12-5-21-18  4-5  3-1-18-4-!  ', choix="2. Decode from A1-Z26")}\n\t{A1Z26(txtt='14-15-20 / -9-13-16-5-18-6-5-3-20 ', choix="2. Decode from A1-Z26").replace('20', 't'):<15}{A1Z26(txtt='16-18-5-4-9-3-20  12-1  13-1-21-22-1-9-19-5  22-1-12-5-21-18  4-5  3-1-18-4-!  ', choix="2. Decode from A1-Z26")}",
#             tps_btw_letters=0.008,
#         )
#         print("\n" * 3)
#         input()
#         clear_lines(17)
#         continue
#     # darks code
#     elif cheat and ("sold" in mise and ("+" in mise or "*" in mise)):
#         cheat_use += 1
#         operateur = "*" if "*" in mise else "+"
#         mise = mise.replace("sold", "").replace("+", "").replace("*", "")
#         mise = mise.strip()
#         if not mise.isdigit():
#             cprint("incorrect", ALERTE_CRITIQUE)
#             time.sleep(0.3)
#             clear_lines(2)
#             continue
#         if operateur == "+":
#             config["sold"] += float(mise)
#             cprint(f"sold += {float(mise)} -> {config['sold']}", WARNING)
#         elif operateur == "*":
#             config["sold"] *= float(mise)
#             cprint(f"sold *= {float(mise)} -> {config['sold']}", WARNING)
#         time.sleep(0.75)
#         clear_lines(2)
#         continue
#     elif cheat and "card" in mise:
#         cheat_use += 1
#         print(f"card -> {card},   color -> {color}")
#         input()
#         clear_lines(3)
#         continue
#     elif cheat and "ch" in mise:
#         cheat_use += 1
#         tour += 1
#         deck_of_cards.append(card)
#         historique.remove(card)
#         clear_lines()
#         game(tour)
#     elif cheat and ("inf" in mise or "full" in mise):
#         cheat_use += 1
#         mise = mise.replace("full", "").replace("inf", "")
#         mise = mise.strip()
#         if not mise.isdigit():
#             cprint("incorrect", ALERTE_CRITIQUE)
#             time.sleep(0.3)
#             clear_lines(2)
#             continue
#         mise = float(mise)
#         clear_lines()
#         print(f"Enter a mise:   {mise}")

#     elif "all" in mise and "-" in mise:
#         mise = mise.replace("all", "").replace("-", "")
#         mise = mise.strip()
#         if not mise.isdigit():
#             cprint("incorrect", ERROR)
#             time.sleep(0.3)
#             clear_lines(2)
#             continue
#         if int(mise) >= config["sold"]:
#             cprint("incorrect", ERROR)
#             time.sleep(0.3)
#             clear_lines(2)
#             continue
#         mise = config["sold"] - int(mise)
#         clear_lines()
#         print(f"Enter a mise:   {mise}")
#     elif mise == "all":
#         mise = config["sold"]
#         clear_lines()
#         print(f"Enter a mise:   {mise}")
#     elif "last" in mise and ("-" in mise or "+" in mise):
#         operateur = "+" if "+" in mise else "-"
#         mise = mise.replace("last", "").replace("-", "").replace("+", "")
#         mise = mise.strip()
#         if not mise.isdigit():
#             cprint("incorrect", ERROR)
#             time.sleep(0.3)
#             clear_lines(2)
#             continue
#         if operateur == "+":
#             if last_mise + int(mise) >= config["sold"]:
#                 cprint("incorrect", ERROR)
#                 time.sleep(0.3)
#                 clear_lines(2)
#                 continue
#             mise = last_mise + int(mise)
#             clear_lines()
#             print(f"Enter a mise:   {mise}")
#         else:
#             if last_mise - int(mise) <= 0:
#                 cprint("incorrect", ERROR)
#                 time.sleep(0.3)
#                 clear_lines(2)
#                 continue
#             mise = last_mise - int(mise)
#             clear_lines()
#             print(f"Enter a mise:   {mise}")

#     elif mise == "last":
#         if last_mise > config["sold"]:
#             clear_lines()
#             continue
#         mise = last_mise
#         clear_lines()
#         print(f"Enter a mise:   {mise}")

#     elif ("half" in mise or mise == "h") and ("-" in mise or "+" in mise):
#         operateur = "+" if "+" in mise else "-"
#         mise = (
#             mise.replace("half", "")
#             .replace("-", "")
#             .replace("+", "")
#             .replace("h", "")
#         )
#         mise = mise.strip()
#         if not mise.isdigit():
#             cprint("incorrect", ERROR)
#             time.sleep(0.3)
#             clear_lines(2)
#             continue
#         if operateur == "+":
#             if config["sold"] // 2 + int(mise) >= config["sold"]:
#                 cprint("incorrect", ERROR)
#                 time.sleep(0.3)
#                 clear_lines(2)
#                 continue
#             mise = config["sold"] // 2 + int(mise)
#         else:
#             if config["sold"] // 2 - int(mise) <= 0:
#                 cprint("incorrect", ERROR)
#                 time.sleep(0.3)
#                 clear_lines(2)
#                 continue
#             mise = config["sold"] // 2 - int(mise)
#         clear_lines()
#         print(f"Enter a mise:   {mise}")

#     elif mise == "half" or mise == "h":
#         mise = config["sold"] // 2
#         clear_lines()
#         print(f"Enter a mise:   {mise}")
#     elif any(
#         x in mise for x in ["r", "rand", "random", "aleatoire", "aléatoire"]
#     ):
#         val = mise
#         for x in ["rand", "random", "aleatoire", "aléatoire", "r"]:
#             val = val.replace(x, "")
#         val = val.strip()
#         parts = val.split()

#         if (
#             len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit()
#         ):  # Syntaxe: "r 50 200"
#             start = int(parts[0])
#             stop = min(int(parts[1]), int(config["sold"]))
#             if stop <= start:
#                 mise = min(max(start, 1), int(config["sold"]))
#             else:
#                 mise = random.randrange(start, stop)
#         elif len(parts) == 1 and parts[0].isdigit():  # Syntaxe: "r 50"
#             start = int(parts[0])
#             if start >= int(config["sold"]):
#                 mise = max(1, int(config["sold"]) - 1)
#             else:
#                 mise = random.randrange(start, int(config["sold"]))
#         else:
#             if int(config["sold"]) > 20:
#                 mise = random.randrange(int(config["sold"]))
#             else:
#                 mise = random.randrange(
#                     11, int(config["sold"]) + 1
#                 )  # Syntaxe: "r"
#         clear_lines()
#         print(f"Enter a mise:   {mise}")

#     elif not mise.isdigit() or int(mise) > config["sold"] or 10 > int(mise):
#         cprint("incorrect", ERROR)
#         time.sleep(0.3)
#         clear_lines(2)
#         continue
#     mise, last_mise = int(mise), int(mise)

#     prediction = input("Enter your prediction (R/N):   ").lower().strip()

#     # darks code
#     if cheat and (prediction == "perfect" or prediction == "right"):
#         cheat_use += 1
#         prediction = color
#     elif cheat and (prediction == "not" or prediction == "false"):
#         cheat_use += 1
#         prediction = (
#             f"{NOIR}Noir{RESET}"
#             if color == f"{ROUGE_FLASH}Rouge{RESET}"
#             else f"{ROUGE_FLASH}Rouge{RESET}"
#         )

#     elif prediction in exit:
#         clear_lines(2)
#         continue
#     elif prediction == "last":
#         prediction = last_prediction
#     elif prediction in [
#         "ra",
#         "rand",
#         "random",
#         "aleatoire",
#         "aléatoire",
#         "al",
#     ]:
#         prediction = random.choice(
#             [f"{ROUGE_FLASH}Rouge{RESET}", f"{NOIR}Noir{RESET}"]
#         )
#     elif prediction in ["ch", "change", "not", "c"]:
#         prediction = (
#             f"{ROUGE_FLASH}Rouge{RESET}"
#             if last_prediction == f"{NOIR}Noir{RESET}"
#             else f"{NOIR}Noir{RESET}"
#         )
#     elif prediction in [
#         "st",
#         "stat",
#         "stats",
#         "lo",
#         "logic",
#         "be",
#         "best",
#         "better",
#     ]:
#         pourc_red, pourc_black = float(stats["Rouge"]), float(stats["Noir"])
#         if pourc_black < pourc_red:
#             prediction = f"{ROUGE_FLASH}Rouge{RESET}"
#         elif pourc_red < pourc_black:
#             prediction = f"{NOIR}Noir{RESET}"
#         else:
#             prediction = random.choice(
#                 [f"{ROUGE_FLASH}Rouge{RESET}", f"{NOIR}Noir{RESET}"]
#             )
#     elif prediction in [
#         "r",
#         "red",
#         "rouge",
#         "1",
#         "sang",
#         "s",
#         "b",
#         "blood",
#     ]:
#         prediction = f"{ROUGE_FLASH}Rouge{RESET}"
#     else:
#         prediction = f"{NOIR}Noir{RESET}"
#     last_prediction = prediction
#     cprint(f"You chosed §{prediction}!", SOULIGN2)
#     time.sleep(0.35)
#     break
