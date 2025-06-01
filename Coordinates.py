import math

def position(rot1, rot2, rot3):
    l1 = 0.6 #Dlugosc nieruchomego segmentu + staw
    l2 = 0.7 #Dlugosc drugiego segmentu + staw
    l3 = 0.67 #Dlugosc trzeciego segmentu + chwytak

    r1 = math.radians(rot1)
    r2= math.radians(rot2)
    r3 = math.radians(rot3)

    z = l1+l2*math.sin(r2)+l3*math.sin(r2-r3) #Wspolrzedna z
    r = l2*math.cos(r2) + l3*math.cos(r2-r3) #Odleglosc od srodka ukladu wspolrzednych

    x = r*math.sin(r1)
    y = r*math.cos(r1)

    return [x,y,z]

def inversed_kinematics(x, y, z):
    l1 = 0.6  # offset w osi Z
    l2 = 0.7
    l3 = 0.67

    r = math.sqrt(x**2 + y**2)
    d = math.sqrt(r**2 + (z - l1)**2)

    if d > l2 + l3 or (d<math.sqrt(l2**2+l3**2)):
        print("Poza zakresem robota")
        return None

    rot1 = math.atan2(x, y)

    # Obliczenie kąta rot3 (łokcia)
    cos_angle3 = (l2**2 + l3**2 - d**2) / (2 * l2 * l3)
    cos_angle3 = max(min(cos_angle3, 1), -1)  # zabezpieczenie 
    rot3 = math.pi - math.acos(cos_angle3)

    # Obliczenie kąta rot2 (ramienia)
    angle_a = math.atan2(z - l1, r)
    cos_angle_b = (l2**2 + d**2 - l3**2) / (2 * l2 * d)
    cos_angle_b = max(min(cos_angle_b, 1), -1)
    angle_b = math.acos(cos_angle_b)
    rot2 = angle_a + angle_b

    rot1 = round(math.degrees(rot1))
    rot2 = round(math.degrees(rot2))
    rot3 = round(math.degrees(rot3))

    print(f"rot1 = {rot1:.2f}, rot2 = {rot2:.2f}, rot3 = {rot3:.2f}")
    return [rot1, rot2, rot3]

def setcoordinates(goal1,goal2,goal3,cur1,cur2,cur3):
    done = 0
    if goal1!=cur1:
        if goal1>cur1: cur1+=1
        else: cur1-=2
    if goal2!=cur2:
        if goal2>cur2: cur2+=1
        else: cur2-=2
    if goal3!=cur3:
        if goal3>cur3: cur3+=1
        else: cur3-=2
    if goal1!=cur1 or goal2!=cur2 or goal3!=cur3:
        done = 0
    else: 
        done = 1
        print("Przesuwanie zakonczone")

    return (cur1,cur2,cur3, not done)
    
