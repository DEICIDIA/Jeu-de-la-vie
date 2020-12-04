from random import *

tabCel = [[randint(0,1) for x in range (5)]for y in range (5)]  

def verifPossible(x, y, tabCel):

    if(x < 0 or x > len(tabCel[0]) - 1 or y < 0 or y > len(tabCel) -1):  
        return 0
    else: 
        return tabCel[y][x]  

def countCelAliveAround( _x, _y, _tabCel):
    compteur = 0
    if(verifPossible(_x+1, _y, _tabCel) == 1):   # à droite
        compteur+=1
    if(verifPossible(_x+1, _y - 1, _tabCel) == 1): # en haut à droite
        compteur+=1
    if(verifPossible(_x, _y - 1, _tabCel) == 1):  # en haut  
        compteur+=1
    if(verifPossible(_x-1, _y-1, _tabCel) == 1): # en haut à gauche
        compteur+=1
    if(verifPossible(_x-1, _y, _tabCel) == 1): # à gauche
        compteur+=1
    if(verifPossible(_x-1, _y+1, _tabCel) == 1): # en bas à gauche 
        compteur+=1
    if(verifPossible(_x, _y+1, _tabCel) == 1):   # en bas
        compteur+=1
    if(verifPossible(_x+1, _y+1, _tabCel) == 1):  # en bas à droite
        compteur+=1
    return compteur 

def killCel(_x, _y, _tabCel): 
    _tabCel[_x][_y] = 0

def bornCel(_x, _y, _tabCel): 
    _tabCel[_x][_y] = 0

def nextStep(tab): 
    tabCompteur = getTabCompteur(tab)
    for i in range(len(tabCompteur)): 
        for j in range(len(tabCompteur[i])):
            if(tabCompteur[i][j] > 3 or tabCompteur[i][j] < 2 ):
                tab[i][j] = 0
            elif(tabCompteur[i][j] == 3): 
                tab[i][j] = 1
    return tab
            
def getTabCompteur(_tabCel):
    tabCompteur = []
    for j in range(len(_tabCel)):
        tabCompteur.append([])
        for i in range(len(_tabCel[j])):
            tabCompteur[j].append(countCelAliveAround( i, j, _tabCel))
    return tabCompteur