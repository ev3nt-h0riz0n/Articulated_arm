### Projekt z przedmiotu programowanie obiektowe i grafika komputerowa
### Autorzy: Dorian Neumann 198415, Antoni Sulkowski 197564
### Plik, w którym zaimplementowane jest sterowanie różnymi segmentami robota i dzwieki
### przy tym wydawane.

import pygame
# from Sound import *
from pygame.locals import *
from Coordinates import *

def keyscamera(xrot,yrot):
    t1,t2 = xrot,yrot
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        xrot-=1
    if keys[pygame.K_DOWN]:
        xrot+=1
    if keys[pygame.K_LEFT]:
        yrot-=1
    if keys[pygame.K_RIGHT]:
        yrot+=1
    #Warunki, zeby za bardzo nie obracac kamerą
    if(xrot<=-25):
        xrot=-25
    if(xrot>=20):
        xrot=20
    #if t1!=xrot or t2!=yrot:
    #     sounds()
    return xrot, yrot

def Keys1(rot):
    t1=rot
    keys=pygame.key.get_pressed()
    if(rot<=358):
        if keys[pygame.K_1]:
            rot+=2
    if (rot>=2):
        if keys[pygame.K_2]:
            rot-=2
    #if t1!=rot:
    #    sounds()
    return rot

def Keys2(rot):
    t1=rot
    keys=pygame.key.get_pressed()
    if(rot<=88):
        if keys[pygame.K_3]:
            rot+=2
    if(rot>=2):
        if keys[pygame.K_4]:
            rot-=2
    #if t1!=rot:
    #    sounds()
    return rot

def Keys3(rot):
    t1=rot
    keys=pygame.key.get_pressed()
    if rot<=88:
        if keys[pygame.K_6]:
            rot+=2
    if(rot>=2):
        if keys[pygame.K_5]:
            rot-=2
    #if t1!=rot:
    #    sounds()
    return rot

def EffectorKeys(ef1,ef2,ef3):
    keys=pygame.key.get_pressed()
    if ef1<=28:
        if keys[pygame.K_KP4]: #6 na NumPadzie
            ef1+=2
    if ef1>=-28:
        if keys[pygame.K_KP6]:
            ef1-=2
    if ef2<=28:
        if keys[pygame.K_KP2]:
            ef2+=2
    if ef2>=-28:
        if keys[pygame.K_KP8]:
            ef2-=2
    if ef3<=28:
        if keys[pygame.K_KP7]:
            ef3+=2
    if ef3>=-28:
        if keys[pygame.K_KP9]:
            ef3-=2
    return ef1,ef2,ef3

def GetToPosition():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_k]:
        x = float(input("Wpisz wartosc x"))
        y = float(input("Wpisz wartosc y"))
        z = float(input("wpisz wartosc z"))
        results = inversed_kinematics(x,y,z)
        if results:
            return (results)
        else: None
    else:
        return None
    
def LearnMovement():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_l]:
        return 1
    else:
        return 0

def PlayLearnedMovement():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_p]:
        return 1
    else: 
        return 0
