import math

def position(rot1, rot2, rot3):
    l1 = 0.6 #Dlugosc nieruchomego segmentu + staw
    l2 = 0.7 #Dlugosc drugiego segmentu + staw
    l3 = 0.67 #Dlugosc trzeciego segmentu + chwytak

    r1 = math.radians(rot1)
    r2= math.radians(rot2)
    r3 = math.radians(rot3)

    z = l1+l2*math.sin(r2)+l3*math.sin(r2+r3) #Wspolrzedna z
    r = l2*math.cos(r2) + l3*math.cos(r2+r3) #Odleglosc od srodka ukladu wspolrzednych

    x = r*math.sin(r1)
    y = r*math.cos(r1)

    return [x,y,z]


def inversekinematics(x,y,z): #Ej kurwa ciekawe to nawet XDD
    #Ograniczenia po wprowadzeniu koordynatow