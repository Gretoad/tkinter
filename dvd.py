from tkinter import *
from math import *
from random import *
from time import sleep
import os

H=835
W=1530
x=0
y=0
r=500
theta=0

bg_color="#000000"

def color():
    c='#'
    for i in range(3):
        c+=hex(randint(16,255))[2:]
    return c

tissu=Canvas(height=H,width=W,bg=bg_color)

def sgt(x,y,r,theta):
    X=r*cos(theta)+x
    Y=r*sin(theta)+y
    tissu.create_line(x,y,X,Y,fill=color())
    return X,Y

def triangle(x,y,r,theta):
    for i in range(3):
        x,y=sgt(x,y,r,theta)
        theta+=2*pi/3

def hexagone(x,y,r,theta):
    for i in range(6):
        x,y=sgt(x,y,r,theta)

        theta+=2*pi/6
def quatre_vingtgone(x,y,r,theta):
    for i in range(randint(1,800)):
        x,y=sgt(x,y,r,theta)
        theta+=pi*2/randint(2, 30)
        
def plateau(x,y,r,theta):
    for _ in range(H//r*2):
        for _ in range(W//r*2):
            triangle(x,y,r,theta)
            x+=r*2
        x=0
        y+=r*2
        
def point(x,y,color):
    tissu.create_line(x, y, x+1, y,fill=color)

def fonction_cos(x,n):
    y=cos(x/n*tau)*H/4
    return y

def fonction_sin(x,n):
    y=sin(x/n*tau)*H/4
    return y

def fonction_tan(x,n):
    y=tan(x/n*tau)*H/4
    return y

def dessiner_fonction_cos(x,n):
    for x in range(W):
        Y=fonction_cos(x,n)
        point(x,H-H/2-Y,"#FF0000")
    
def dessiner_fonction_sin(x,n):
    for x in range(W):
        Y=fonction_sin(x,n)
        point(x,H-H/2-Y,"#DDDDFF")

def dessiner_fonction_tan(x,n):
    for x in range(W):
        Y=fonction_tan(x,n)
        point(x,H-H/2-Y,"#FF00FF")
        
def cercle(r,theta):
    x=randint(0,W)
    y=randint(0,H)
    n=200
    R=n*r/2/pi
    y=y-R
    for i in range(n):
        x,y=sgt(x,y,r,theta)
        theta+=2*pi/n
          
def texte(x,y,r,texte,police,style,bg_color):
    txt=tissu.create_text(x+r/2,y+r/2,fill=bg_color,text=f"{texte}",font=(f"{police}",r//5,f"{style}"))
    return txt

def event(x,y,X,Y,vx,vy):
    test=False
    if X==W:
        vx.append(-1)
        test=True
    if x==0:
        vx.append(1)
        test=True
    if Y==H:
        vy.append(-1)
        test=True
    if y==0:
        vy.append(1)
        test=True
    return test

def acceleration(r):
    sleep(r*10**-5)
    
def dvd(r):
    txt_color=color()    
    polygon_color=color()
    x=W//2-r/2
    y=H//2-r/2
    n=0
    vx=[choice([-1,1])]
    vy=[choice([-1,1])]
    while True:
        X=x+r
        Y=y+r
        carre=tissu.create_polygon(x,y,x,Y,X,Y,X,y,fill=polygon_color)
        txt=texte(x,y,r,("Bowser" if n%2==0 else "Toad"),"arial","italic",txt_color)
        test = event(x,y,X,Y,vx,vy)
        x+=vx[-1]
        y+=vy[-1]
        tissu.pack()
        tissu.update()
        if test==False:
            tissu.delete(txt)
        else:
            r-=r//10
            polygon_color=color() #change la couleur du carré
            txt_color=color() #change la couleur du texte 
            n+=1 #change le texte
        tissu.delete(carre) 
        
def cahsohtoa():
    n=1
    while True:
        dessiner_fonction_cos(x,n)
        dessiner_fonction_sin(x,n)
        dessiner_fonction_tan(x,n)
        tissu.update()
        tissu.delete(ALL)
        tissu.pack()
        n+=1
dvd(r)
