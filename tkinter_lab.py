from random import randint 
from time import sleep


def my_map(size):
    tab = []
    inc = []
    for y in range(size):
        lgn = []
        for x in range(size):
            lgn.append(0)
            inc.append((x, y))
        tab.append(lgn)
    return tab, inc

def aff(tab):
    sortie = ""
    for lgn in tab:
        sortie+=str(lgn) + "\n"
    return sortie

def initialisation(tab, inc):
    # INITIALISATION
    murs = []
    # 1
    debut = (10, 10)
    # 2
    premier = inc.pop(inc.index(debut))
    tab[debut[1]][debut[0]] = 100
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 3
    for delta in DIRECTIONS:
        try:
            voisin  = (premier, (premier[0]+delta[0], premier[1]+delta[1]))
            murs.append(voisin)
        except IndexError:
            pass
    return murs

def set_lab(tab, inc):
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    murs = initialisation(tab, inc)
    n = 101 # nombre de repetition
    # PROCEDE
    while len(murs) > 0:
        # 4
        p = randint(0, len(murs)-1)
        mur = murs.pop(p)
        # 5
        if mur[1] in inc:
            # 6
            cell = inc.pop(inc.index(mur[1]))
            tab[mur[1][1]][mur[1][0]] = n
            n+=1
            # 7
            for delta in DIRECTIONS:
                try:
                    voisin  = (cell, (cell[0]+delta[0], cell[1]+delta[1]))
                    murs.append(voisin)
                except IndexError:
                    pass
        print(aff(tab))





## Valeurs et appels

size_lab = 20
tab1, inc = my_map(size_lab)
set_lab(tab1, inc)
