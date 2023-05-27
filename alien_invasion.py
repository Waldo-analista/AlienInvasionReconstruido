import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from stats import Stats
from boton import Boton
from tablero import Tablero

import funciones as f

def correr_juego():
    settings=Settings()

    pygame.init()  #inicia configuraciones en el background que pygame necesita para trabajar correctamente
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))   #crea una pantalla de ancho 1200 y de alto 800
    pygame.display.set_caption('Juego Invasion de Aliens')  #Pone el nombre del juego a la ventana
 


    ship=Ship(settings,screen,'images/ship.bmp')
    bullets=Group()
    aliens=Group()
    f.crear_flota(settings,screen,ship,aliens)    
    stats=Stats(settings)
    pygame.mixer.music.load('background.wav')   
    pygame.mixer.music.play(-1)   

    boton_play=Boton(settings,screen,'Click aquí para jugar')
    tablero=Tablero(settings,screen,stats)

    while True:
        f.check_eventos(screen,settings,ship,bullets,aliens,stats,boton_play,tablero)
        f.actualiza_screen(screen,settings,ship,bullets,aliens,stats,boton_play,tablero)

 
correr_juego()



