import string

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


def MAJ():
    texte_enter = input("enter a text to change the MAJ mode: \n")
    texte_exit = ""
    for i in texte_enter:
        if i == " ":
            texte_exit += " "
            continue
        c = a.index(i)
        d = b[c]
        texte_exit += d
    return texte_exit


is_running = True

while is_running:
    choice = input("enter ? (y/n):    ").strip().casefold()
    if choice == "y":
        print(MAJ())
    else:
        is_running = False
input("")
