### Projekt z przedmiotu programowanie obiektowe i grafika komputerowa
### Autorzy: Dorian Neumann 198415, Antoni Sulkowski 197564
### Plik główny obsługujący wszystkie inne funkcje.


#Import bibliotek potrzebnych do wykonania projektu
import pygame
import OpenGL
import random
import threading
import socket
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Articulated_arm import *
from Controls import *


def light():
        #Oświetlenie (żeby było widać, że 3D)
    glEnable(GL_DEPTH_TEST)  # Potrzebne do poprawnego nakładania się obiektów

    # Światło i cieniowanie
    glEnable(GL_LIGHTING) #To włącza oświetlenie
    glEnable(GL_LIGHT0) #To włącza pierwsze źródło światła
    glEnable(GL_NORMALIZE)  # Automatyczne normalizowanie wektorów normalnych

    # Ustawienie źródła światła
    glLightfv(GL_LIGHT0, GL_POSITION,  (1, 1, -3, 0))  # Światło kierunkowe z góry z przodu
    glLightfv(GL_LIGHT0, GL_DIFFUSE,   (1.0, 1.0, 1.0, 1.0))  # Białe światło
    glLightfv(GL_LIGHT0, GL_SPECULAR,  (1.0, 1.0, 1.0, 1.0))

    # Materiał - DO DOPRACOWANIA
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0) 



#Ta funkcja odpowiada za całą symulację :)
def init():
    xrot, yrot, rot1, rot2, rot3 = 0,0,0,0,0
    rot_vars = [rot1, rot2, rot3]
    listener_thread = threading.Thread(target=udp_listener, args=(rot_vars,), daemon=True)
    listener_thread.start()
    magnet_on = False  # Stan chwytaka magnetycznego
    #Inicjalizacja okna i ustawienie pozycji operatora
    pygame.init() 
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(60, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -0.3, -3.5)
    glRotatef(25, 1, 0, 0)
    light()

    #Generowanie symulacji
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Update from UDP listener
        rot1 = rot_vars[0]
        rot2 = rot_vars[1]
        rot3 = rot_vars[2]

        xrot, yrot = keyscamera(xrot, yrot)
        rot1 = Keys1(rot1)
        rot2 = Keys2(rot2)
        rot3 = Keys3(rot3)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply camera rotation to the whole scene (room and robot)
        glPushMatrix()
        glRotatef(xrot, 1, 0, 0)
        glRotatef(yrot, 0, 1, 0)

        draw_room(size=5)  # Draw the room

        # Raise the robot above the floor (e.g., y = 0.2)
        glPushMatrix()
        glTranslatef(0.0, 0.01, 0.0)  # Adjust this value as needed
        base()

        glPushMatrix()  # 1 Segment
        glRotatef(rot1, 0, 1, 0)
        Segment1()

        glPushMatrix()  # 2 Segment
        glTranslatef(0.0, 0.7, 0)
        glRotatef(rot2, -1, 0, 0)
        JointSegment2()

        glPushMatrix()  # 3 Segment
        glTranslatef(0, 0, 0.7)
        glRotatef(rot3, 1, 0, 0)
        JointSegment3()

        glPushMatrix()  # Chwytak
        glTranslatef(0, 0.0, 0.65)
        EffectorJoint()

        glPopMatrix()  # Koniec chwytaka
        glPopMatrix()  # Koniec 3 segmentu
        glPopMatrix()  # Koniec 2 segmentu
        glPopMatrix()  # Koniec 1 segmentu
        glPopMatrix()  # Koniec bazy

        glPopMatrix()  # End camera rotation

        # Switch to 2D mode for GUI overlay
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)
        screen = pygame.display.get_surface()
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        pygame.display.flip()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            
        pygame.time.wait(25) #Funkcja zatrzymująca na chwilę program przed powtórzeniem pętli. Stosowane, aby program nie
        #Powodował zbyt dużego obciążenia.
    pygame.quit()

def udp_listener(rot_vars):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, _ = sock.recvfrom(1024)
        cmd = data.decode()
        if cmd.startswith("seg1:"):
            rot_vars[0] = int(cmd.split(":")[1])
        elif cmd.startswith("seg2:"):
            rot_vars[1] = int(cmd.split(":")[1])
        elif cmd.startswith("seg3:"):
            rot_vars[2] = int(cmd.split(":")[1])

UDP_IP = "127.0.0.1"
UDP_PORT = 5006

init()
