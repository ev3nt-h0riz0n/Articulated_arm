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
from Surroundings import *
from Coordinates import *

def send_position_to_panel(x, y, z):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #inny socket do wysyłania pozycji, żeby nie kolidował z odbieraniem danych
    sock.sendto(f"pos:{x},{y},{z}".encode(), ("127.0.0.1", 5007))
    sock.close()


def udp_listener(rot_vars, magnet_var, should_exit):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, _ = sock.recvfrom(1024)
        cmd = data.decode()
        if cmd == "EXIT":
            should_exit[0] = True
            break
        if cmd.startswith("seg1:"):
            rot_vars[0] = int(cmd.split(":")[1])
        elif cmd.startswith("seg2:"):
            rot_vars[1] = int(cmd.split(":")[1])
        elif cmd.startswith("seg3:"):
            rot_vars[2] = int(cmd.split(":")[1])
        elif cmd.startswith("magnet:"):
            magnet_var[0] = bool(int(cmd.split(":")[1]))

UDP_IP = "127.0.0.1"
UDP_PORT = 5006

#Ta funkcja odpowiada za całą symulację :)
def init():
    xrot, yrot, rot1, rot2, rot3 = 0,0,0,0,0
    rot_vars = [rot1, rot2, rot3]
    magnet_var = [False]
    should_exit = [False]
    listener_thread = threading.Thread(target=udp_listener, args=(rot_vars, magnet_var, should_exit), daemon=True)
    listener_thread.start()


    #Obsluga chwytaka magnesowego
    magnet_on = False
    usedsuccesfully = False
    mr1,mr2,mr3=0,0,0 #Sprawdzenie w jakim obrocie znajduje sie robot po upuszczeniu przedmiotu

    #Do obsługi przesunięcia robota w konkretne współrzędne
    r1,r2,r3 = 0,0,0  #Sprawdzanie obecnego obrotu robota w momencie włączenia funkcji
    movingworking = 0 #Czy przesuwanie jest w toku?


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
        magnet_on = magnet_var[0]
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_m : 
                    magnet_on = not magnet_on
                    usedsuccesfully = True

        # Sprawdzenie czy program ma się zakończyć
        if should_exit[0]:
            running = False

        # Pozyskanie wartości obrotów z listenera
        rot1 = rot_vars[0]
        rot2 = rot_vars[1]
        rot3 = rot_vars[2]

        xrot, yrot = keyscamera(xrot, yrot)
        if movingworking == 0:    
            rot1 = Keys1(rot1)
            rot2 = Keys2(rot2)
            rot3 = Keys3(rot3)

        #Funkcja odpowiadajaca za przemieszczenie do konkretnego punktu
        result = GetToPosition() 
        if result:
            r1,r2,r3 = result
            print(result)
            movingworking=1
        
        if movingworking == 1:
            rot1, rot2, rot3, movingworking = setcoordinates(r1,r2,r3,rot1,rot2,rot3)


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Ruch kamery
        glPushMatrix()
        glRotatef(xrot, 1, 0, 0)
        glRotatef(yrot, 0, 1, 0)

        draw_room(size=5)  #Rysowanie pokoju

        #Rysowanie robota
        glPushMatrix()
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

        if magnet_on: #Prymitywne dzialanie magnesu
            glTranslatef(0, -0.05, 0.19)
            Rocket()
            w1,w2,w3 = position(rot1,rot2,rot3)
            mr1,mr2,mr3 = rot1,rot2,rot3
        elif usedsuccesfully == 1:
            glPopMatrix()
            glPopMatrix()
            glPopMatrix()
            glPopMatrix()
            glPopMatrix()

            #Rysowanie rakiety po upuszczeniu przez chwytak magnetyczny. Trzeba powtórzyć całą sekwencje
            #przemieszczeń, żeby zwrócić tamte współrzędne.
            glRotatef(mr1, 0, 1, 0)
            glTranslatef(0.0, 0.7, 0)         
            glRotatef(mr2, -1, 0, 0)
            glTranslatef(0, 0, 0.7)          
            glRotatef(mr3, 1, 0, 0)
            glTranslatef(0, 0.0, 0.65)       
            glTranslatef(0, -0.05, 0.19)    
            Rocket()


        if magnet_on or (usedsuccesfully==0 and magnet_on == 0):
            glPopMatrix() #Koniec chwytaka
            glPopMatrix() #Koniec 3 segmentu
            glPopMatrix() #Koniec 2 segmentu
            glPopMatrix() #Koniec 1 segmentu
            glPopMatrix() #Koniec bazy

            if magnet_on==0 and usedsuccesfully==0:
                glTranslatef(0.2, 0.3, 1)
                Rocket()

        #Generacja osobnego obiektu (rakiety)

        glPopMatrix() #Kamera
        x, y, z = position(rot1, rot2, rot3)
        
        #wysyłanie pozycji do panelu
        send_position_to_panel(x, y, z)
        print((x, y, z))

        pygame.display.flip()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            
        pygame.time.wait(25) #Funkcja zatrzymująca na chwilę program przed powtórzeniem pętli. Stosowane, aby program nie
        #Powodował zbyt dużego obciążenia.
    pygame.quit()




init()
