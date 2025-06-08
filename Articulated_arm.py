### Projekt z przedmiotu programowanie obiektowe i grafika komputerowa
### Autorzy: Dorian Neumann 198415, Antoni Sulkowski 197564
### Plik, w którym zaimplementowane jest modelowanie całego robota wraz z elementami dodatkowymi

import OpenGL
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

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
    glTranslatef(0,0,0.5)
    gluDisk(quadric, 0, 0.12, 32, 1)
    glTranslatef(0.1 ,0.0, 0.0)
    gluCylinder(quadric, 0.02, 0.02, 0.1, 16, 4)
    glTranslatef(0.0 ,0.0, 0.1)
    gluSphere(quadric, 0.02, 32,32)
    glTranslatef(-0.2 ,0.0, 0.0)
    gluSphere(quadric, 0.02, 32,32)
    glTranslatef(0.0 ,0.0, -0.1)
    gluCylinder(quadric, 0.02, 0.02, 0.1, 16, 4)
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
    gluDisk(quadric, 0, 0.1, 32, 1)
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
    gluCylinder(quadric, 0.1, 0.1, 0.4, 32, 4)
    gluDisk(quadric, 0, 0.1, 32, 1)
    glPopMatrix()

def EffectorJoint():
    glPushMatrix()
    quadric=gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (1.0, 0.0, 0.0, 1.0)) 
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)
    gluSphere(quadric, 0.1, 32, 32)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (1.0, 0.4, 0.0, 1.0)) 
    glTranslatef(0.0,0.0,0.1)
    gluCylinder(quadric, 0.12,0.12,0.05,32,4)
    gluDisk(quadric, 0, 0.12, 32, 1)
    glPushMatrix()
    glTranslatef(0, 0, 0.05)
    gluDisk(quadric, 0, 0.12, 32, 1)
    glPopMatrix()
    gluDeleteQuadric(quadric)
    glPopMatrix()
