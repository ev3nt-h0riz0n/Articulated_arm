import FreeSimpleGUI as sg
import socket
import threading

UDP_IP = "127.0.0.1"
UDP_PORT = 5006
FEEDBACK_PORT = 5007  # Inny port do odbierania pozycji
SLIDER_RANGE1 = (0, 360)
SLIDER_RANGE2 = (0, 90)
SLIDER_RANGE3 = (0, 60)
INITIAL_VALUES = {'seg1': 0, 'seg2': 0, 'seg3': 0}

current_position = ['0', '0', '0']

def position_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, FEEDBACK_PORT))
    sock.setblocking(False)
    while True:
        try:
            data, _ = sock.recvfrom(1024)
            msg = data.decode()
            if msg.startswith("pos:"):
                _, coords = msg.split(":")
                x, y, z = coords.split(",")
                current_position[0] = x
                current_position[1] = y
                current_position[2] = z
        except BlockingIOError:
            pass

# Początek wątku do odbierania pozycji
threading.Thread(target=position_listener, daemon=True).start()

def send_command(segment, value):
    msg = f"{segment}:{value}"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    sock.close()

def send_magnet(state):
    msg = f"magnet:{int(state)}"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    sock.close()

#ułożenie okna GUI
layout = [
    [sg.Text('Arm Segment Controls', font=('Arial', 16), justification='center', expand_x=True)],
    [sg.Text('Segment 1'), sg.Slider(range=SLIDER_RANGE1, default_value=INITIAL_VALUES['seg1'], orientation='h', size=(34, 20), key='seg1')],
    [sg.Text('Segment 2'), sg.Slider(range=SLIDER_RANGE2, default_value=INITIAL_VALUES['seg2'], orientation='h', size=(34, 20), key='seg2')],
    [sg.Text('Segment 3'), sg.Slider(range=SLIDER_RANGE3, default_value=INITIAL_VALUES['seg3'], orientation='h', size=(34, 20), key='seg3')],
    [sg.Checkbox('Magnet ON', key='magnet', enable_events=True)],
    [sg.Text('Current position: ', key='pos_label', font=('Arial', 12))],
    [sg.Button('Exit', button_color=('white', 'firebrick3'), expand_x=True)]
]

window = sg.Window('Arm Controls', layout, finalize=True, element_justification='center', font=('Arial', 12))

last_values = INITIAL_VALUES.copy()
last_magnet = False


while True:
    event, values = window.read(timeout=100)
    # Update pozycji w oknie
    try:
        x = round(float(current_position[0]), 2)
        y = round(float(current_position[1]), 2)
        z = round(float(current_position[2]), 2)
        window['pos_label'].update(f"Current position: {x}, {y}, {z}")
    except ValueError:
        window['pos_label'].update("Current position: ?, ?, ?")
    if event in (sg.WIN_CLOSED, 'Exit'):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b'EXIT', (UDP_IP, UDP_PORT))
        sock.close()
        break

    for seg in ['seg1', 'seg2', 'seg3']:
        val = int(values[seg])
        if val != last_values[seg]:
            send_command(seg, val)
            last_values[seg] = val

    if values['magnet'] != last_magnet:
        send_magnet(values['magnet'])
        last_magnet = values['magnet']

window.close()
