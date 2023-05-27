import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,settings,screen,ship):
        super().__init__()
        self.settings=settings
        self.screen=screen
        self.ship=ship
        self.color=settings.bullet_color
        self.speed_factor=settings.bullet_speed_factor

        self.rect=pygame.Rect(0,0,settings.bullet_width,settings.bullet_height) #se crea rectangulo
        self.rect.centerx=ship.rect.centerx
        self.rect.bottom=ship.rect.top
        self.y=self.rect.y

    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y

    def dibujar_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)




