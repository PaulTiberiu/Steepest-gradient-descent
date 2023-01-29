# exemple de visualisation graphique en 2d utilisant matplotlib

from math import *
import matplotlib.pyplot as plt

# defintion des bornes de la figures
xmin = -5
xmax = 5
ymin = -5
ymax = 5
pas = 0.1
nbx = int((xmax-xmin)/pas)
nby = int((ymax-ymin)/pas)

m1 = 3.0
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

def gaussiennes(x,y):
    return f(x,y) + g(x,y) + h(x,y)

# definition de Z et Zbas, deux listes de listes qui contiennent
# respectivement la valeur de la fonction f(x,y), et une attribution
# en entier en fonction de la valeur de f...

Z = []
Zbas = []
for i in range(nbx+1):
    x = xmin + i*pas
    L = []
    Lbas = []
    for j in range(nby+1):
        y = ymin + j*pas
        w = gaussiennes(x,y)
        L.append(w)
        if w < 0 :
            Lbas.append(-1)
        else :
            Lbas.append(1)
    Z.append(L)
    Zbas.append(Lbas)

# tracé de la fonction f stockée dans matrice Z
plt.imshow(Z, extent=[xmin, xmax, ymin, ymax], origin='lower',
            cmap='hot', alpha=0.5)

# ajout echelle de valeurs 
plt.colorbar()

# points extremums de chaques gaussiennes

def find_X_in_g(xmax,xmin,ymin,ymax):
    fmax = g(xmin,ymin)
    imax = xmin
    i = xmin
    j = ymin
    while i < xmax:
        while j < ymax:
            fct = g(i,j)
            if fct > fmax :
                imax = i
                fmax = fct 
            j = j + pas
        i = i + pas
        j = ymin
    return imax

def find_Y_in_g(xmax,xmin,ymin,ymax):
    fmax = g(xmin,ymin)
    jmax = ymin
    i = xmin
    j = ymin
    while i < xmax:
        while j < ymax:
            fct = g(i,j)
            if fct > fmax :
                jmax = j
                fmax = fct
            j = j + pas
        i = i + pas
        j = ymin
    return jmax

def find_X_in_f(xmax,xmin,ymin,ymax):
    fmax = f(xmin,ymin)
    imax = xmin
    i = xmin
    j = ymin
    while i < xmax:
        while j < ymax:
            fct = f(i,j)
            if fct > fmax :
                imax = i
                fmax = fct 
            j = j + pas
        i = i + pas
        j = ymin
    return imax

def find_Y_in_f(xmax,xmin,ymin,ymax):
    fmax = f(xmin,ymin)
    jmax = ymin
    i = xmin
    j = ymin
    while i < xmax:
        while j < ymax:
            fct = f(i,j)
            if fct > fmax :
                jmax = j
                fmax = fct
            j = j + pas
        i = i + pas
        j = ymin
    return jmax

def find_X_in_h(xmax,xmin,ymin,ymax):
    fmax = h(xmin,ymin)
    imax = xmin
    i = xmin
    j = ymin
    while i < xmax:
        while j < ymax:
            fct = h(i,j)
            if fct > fmax :
                imax = i
                fmax = fct 
            j = j + pas
        i = i + pas
        j = ymin
    return imax
                                                                        #ICI LES COORDONÉES SONT INVERSÉES
def find_Y_in_h(xmax,xmin,ymin,ymax):
    fmax = h(xmin,ymin)
    jmax = ymin
    i = xmin
    j = ymin
    while i < xmax:
        while j < ymax:
            fct = h(i,j)
            if fct > fmax :
                jmax = j
                fmax = fct
            j = j + pas
        i = i + pas
        j = ymin
    return jmax

x_max = [find_X_in_g(xmax,xmin,ymin,ymax),find_X_in_f(xmax,xmin,ymin,ymax),find_X_in_h(xmax,xmin,ymin,ymax)]
y_max = [find_Y_in_g(xmax,xmin,ymin,ymax),find_Y_in_f(xmax,xmin,ymin,ymax),find_Y_in_h(xmax,xmin,ymin,ymax)]   #SI ON ECHANGE x_max ET y_max ON OBTIENT LES BONS MAXIMAS

# ajout de ces deux points sur la figure
plt.plot(y_max, x_max,'ro', label='extrema')


# ajout des zones definies par Zbas
plt.imshow(Zbas, extent=[xmin, xmax, ymin, ymax], origin='lower',
            cmap='hot', alpha=0.5)
     
plt.legend()   
plt.show()

