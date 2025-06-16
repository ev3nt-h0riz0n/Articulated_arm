### Projekt z przedmiotu programowanie obiektowe i grafika komputerowa
### Autorzy: Dorian Neumann 198415, Antoni Sulkowski 197564
### Plik, w którym zaimplementowane jest modelowanie całego robota wraz z elementami dodatkowymi

import OpenGL
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

class RobotArm:
    def __init__(self):
        self.quadric=gluNewQuadric()
        gluQuadricNormals(self.quadric, GLU_SMOOTH)
        
    def __del__(self):
        gluDeleteQuadric(self.quadric)

    def set_material(self, ambient_diffuse, specular=(1.0, 1.0, 1.0, 1.0), shininess=50.0):
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, ambient_diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, specular)
        glMaterialf(GL_FRONT, GL_SHININESS, shininess)

    def Segment(self): #Obrót regionalny wokół osi z
        glPushMatrix()
        self.set_material((1.0,1.0,0.0,1.0))
        glRotatef(-90, 1, 0, 0)
        glTranslatef(0, 0, 0.1)
        gluCylinder(self.quadric, 0.2, 0.12, 0.5, 32, 4)
        glTranslatef(0,0,0.5)
        gluDisk(self.quadric, 0, 0.12, 32, 1)

        #Little handles
        glTranslatef(0.1 ,0.0, 0.0)
        gluCylinder(self.quadric, 0.02, 0.02, 0.1, 16, 4)
        glTranslatef(0.0 ,0.0, 0.1)
        gluSphere(self.quadric, 0.02, 32,32)
        glTranslatef(-0.2 ,0.0, 0.0)
        gluSphere(self.quadric, 0.02, 32,32)
        glTranslatef(0.0 ,0.0, -0.1)
        gluCylinder(self.quadric, 0.02, 0.02, 0.1, 16, 4)
        glPopMatrix()

    def JointSegment2(self):
        glPushMatrix()
        self.set_material((0.0,1.0,0.0,1.0))
        gluSphere(self.quadric, 0.1, 32, 32)
        self.set_material((0.0,0.4,1.0,1.0))
        glTranslatef(0.0, 0.0, 0.1)
        gluCylinder(self.quadric, 0.1, 0.1, 0.5, 32, 4)
        gluDisk(self.quadric, 0, 0.1, 32, 1)
        glPopMatrix()

    def JointSegment3(self):
        glPushMatrix()
        self.set_material((0.0,1.0,0.0,1.0))
        gluSphere(self.quadric, 0.1, 32, 32)
        self.set_material((0.0,0.4,1.0,1.0))
        glTranslatef(0.0, 0.0, 0.1)
        gluCylinder(self.quadric, 0.1, 0.1, 0.4, 32, 4)
        gluDisk(self.quadric, 0, 0.1, 32, 1)
        glPopMatrix()

    def EffectorJoint(self):
        glPushMatrix()
        self.set_material((0.0,1.0,0.0,1.0))
        gluSphere(self.quadric, 0.1, 32, 32)
        self.set_material((1.0,0.2,0.0,1.0))
        glTranslatef(0.0,0.0,0.1)
        gluCylinder(self.quadric, 0.12,0.12,0.05,32,4)
        gluDisk(self.quadric, 0, 0.12, 32, 1)
        glPushMatrix()
        glTranslatef(0, 0, 0.05)
        gluDisk(self.quadric, 0, 0.12, 32, 1)
        glPopMatrix()
        glPopMatrix()



