from random import randint 
from time import sleep
from tkinter import *


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

def initialisation(tab, inc, debut, d, color):
    # INITIALISATION
    murs = []
    # 2
    premier = inc.pop(inc.index(debut))
    tab[debut[1]][debut[0]] = 1
    tissu.itemconfig(d[(premier[0],premier[1])], fill = color)
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 3
    for delta in DIRECTIONS:
        try:
            voisin  = (premier, (premier[0]+delta[0], premier[1]+delta[1]))
            murs.append(voisin)
        except IndexError:
            pass
    return murs

def set_lab(tab, inc, debut, d):
    color = "#0000FF"
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    murs = initialisation(tab, inc, debut, d, color)
    n = 1 # nombre de repetition
    # PROCEDE
    while True:
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
                if n//15 > 255:
                    color = "#FF00FF"
                else:
                    red = hex(n//15)[2:]
                    if len(red) == 1:
                        red = "0" + red
                    color = "#" + red + "00FF"
                tissu.itemconfig(d[(mur[1][0],mur[1][1])], fill = color)
            window.update()
            print(n)
        window.update()



# Interface graphique

SIZE = 800
window = Tk()
tissu = Canvas(window, width = SIZE, height = SIZE, bg = "#000000")
tissu.pack()

def set_cell(x, y, X, Y, color):
    num = tissu.create_rectangle(x, y, X, Y, fill = color)
    return num
    
def tableau(size, n_cell, tab):
    d = {}
    cell_size = size / n_cell
    for y in range(n_cell):
        for x in range(n_cell):
            start_x = cell_size*x
            start_y = cell_size*y
            end_x = start_x+cell_size
            end_y = start_y+cell_size
            if tab[y][x] == 0:
                num = set_cell(start_x, start_y, end_x, end_y, "#000000")
                d[(x,y)] = num
    return d



## Valeurs et appels

size_lab = 200
tab1, inc = my_map(size_lab)
d = tableau(SIZE, size_lab, tab1)
# 1
debut = (size_lab//2, size_lab//2)
set_lab(tab1, inc,debut, d)
