import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,settings,screen,path_image):
        super().__init__()
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.settings=settings


        self.image=pygame.image.load(path_image)
        self.rect=self.image.get_rect()


        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.x=self.rect.centerx

        self.right_move=False #establece movimiento a la derecha
        self.left_move=False


    def dibujar_ship(self):
        self.screen.blit(self.image,self.rect)  #dibuja la imagen en la screen en la posicion indicada por el rectangulo

    def mov_continuo(self):
        if self.right_move:
            if (self.x+self.rect.width/2) <=self.screen_rect.width:
                self.x+=self.settings.ship_speed_factor
                self.rect.centerx=self.x
        if self.left_move:
            if (self.x-self.rect.width/2)>=0:
                self.x-=self.settings.ship_speed_factor
                self.rect.centerx=self.x

    def center_ship(self):
        self.rect.centerx=self.screen_rect.centerx




