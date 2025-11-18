from random import randint 
from tkinter import *
import copy

# Bon courage pour lire mon code !

class Perle():
    
    def __init__(self, valeur, dessous = None):
        self.v = valeur
        self.dessous = dessous
    
    
class File():
    
    def __init__(self, premiere = None, derniere = None):
        self.premiere = premiere
        self.derniere = derniere
    
    def est_vide(self):
        return self.premiere == None
    
    def enfiler(self, e):
        ancienne_derniere = self.derniere
        self.derniere = Perle(e)
        if self.est_vide():
            self.premiere = self.derniere
        else:
            ancienne_derniere.dessous = self.derniere
    
    def defiler(self):
        ancienne_premiere = self.premiere
        self.premiere = self.premiere.dessous
        if self.est_vide():
            self.derniere = None
        return ancienne_premiere.v

# Création du tableau
def my_map(size):
    tab = []
    inc = []
    for y in range(size):
        lgn = []
        for x in range(size):
            if x%2==0 and y%2==0:
                lgn.append(0) # Cellules
            else:
                lgn.append(-1) # Murs
            inc.append((x, y))
        tab.append(lgn)
    return tab, inc


def initialisation(tab, inc, debut, d, color):
    # INITIALISATION
    murs = []
    # 2
    premier = inc.pop(inc.index(debut))
    tab[debut[1]][debut[0]] = 1
    tissu.itemconfig(d[(premier[0],premier[1])], fill = color, outline = color)
    DIRECTIONS = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    # 3
    for delta in DIRECTIONS:
        try:
            voisin  = (premier, (premier[0]+delta[0], premier[1]+delta[1]))
            murs.append(voisin)
        except IndexError:
            pass
    return murs


def set_lab(tab, inc, debut, d):
    color = "#FFFFFF"
    DIRECTIONS = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    murs = initialisation(tab, inc, debut, d, color)
    n = 1 # nombre de repetition
    # PROCEDE
    while len(murs) > 0:
        # 4
        p = randint(0, len(murs)-1)
        mur = murs.pop(p)
        # 5
        if mur[1] in inc:
            # 6
            cell = inc.pop(inc.index(mur[1]))
            tab[mur[1][1]][mur[1][0]] = n+2
            variation = ((mur[1][0]-mur[0][0])//2, (mur[1][1]-mur[0][1])//2)
            n+=1
            # 7
            for delta in DIRECTIONS:
                try:
                    voisin  = (cell, (cell[0]+delta[0], cell[1]+delta[1]))
                    murs.append(voisin)
                except IndexError:
                    pass
            tissu.itemconfig(d[(mur[1][0],mur[1][1])], fill = color, outline = color)
            try:
                tissu.itemconfig(d[(mur[0][0]+variation[0],mur[0][1]+variation[1])], fill = color, outline = color)
                tab[mur[0][1]+variation[1]][mur[0][0]+variation[0]] = n+1
            except KeyError:
                pass
        window.update()

def incendie(tab, d, feu):
    # copies
    d_copie = copy.deepcopy(d)
    tab_copie = copy.deepcopy(tab)
    color = "#0000FF"
    file = File()
    file_futur = File()
    x, y = feu[0], feu[1]
    file.enfiler((x, y))
    tissu.itemconfig(d_copie[(feu[0],feu[1])], fill = color, outline = color)
    tab_copie[y][x] = 0
    DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]
    n = 1
    # Scan des voisins
    while True:
        while not file.est_vide():
            val = file.defiler()
            for delta in DIRECTIONS:
                try:
                    voisin = (val[0]+delta[0], val[1]+delta[1])
                    if voisin[0] >= 0 and voisin[1] >= 0:
                        if tab_copie[voisin[1]][voisin[0]] > 0:
                            file_futur.enfiler(voisin)
                            tab_copie[voisin[1]][voisin[0]] = 0
                            if (voisin[0],voisin[1]) in d_copie:
                                if n > 255:
                                    red = hex(255)[2:]
                                else:
                                    red = hex(n)[2:]
                                    if len(red) == 1:
                                        red = "0" + red
                                color = "#" + red + "00FF"
                                tissu.itemconfig(d_copie[(voisin[0],voisin[1])], fill = color, outline = color)
                except IndexError:
                    pass
        
        if file_futur.est_vide():
            break        
        # Remplace file_futur par file
        while not file_futur.est_vide():
            file.enfiler(file_futur.defiler())
        
        
        window.update()
        n+=1

def search(tab, d, fin):
    # copies
    d_copie = copy.deepcopy(d)
    tab_copie = copy.deepcopy(tab)
    color = "#00FF00"
    file = File()
    file_futur = File()
    x, y = fin[0], fin[1]
    file.enfiler((x, y))
    tissu.itemconfig(d_copie[(fin[0],fin[1])], fill = color, outline = color)
    tab_copie[y][x] = 0
    DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]
    n = 1
    # Scan des voisins
    while True:
        while not file.est_vide():
            val = file.defiler()
            for delta in DIRECTIONS:
                try:
                    voisin = (val[0]+delta[0], val[1]+delta[1])
                    if voisin[0] >= 0 and voisin[1] >= 0:
                        if tab_copie[voisin[1]][voisin[0]] > 0:
                            if tab_copie[voisin[1]][voisin[0]] > tab_copie[val[1]][val[0]]:
                                file_futur.enfiler(voisin)
                                tab_copie[voisin[1]][voisin[0]] = 0
                                if (voisin[0],voisin[1]) in d:
                                    if n > 255:
                                        red = hex(255)[2:]
                                    else:
                                        red = hex(n)[2:]
                                        if len(red) == 1:
                                            red = "0" + red
                                    color = "#" + red + "FF00"
                                    tissu.itemconfig(d_copie[(voisin[0],voisin[1])], fill = color, outline = color)
                except IndexError:
                    pass
                
        # Remplace file_futur par file
        while not file_futur.est_vide():
            file.enfiler(file_futur.defiler())
        
        window.update()
        n+=1

# Interface graphique

SIZE = 800
window = Tk()
tissu = Canvas(window, width = SIZE, height = SIZE, bg = "#000000")
tissu.pack()

def set_cell(x, y, X, Y, color):
    num = tissu.create_rectangle(x, y, X, Y, fill = color, outline = color)
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
            elif tab[y][x] == -1:
                num = set_cell(start_x, start_y, end_x, end_y, "#000000")
                d[(x,y)] = num
    return d



## Valeurs et appels

size_lab = 101
tab1, inc = my_map(size_lab)
d = tableau(SIZE, size_lab, tab1)
debut = (0, 0)
fin = (size_lab-1, size_lab-1)
set_lab(tab1, inc, debut, d)
incendie(tab1, d, debut)
search(tab1, d, fin)
