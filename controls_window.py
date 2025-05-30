import FreeSimpleGUI as sg
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006
#TODO:RÓŻNE ZAKRESY DLA RÓŻNYCH SEGMENTÓW
SLIDER_RANGE = (-90, 90)
INITIAL_VALUES = {'seg1': 0, 'seg2': 0, 'seg3': 0}

def send_command(segment, value):

    msg = f"{segment}:{value}"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    sock.close()

layout = [
    [sg.Text('Arm Segment Controls', font=('Arial', 16), justification='center', expand_x=True)],
    [sg.Text('Segment 1'), sg.Slider(range=SLIDER_RANGE, default_value=INITIAL_VALUES['seg1'], orientation='h', size=(34, 20), key='seg1')],
    [sg.Text('Segment 2'), sg.Slider(range=SLIDER_RANGE, default_value=INITIAL_VALUES['seg2'], orientation='h', size=(34, 20), key='seg2')],
    [sg.Text('Segment 3'), sg.Slider(range=SLIDER_RANGE, default_value=INITIAL_VALUES['seg3'], orientation='h', size=(34, 20), key='seg3')],
    [sg.Button('Exit', button_color=('white', 'firebrick3'), expand_x=True)]
]

window = sg.Window('Arm Controls', layout, finalize=True, element_justification='center', font=('Arial', 12))


last_values = INITIAL_VALUES.copy()

while True:
    event, values = window.read(timeout=100)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    for seg in ['seg1', 'seg2', 'seg3']:
        val = int(values[seg])
        if val != last_values[seg]:
            send_command(seg, val)
            last_values[seg] = val

window.close()
