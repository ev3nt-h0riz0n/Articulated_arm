import random
import pygame

#Inicjalizacja dzwiekow
pygame.mixer.init()
channel = pygame.mixer.Channel(0)

# Lista dostępnych dźwięków
sound_files = ["sounds/Robotic1.mp3", "sounds/Robotic2.mp3", "sounds/Robotic3.mp3"]

# Zmienna do śledzenia aktualnego dźwięku
current_sound = None
last_played_path = None

def sounds(play=True):
    global current_sound, last_played_path

    if play:
        # Jeśli nie gra już dźwięk – wylosuj nowy i zagraj
        if not channel.get_busy():
            path = random.choice(sound_files)
            current_sound = pygame.mixer.Sound("sounds/Robotic2.mp3")
            last_played_path = path
            channel.play(current_sound, loops=-1)
    else:
        # Zatrzymaj dźwięk jeśli jakiś leci
        if channel.get_busy():
            channel.stop()
            current_sound = None
            last_played_path = None