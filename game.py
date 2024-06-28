from os import truncate
import pygame
import sys
import tkinter as tk
from mainmenu import beatmap_selected
import time

#variables

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 175, 255)
grey = (175, 175, 175)
yellow = (255, 235, 0)
green = (0, 225, 55)
purple = (215, 0, 225)

combo = 0

key1_color = grey
key2_color = grey
key3_color = grey
key4_color = grey

def obtener_resolucion():
    pygame.init()
    info_pantalla = pygame.display.Info()
    ancho = info_pantalla.current_w
    alto = info_pantalla.current_h
    pygame.quit()
    return ancho, alto
ancho, alto = obtener_resolucion()

screen_width = ancho//4
screen_height = alto//1.2
radius = (screen_width // 8) - 10

col1 = [50, -50, 0]
col2 = [150, -50, 1]
col3 = [250, -50, 2]
col4 = [350, -50, 3]

no_note = True

current_time=0
start_time = 120 / 1000.0

perfect_timer = 0
perfect_note_hit = False

good_timer = 0
good_note_hit=False

bad_timer = 0
bad_note_hit = False

#counters
key_num_set = 0

#arrays

notes = []
seconds = []
circles_on_scene = []
keys = [False, False, False, False]

durations =[]
#functions

def set_notes():
    with open(f'beatmaps/{beatmap_selected}/notes.txt', 'r', encoding='utf-8') as file:
        lineas = file.readlines()
        for linea in lineas:
            note = linea.split()
            seconds.append(float(note[0]))
            notes.append(int(note[1]))
            if len(note) > 2:
                durations.append(float(note[2]))
            else:
                durations.append(0)  # Si no hay duración especificada, se asume nota regular

          

def display_keys():
    pygame.draw.circle(screen, key1_color, (50, 530), radius)
    pygame.draw.circle(screen, key2_color, (150, 530), radius)
    pygame.draw.circle(screen, key3_color, (250, 530), radius)
    pygame.draw.circle(screen, key4_color, (350, 530), radius)

def create_circle():

    global key_num_set
    global no_note

    key_num = notes[key_num_set]
    
    if key_num == 1:
        col = col1.copy()
        color = white
    elif key_num == 2:
        col = col2.copy()
        color = blue
    elif key_num == 3:
        col = col3.copy()
        color = blue
    elif key_num == 4:
        col = col4.copy()
        color = white
    else:
        no_note = True

    if not no_note:
        circles_on_scene.append((screen, color, col, radius))

    key_num_set += 1

def perfect_note():

    global perfect_timer
    global perfect_note_hit

    if perfect_note_hit:
        screen.blit(perfect_text, perfect_center)
        perfect_timer += 1
        if perfect_timer >= 5:
            perfect_note_hit = False
            perfect_timer = 0

def good_note():

    global good_timer
    global good_note_hit

    if good_note_hit:
        screen.blit(good_text, good_center)
        good_timer += 1
        if good_timer >= 5:
            good_note_hit = False
            good_timer = 0

def bad_note():

    global bad_timer
    global bad_note_hit

    if bad_note_hit:
        screen.blit(bad_text, bad_center)
        bad_timer += 1
        if bad_timer >= 5:
            bad_note_hit = False
            bad_timer = 0
circle_speed = 2
def update_circles():
    global combo
    global perfect_note_hit
    global good_note_hit
    global bad_note_hit
    global no_note

    hit_detected = [False] * 4  # Bandera para detectar si una nota fue golpeada para cada columna

    if not no_note:
        for circle in circles_on_scene[:]:
            pygame.draw.circle(circle[0], circle[1], (circle[2][0], circle[2][1]), circle[3])
            fpscirlcespeed = circle_speed * dt * targetfps
            circle[2][1] += fpscirlcespeed

            if 470 <= circle[2][1] <= 600 and keys[circle[2][2]] and not hit_detected[circle[2][2]]:
                combo += 1
                perfect_note_hit = True
                circles_on_scene.remove(circle)
                hit_detected[circle[2][2]] = True  # Marcar que una nota fue golpeada en esta columna
            
            elif 430 <= circle[2][1] <= 640 and keys[circle[2][2]] and not hit_detected[circle[2][2]]:
                combo += 1
                good_note_hit = True
                circles_on_scene.remove(circle)
                hit_detected[circle[2][2]] = True  # Marcar que una nota fue golpeada en esta columna
            
            elif 390 <= circle[2][1] <= 680 and keys[circle[2][2]] and not hit_detected[circle[2][2]]:
                combo += 1
                bad_note_hit = True
                circles_on_scene.remove(circle)
                hit_detected[circle[2][2]] = True  # Marcar que una nota fue golpeada en esta columna

            elif circle[2][1] > 680:
                combo = 0
                circles_on_scene.remove(circle)

    else:
        no_note = False



time_for_timing = 0
song_timed = False

def song_timing():

    global time_for_timing
    global song_timed

    if not song_timed:
        if current_time >= (580/((circle_speed)*540)):
            pygame.mixer.music.play()
            song_timed = True

def counter():
    global current_time
    current_time = pygame.time.get_ticks() / 1000.0 - start_time

#display
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Osu!Mania')
game_icon = pygame.image.load("data/mania_icon.png")
pygame.display.set_icon(game_icon)

#music

pygame.mixer.init()
pygame.mixer.music.load(f'beatmaps/{beatmap_selected}/{beatmap_selected}.mp3')

#fonts
font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 35)

#text


perfect_text = font2.render('PERFECT', True, yellow)
good_text = font2.render('GOOD', True, green)
bad_text = font2.render('BAD', True, purple)

perfect_center = perfect_text.get_rect(center=(screen_width / 2, screen_height / 2.4))
good_center = good_text.get_rect(center=(screen_width / 2, screen_height / 2.4))
bad_center = bad_text.get_rect(center=(screen_width / 2, screen_height / 2.4))

#sound effects
hitsound = pygame.mixer.Sound("data/hit_sound.ogg")

set_notes()
seconds_set = 0

create = 0
clock = pygame.time.Clock()

fps = 120
targetfps = 540

prev_time = time.time()
dt = 0

running = True
while running:

    now=time.time()
    dt=now-prev_time
    prev_time = now
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  
                keys[0] = True
                key1_color = white
                hitsound.play()
            if event.key == pygame.K_f:  # Si presiona F y no estaba presionado antes
                keys[1] = True
                key2_color = white
                hitsound.play()
            if event.key == pygame.K_j:  # Si presiona J y no estaba presionado antes
                keys[2] = True
                key3_color = white
                hitsound.play()
            if event.key == pygame.K_k:  # Si presiona K y no estaba presionado antes
                keys[3] = True
                key4_color = white
                hitsound.play()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                key1_color = grey
            if event.key == pygame.K_f:
                key2_color = grey
            if event.key == pygame.K_j:
                key3_color = grey
            if event.key == pygame.K_k:
                key4_color = grey

            

    screen.fill(black)


    display_keys()

    counter()

    song_timing()

    if seconds_set >= 0 and seconds_set < len(seconds):
        if current_time >= seconds[seconds_set]:
            create_circle()
            seconds_set += 1
            # Check if next seconds are the same
            while seconds_set < len(seconds) and seconds[seconds_set] == seconds[seconds_set - 1]:
                create_circle()
                seconds_set += 1
    update_circles()
    combo_text = font1.render(f'{combo}', True, yellow)
    text_rect = combo_text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(combo_text, text_rect)

    perfect_note()
    good_note()
    bad_note()
    keys=[False, False, False, False]
    
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
sys.exit()