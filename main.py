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
    EfRot1,EfRot2,EfRot3 = 0,0,0 #Rotacja chwytaka

    rot_vars = [rot1, rot2, rot3]
    magnet_var = [False]
    should_exit = [False]
    listener_thread = threading.Thread(target=udp_listener, args=(rot_vars, magnet_var, should_exit), daemon=True)
    listener_thread.start()


    #Obsluga chwytaka magnesowego
    magnet_on = False
    usedsuccesfully = False
    mr1,mr2,mr3, mefr1,mefr2,mefr3=0,0,0,0,0,0 #Sprawdzenie w jakim obrocie znajduje sie robot po upuszczeniu przedmiotu

    #Do obsługi przesunięcia robota w konkretne współrzędne
    movingworking = 0 #Czy przesuwanie jest w toku?

    #Nauka ruchu
    learning = False
    clicked = True
    startingpos =[None,None,None]
    learning_matrix = []

    #Odtwarzanie nauczonego ruchu
    stage = [False, False] #stage[0] - przemieszczenie do startowych, [1] powtorka ruchu


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
            EfRot1,EfRot2,EfRot3 = EffectorKeys(EfRot1,EfRot2,EfRot3)

        #Funkcja odpowiadajaca za przemieszczenie do konkretnego punktu
        result = GetToPosition() 
        if result:
            goalr1,goalr2,goalr3 = result
            print(result)
            movingworking=1
        
        if movingworking == 1:
            rot1, rot2, rot3, movingworking = setcoordinates(goalr1,goalr2,goalr3,rot1,rot2,rot3)

#Mechanizm nauki robota  
        if learning == 0:
            clicked = LearnMovement()
        if clicked == 1: #Gdy wcisniety zostal przycisk L nauki
            startingpos[0],startingpos[1],startingpos[2] = rot1,rot2,rot3 #Ustawiamy pozycje startowe
            print("Uczenie rozpoczate")
            learning_matrix.clear() 
            learning=1 
            learning_index = 0 
            clicked=0 
        if learning == 1: 
            if learning_index<=199: #Petla pozwala przez 5 sekund sciagac obrot segmentow robota
                learning_matrix.append([rot1,rot2,rot3,EfRot1,EfRot2,EfRot3,magnet_on])
                learning_index+=1
            elif learning_index==200: 
                print("Uczenie zakonczone")
                learning = 0

        #Mechanizm odtworzenia zrobionego ruchu
        if learning_matrix and learning == 0: #Gdy na liscie jest zapis ruchow, to:
            played = PlayLearnedMovement()
            if played == 1: stage[0] = 1
            if stage[0] == 1:
                rot1,rot2,rot3, stage[0] = setcoordinates(startingpos[0],startingpos[1],startingpos[2],rot1,rot2,rot3)
                if stage[0] == 0: 
                    stage[1] = 1
                    playing_index = 0
            if stage[1] == 1:
                if playing_index < len(learning_matrix):
                    rot1,rot2,rot3,EfRot1,EfRot2,EfRot3,magnet_on = learning_matrix[playing_index]
                    playing_index+=1
                else:
                    print("Ruch zakonczony")
                    stage[1] = 0


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
        glRotatef(EfRot1, 0, 1, 0) #Obrot prawo lewo
        glRotatef(EfRot2, 1, 0, 0) #Obrot gora dol
        glRotatef(EfRot3, 0, 0, 1) #Obrtót talerza dookola osi talerza
        EffectorJoint()

        if magnet_on: #Prymitywne dzialanie magnesu
            glTranslatef(0, -0.05, 0.19)
            Rocket()
            w1,w2,w3 = position(rot1,rot2,rot3)
            mr1,mr2,mr3,mefr1,mefr2,mefr3 = rot1,rot2,rot3, EfRot1,EfRot2,EfRot3 #mr - magnet rotations, mefr - magnet effector rotations
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
            glRotatef(mefr1, 0, 1, 0) #Obrot prawo lewo
            glRotatef(mefr2, 1, 0, 0) #Obrot gora dol
            glRotatef(mefr3, 0, 0, 1) #Obrtót talerza dookola osi talerza         
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

        pygame.display.flip()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            
        pygame.time.wait(25) #Funkcja zatrzymująca na chwilę program przed powtórzeniem pętli. Stosowane, aby program nie
        #Powodował zbyt dużego obciążenia.
    pygame.quit()


init()
