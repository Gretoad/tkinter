from random import random
from tkinter import *

## File

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


## Fonctions

# Création du tableau

def my_map(size):
    tab = []
    for _ in range(size):
        lgn = []
        for _ in range(size):
            p = random()
            if p <= 0.41:
                lgn.append(-2)
            else:
                lgn.append(-1)
        tab.append(lgn)
    return tab

# Simulation d'un incendie

def incendie(tab, d, feu):
    file = File()
    file_futur = File()
    x, y = feu[0], feu[1]
    file.enfiler((x, y))
    tab[y][x] = 0
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
                        if tab[voisin[1]][voisin[0]] == -1:
                            file_futur.enfiler(voisin)
                            tab[voisin[1]][voisin[0]] = 0
                            if (voisin[0],voisin[1]) in d:
                                if n//4 > 255:
                                    red = hex(255)[2:]
                                else:
                                    red = hex(n//4)[2:]
                                    if len(red) == 1:
                                        red = "0" + red
                                    color = "#" + red + (4-len(red))*"0" + "FF"
                                tissu.itemconfig(d[(voisin[0],voisin[1])], fill = color, outline = color)
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
    
def tableau(size, n_cell, tab, feu):
    d = {}
    cell_size = size / n_cell
    for y in range(n_cell):
        for x in range(n_cell):
            start_x = cell_size*x
            start_y = cell_size*y
            end_x = start_x+cell_size
            end_y = start_y+cell_size
            if tab[y][x] == -1:
                num = set_cell(start_x, start_y, end_x, end_y, "#000000")
                d[(x,y)] = num
            # Si c'est la position exactement du départ de  l'incendie
            if x == feu[0] and y == feu[1]:
                num = set_cell(start_x, start_y, end_x, end_y, "#000000")
    return d


## valeurs et appels

size_tab = 500
depart_du_feu = (size_tab//2, size_tab//2)
tab1 = my_map(size_tab)

d = tableau(SIZE, size_tab, tab1, depart_du_feu)
incendie(tab1, d, depart_du_feu)
