### Projekt z przedmiotu programowanie obiektowe i grafika komputerowa
### Autorzy: Dorian Neumann 198415, Antoni Sulkowski 197564
### Plik, w którym zaimplementowane jest modelowanie całego robota wraz z elementami dodatkowymi

import OpenGL
from OpenGL.GLU import *
from OpenGL.GL import *

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

def Segment1(): #Obrót regionalny wokół osi z
    glPushMatrix()
    quadric=gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (1.0, 1.0, 0.0, 1.0))  # Żółty kolor
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
    glRotatef(-90, 1, 0, 0)
    glTranslatef(0, 0, 0.1)
    gluCylinder(quadric, 0.2, 0.12, 0.5, 32, 4)

    gluDeleteQuadric(quadric)
    glPopMatrix()

def JointSegment2():
    glPushMatrix()
    quadric=gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.0, 1.0, 0.0, 1.0)) 
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
    gluSphere(quadric, 0.1, 32, 32)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.0, 0.0, 1.0, 1.0))
    glTranslatef(0.0, 0.0, 0.1)
    gluCylinder(quadric, 0.1, 0.1, 0.5, 32, 4)
    gluDeleteQuadric(quadric)
    glPopMatrix()

def JointSegment3():
    glPushMatrix()
    quadric=gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.0, 1.0, 0.0, 1.0)) 
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
    gluSphere(quadric, 0.1, 32, 32)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.0, 0.0, 1.0, 1.0))
    glTranslatef(0.0, 0.0, 0.1)
    gluCylinder(quadric, 0.1, 0.1, 0.7, 32, 4)
    gluDeleteQuadric(quadric)
    glPopMatrix()
