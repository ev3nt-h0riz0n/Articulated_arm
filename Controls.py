import pygame
from pygame.locals import *

def keyscamera(xrot,yrot):
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
    if(xrot<=-30):
        xrot=-30
    if(xrot>=20):
        xrot=20
    return xrot, yrot

def Keys1(rot):
    keys=pygame.key.get_pressed()
    if(rot<=358):
        if keys[pygame.K_1]:
            rot+=2
    if (rot>=2):
        if keys[pygame.K_2]:
            rot-=2
    return rot

def Keys2(rot):
    keys=pygame.key.get_pressed()
    if(rot<=88):
        if keys[pygame.K_3]:
            rot+=2
    if(rot>=2):
        if keys[pygame.K_4]:
            rot-=2
    return rot