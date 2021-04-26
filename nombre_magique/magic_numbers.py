import random
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_VIES = 4
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX)

def demander_nombre(nbre_min, nombre_max):
    nombre_int = 0

    while nombre_int == 0:
        nombre_str = input(f"Choiissisez le nombre magique entre {nbre_min} et {nombre_max} ? ")
        try:
            nombre_int = int(nombre_str)
        except:
            print('Erreur: vous devez rentrer un nombre')
        else:
            if nombre_int < nbre_min or nombre_int > nombre_max:
                print(f"Le nombre doit être compris entre {nbre_min} et {nombre_max}")
                nombre_int = 0


    return nombre_int

nombre = 0
vies = NB_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)

    if nombre < NOMBRE_MAGIQUE:
        print("le nombre magique est plus grand")
        vies -= 1
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre maigqye est plus petit")
        vies -= 1
    else:
        print("vous avez trouver")

if vies == 0:
    print(f"vous avez perdu, le nombre magique etais {NOMBRE_MAGIQUE}")



# gagne = False
# for i in range(0, NB_VIES):
#     vies = NB_VIES-i
#     print(f"Il vous reste {vies} vies")
#     nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
#     if nombre == NOMBRE_MAGIQUE:
#         print("Bravo, vous avez gagné")
#         gagne = True
#         break
#     elif nombre > NOMBRE_MAGIQUE:
#         print("Le nombre magique est plus petit")
#     else:
#         print("Le nombre magique est plus grand")
#
# if not gagne:
#     print(f"Vous avez perdu! Le nombre magique était: {NOMBRE_MAGIQUE}")
