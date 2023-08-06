import random
import time

choix = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b",
         "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
code_al = []
decompte = 0
width = 1
test = 0
mdp = input("choisis ton mot de passe")

while True:
    nbr_combi = 62 ** width

    new_code = random.choices(choix, k=width)
    new_code = "".join(map(str, new_code))
    if int(decompte) == nbr_combi:
        width += 1
        print(width)
        continue
    elif new_code == mdp:
        print("trouver !")
        break
    if new_code not in code_al:
        code_al.append(new_code)
        test += 1
        decompte += 1
        print(new_code)
        print(decompte)
        continue
    elif new_code in code_al:
        continue
