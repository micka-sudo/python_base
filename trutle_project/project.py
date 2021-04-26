import turtle

t = turtle.Turtle()


# for i in range(0,5):
#     t.forward(30)
#     t.left(90)
#     t.forward(30)
#     t.right(90)
# t.forward(30)

def escalier(taille, nb):
    for i in range(0,nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)

# escalier(30,5)

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

carre(50)

def carres(taille_depart, nb):

    for i in range(0, nb):
        taille = (i+1)*taille_depart
        carre(taille)
carres(20,6)

turtle.done()
