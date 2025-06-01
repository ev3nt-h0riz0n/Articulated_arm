### Projekt z przedmiotu programowanie obiektowe i grafika komputerowa
### Autorzy: Dorian Neumann 198415, Antoni Sulkowski 197564
### Plik obsługujący rysowanie otoczenia robota i rzeczy z tym związanych. (Światło, pokój, rakieta, funkcje wspomagające, napisy na ekranie)

import OpenGL
import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *


def light():
        #Oświetlenie (żeby było widać, że 3D)
    glEnable(GL_DEPTH_TEST)  # Potrzebne do poprawnego nakładania się obiektów

    # Światło i cieniowanie
    glEnable(GL_LIGHTING) #To włącza oświetlenie
    glEnable(GL_LIGHT0) #To włącza pierwsze źródło światła
    glEnable(GL_NORMALIZE)  # Automatyczne normalizowanie wektorów normalnych

    # Ustawienie źródła światła
    glLightfv(GL_LIGHT0, GL_POSITION,  (0.0, 3.0, 1.5, 1.0))  # Pozycja swiatła
    glLightfv(GL_LIGHT0, GL_DIFFUSE,   (1.0, 1.0, 1.0, 1.0))  # Białe światło
    glLightfv(GL_LIGHT0, GL_SPECULAR,  (1.0, 1.0, 1.0, 1.0)) 

    # Materiał - DO DOPRACOWANIA
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0) 


def draw_room(size=5):
    """Draws a simple room with floor, ceiling, and four walls."""
    glPushMatrix()
    glDisable(GL_LIGHTING)  # Optional: flat color for room

    # Floor
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-size, 0, -size)
    glVertex3f(size, 0, -size)
    glVertex3f(size, 0, size)
    glVertex3f(-size, 0, size)
    glEnd()

    # Ceiling
    glColor3f(0.8, 0.8, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(-size, size, -size)
    glVertex3f(size, size, -size)
    glVertex3f(size, size, size)
    glVertex3f(-size, size, size)
    glEnd()

    # Walls
    wall_colors = [(0.6, 0.6, 0.8), (0.6, 0.8, 0.6), (0.8, 0.6, 0.6), (0.8, 0.8, 0.6)]
    # Back wall
    glColor3fv(wall_colors[0])
    glBegin(GL_QUADS)
    glVertex3f(-size, 0, -size)
    glVertex3f(size, 0, -size)
    glVertex3f(size, size, -size)
    glVertex3f(-size, size, -size)
    glEnd()
    # Front wall
    glColor3fv(wall_colors[1])
    glBegin(GL_QUADS)
    glVertex3f(-size, 0, size)
    glVertex3f(size, 0, size)
    glVertex3f(size, size, size)
    glVertex3f(-size, size, size)
    glEnd()
    # Left wall
    glColor3fv(wall_colors[2])
    glBegin(GL_QUADS)
    glVertex3f(-size, 0, -size)
    glVertex3f(-size, 0, size)
    glVertex3f(-size, size, size)
    glVertex3f(-size, size, -size)
    glEnd()
    # Right wall
    glColor3fv(wall_colors[3])
    glBegin(GL_QUADS)
    glVertex3f(size, 0, -size)
    glVertex3f(size, 0, size)
    glVertex3f(size, size, size)
    glVertex3f(size, size, -size)
    glEnd()

    glEnable(GL_LIGHTING)
    glPopMatrix()



def Rocket():
    glPushMatrix()
    quadric=gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (1.0, 1.0, 1.0, 1.0)) 
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
    glRotatef(90,0,0,1)
    gluCylinder(quadric, 0.04, 0.04, 0.14, 32, 1)
    gluDisk(quadric, 0.00, 0.04, 32, 1)
    glTranslatef(0,0,0.14)
    gluDisk(quadric, 0.00, 0.04, 32, 1)

    gluDeleteQuadric(quadric)
    glPopMatrix()

def CwiercSfery(radius):
    glPushMatrix()
    #Włacza ograniczenia płaszczyznowe
    glEnable(GL_CLIP_PLANE0)
    glEnable(GL_CLIP_PLANE1)
    glEnable(GL_CLIP_PLANE2)
    #Ogranicza sferę jak na analizie matematycznej (X>0 itd)
    eqnX = [1.0, 0.0, 0.0, 0.0]
    glClipPlane(GL_CLIP_PLANE0, eqnX)
    eqnY = [0.0, 1.0, 0.0, 0.0]
    glClipPlane(GL_CLIP_PLANE1, eqnY)
    eqnZ = [0.0, 0.0, 1.0, 0.0]
    glClipPlane(GL_CLIP_PLANE2, eqnZ)

    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.0, 0.8, 1.0, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
    gluSphere(quadric, radius, 32, 32)

    gluDeleteQuadric(quadric)
    glDisable(GL_CLIP_PLANE0)
    glDisable(GL_CLIP_PLANE1)
    glDisable(GL_CLIP_PLANE2)
    glPopMatrix()



def base():
    glPushMatrix() #Te dwie funkcje są ważne (glPopMatrix)!! Żeby obiekt cały czas nie zmieniał położenia przez glTranslatef
    quadric = gluNewQuadric() #Tworzymy obiekt do rysowania walca
    gluQuadricNormals(quadric, GLU_SMOOTH)  # Włączamy generowanie normalnych do cieniowania

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.5, 0.5, 0.5))  # Żółty kolor
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)

    glRotatef(-90, 1, 0, 0)  # Obróć, żeby stał "na ziemi"
    glTranslatef(0, 0, -0.1)  # Połowa wysokości w dół

    # Główna część cylindra
    gluCylinder(quadric, 0.5, 0.5, 0.2, 32, 4)
    #Składnia (quadratic, promiec dolny, promien gorny,  wysokosc, ilosc faces poprzecznych, ilosc faces pionowych) ~Jak nie wiesz o co chodzi to pisz
    # Usuwamy quadric po użyciu (unikamy wycieków pamięci)
    # Dolne wieczko
    gluDisk(quadric, 0, 0.5, 32, 1)
    # Górne wieczko
    glPushMatrix()
    glTranslatef(0, 0, 0.2)
    gluDisk(quadric, 0, 0.5, 32, 1)
    glPopMatrix()

    gluDeleteQuadric(quadric)
    glPopMatrix()


