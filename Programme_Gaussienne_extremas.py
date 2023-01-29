from math import *
import matplotlib.pyplot as plt

# defintion des bornes du graphique
xmin = -5
xmax = 5
ymin = -5
ymax = 5
pas = 0.1
nbx = int((xmax-xmin)/pas)
nby = int((ymax-ymin)/pas)

# nous demandons à l'utilisateur le nombre de gaussiennes qu'il souhaite afficher puis leurs paramètres

print("Les bornes vont de",xmin,"à",xmax,"en x et de",ymin,"à",ymax,"en y.")
nb = int(input("Veuillez donner le nombre de gaussiennes que vous voulez afficher (Nous n'en affichons pas plus de 5): "))
if nb > 0:
    sigma1 = float(input("Veuillez saisir les paramètres que vous utiliserez pour la première gaussienne : \nsigma n°1: "))
    sigma2 = float(input("\nsigma n°2: "))
    m1 = float(input("\nespérence n°1: "))
    m2 = float(input("\nespérence n°2: "))
    if nb > 1:
        sigma3 = float(input("Veuillez saisir les paramètres que vous utiliserez pour la deuxième gaussienne : \nsigma n°1: "))
        sigma4 = float(input("\nsigma n°2: "))
        m3 = float(input("\nespérence n°1: "))
        m4 = float(input("\nespérence n°2: "))
        if nb > 2:
            sigma5 = float(input("Veuillez saisir les paramètres que vous utiliserez pour la troisième gaussienne : \nsigma n°1: "))
            sigma6 = float(input("\nsigma n°2: "))
            m5 = float(input("\nespérence n°1: "))
            m6 = float(input("\nespérence n°2: "))
            if nb > 3:
                sigma7 = float(input("Veuillez saisir les paramètres que vous utiliserez pour la quatrième gaussienne : \nsigma n°1: "))
                sigma8 = float(input("\nsigma n°2: "))
                m7 = float(input("\nespérence n°1: "))
                m8 = float(input("\nespérence n°2: "))
                if nb > 4:
                    sigma9 = float(input("Veuillez saisir les paramètres que vous utiliserez pour la cinquième gaussienne : \nsigma n°1: "))
                    sigma10 = float(input("\nsigma n°2: "))
                    m9 = float(input("\nespérence n°1: "))
                    m10 = float(input("\nespérence n°2: "))
                    if nb > 5:
                        print("Nous ne pouvons pas afficher plus de 5 gaussiennes.")

def f(x,y):
    a = 1 / (sigma1*sigma2 *2*pi)
    c = ((x-m1)/sigma1)**2
    d = ((y-m2)/sigma2)**2
    return (a * exp((-1/2)*(c + d)))

def g(x,y):
    a1 = 1 / (sigma3*sigma4 *2*pi)
    c1 = ((x-m3)/sigma3)**2
    d1 = ((y-m4)/sigma4)**2
    return (a1 * exp((-1/2)*(c1 + d1)))

def h(x,y):
    a2 = 1 / (sigma5*sigma6 *2*pi)
    c2 = ((x-m5)/sigma5)**2
    d2 = ((y-m6)/sigma6)**2
    return (a2 * exp((-1/2)*(c2 + d2)))

def k(x,y):
    a3 = 1 / (sigma7*sigma8 *2*pi)
    c3 = ((x-m7)/sigma7)**2
    d3 = ((y-m8)/sigma8)**2
    return (a3 * exp((-1/2)*(c3 + d3)))

def l(x,y):
    a4 = 1 / (sigma9*sigma10 *2*pi)
    c4 = ((x-m9)/sigma9)**2
    d4 = ((y-m10)/sigma10)**2
    return (a4 * exp((-1/2)*(c4 + d4)))

def gaussiennes(x,y):
    if nb >= 5:
        return f(x,y) + g(x,y) + h(x,y) + k(x,y) + l(x,y)
    elif nb == 4:
        return f(x,y) + g(x,y) + h(x,y) + k(x,y)
    elif nb == 3:
        return f(x,y) + g(x,y) + h(x,y)
    elif nb == 2:
        return f(x,y) + g(x,y)
    elif nb == 1:
        return f(x,y)
    else:
        return 0

# definition de Z et Zbas, deux listes de listes qui contiennent
# respectivement la valeur de la fonction f(x,y), et une attribution
# en entier en fonction de la valeur de f...

Z = []
Zbas = []
Liste_x = []
Liste_y = []
for i in range(nbx+1):
    x = xmin + i*pas
    L = []
    Lbas = []
    for j in range(nby+1):
        y = ymin + j*pas
        w = gaussiennes(x,y)
        if (w > gaussiennes(x-pas,y) and w > gaussiennes(x+pas,y) and w > gaussiennes(x,y-pas) and w > gaussiennes(x-pas,y-pas) and w > gaussiennes(x+pas,y-pas) and w > gaussiennes(x-pas,y+pas) and w > gaussiennes(x,y+pas) and w > gaussiennes(x+pas,y+pas)):
            Liste_y.append(x)
            Liste_x.append(y)
        L.append(w)
        Lbas.append(1)
    Z.append(L)
    Zbas.append(Lbas)

# tracé de la fonction f stockée dans matrice Z
plt.imshow(Z, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap='hot', alpha=0.5)

# ajout de l'echelle de valeurs 
plt.colorbar()

# points extremas de chaques gaussiennes

x_max = [Liste_x]
y_max = [Liste_y]

# ajout de ces extremas sur la figure
plt.plot(x_max, y_max,'ro', label='extrema')

# ajout des zones definies par Zbas
plt.imshow(Zbas, extent=[xmin, xmax, ymin, ymax], origin='lower', cmap='hot', alpha=0.5)

# ajout d'un titre au dessus du graphique
plt.title("Gaussiennes vue du dessus")

plt.legend()
plt.show()

# valeurs pour tester notre programme
"""m1 = 3.0
sigma1 = 1.0        # valeurs de la 1ère Gaussienne
m2 = 2.0
sigma2 = 0.5

m3 = -3.0
sigma3 = 0.5        # valeurs de la 2ème Gaussienne
m4 = -3.0
sigma4 = 1.0

m5 = 2.0
sigma5 = 1.0        # valeurs de la 3ème Gaussienne
m6 = -2.0
sigma6 = 0.5

m7 = -2.0
sigma7 = 0.75        # valeurs de la 4ème Gaussienne
m8 = 3
sigma8 = 0.75

m9 = 0
sigma9 = 1        # valeurs de la 5ème Gaussienne
m10 = 0
sigma10 = 0.5"""