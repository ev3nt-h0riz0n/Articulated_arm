### Projekt z przedmiotu programowanie obiektowe i grafika komputerowa
### Autorzy: Dorian Neumann 198415, Antoni Sulkowski 197564
### Plik główny obsługujący wszystkie inne funkcje.


#Import bibliotek potrzebnych do wykonania projektu
import pygame
import OpenGL
import math
from pygame.locals import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Articulated_arm import *
from Controls import *
from Surroundings import *
from Coordinates import *


#Ta funkcja odpowiada za całą symulację :)
def init():
    xrot, yrot, rot1, rot2, rot3 = 0,0,0,0,0
    EfRot1,EfRot2,EfRot3 = 0,0,0 #Rotacja chwytaka

    #Obsluga chwytaka magnesowego
    magnet_on = False
    usedsuccesfully = False
    mr1,mr2,mr3, mefr1,mefr2,mefr3=0,0,0,0,0,0 #Sprawdzenie w jakim obrocie znajduje sie robot po upuszczeniu przedmiotu
    object_position = [0,0.3,1]

    #Przemieszczenie globalne
    movingworking = 0

    #Nauka ruchu
    learning = False
    clicked = True
    startingpos =[None,None,None]
    learning_matrix = []

    #Odtwarzanie nauczonego ruchu
    stage = [False, False] #stage[0] - przemieszczenie do startowych, [1] powtorka ruchu
    arm=RobotArm()

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
            elif event.type == KEYDOWN:
                if event.key == K_m :
                    x,y,z = position(rot1,rot2,rot3)
                    if magnet_on == True: 
                        magnet_on = False
                    elif math.sqrt((x-object_position[0])**2+(y-object_position[2])**2+(z-object_position[1])**2)<=0.15:
                        usedsuccesfully = True
                        magnet_on = True
                    else: print("Obiekt poza zasiegiem przedmiotu")

        xrot,yrot=keyscamera(xrot,yrot)
        if movingworking == 0 and stage[0] == 0 and stage[1]==0:
            rot1=Keys1(rot1) #Obrót wokol osi Z
            rot2=Keys2(rot2) #Obrot wokol osi Y
            rot3=Keys3(rot3)
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
                    #Upewnienie się, że obiekt znajduje się przy magniesie, aby go przenieść 
                    x,y,z = position(rot1,rot2,rot3)
                    if math.sqrt((x-object_position[0])**2+(y-object_position[2])**2+(z-object_position[1])**2)>0.15 and magnet_on ==True: 
                        magnet_on=False
                else:
                    print("Ruch zakonczony")
                    stage[1] = 0

                    


        #GENEROWANIE CALEGO ROBOTA
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()  #Odpowiada za ruch kamery
        glRotatef(xrot, 1, 0, 0)
        glRotatef(yrot, 0, 1, 0)
        draw_room(size=5)  

        glPushMatrix() #Baza
        glTranslatef(0.0, 0.01, 0.0)
        base()

        glPushMatrix() #1 Segment
        glRotatef(rot1, 0, 1, 0)
        arm.Segment()

        glPushMatrix() #2 Segment
        glTranslatef(0.0, 0.7, 0)
        glRotatef(rot2, -1, 0, 0)
        arm.JointSegment2()

        glPushMatrix() #3 Segment
        glTranslatef(0, 0, 0.7)
        glRotatef(rot3, 1, 0, 0)
        arm.JointSegment3()

        glPushMatrix() #Chwytak
        glTranslatef(0,0.0, 0.55)
        glRotatef(EfRot1, 0, 1, 0) #Obrot prawo lewo
        glRotatef(EfRot2, 1, 0, 0) #Obrot gora dol
        glRotatef(EfRot3, 0, 0, 1) #Obrtót talerza dookola osi talerza
        arm.EffectorJoint()

        if magnet_on: #Prymitywne dzialanie magnesu
            glTranslatef(0, 0.0, 0.20)
            Object()
            object_position[0], object_position[2], object_position[1] = position(rot1,rot2,rot3)
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
            glTranslatef(0, 0.0, 0.55)
            glRotatef(mefr1, 0, 1, 0) #Obrot prawo lewo
            glRotatef(mefr2, 1, 0, 0) #Obrot gora dol
            glRotatef(mefr3, 0, 0, 1) #Obrtót talerza dookola osi talerza        
            glTranslatef(0, 0.0, 0.20)  
            Object()


        if magnet_on or (usedsuccesfully==0 and magnet_on == 0):
            glPopMatrix() #Koniec chwytaka
            glPopMatrix() #Koniec 3 segmentu
            glPopMatrix() #Koniec 2 segmentu
            glPopMatrix() #Koniec 1 segmentu
            glPopMatrix() #Koniec bazy

            if magnet_on==0 and usedsuccesfully==0:
                glTranslatef(0, 0.3, 1)
                Object()

        #Generacja osobnego obiektu (rakiety)

        glPopMatrix() #Kamera

        pygame.display.flip()
        pygame.time.wait(25) #Funkcja zatrzymująca na chwilę program przed powtórzeniem pętli. Stosowane, aby program nie
        #Powodował zbyt dużego obciążenia.
    pygame.quit()

init()