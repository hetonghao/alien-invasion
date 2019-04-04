"""
@author HeTongHao
@date 2019/4/4 18:51
@description  
"""

import pygame
from .object import Object


class Alien(Object):

    def __init__(self, screen, moving_speed=5):
        super().__init__(screen, moving_speed)
        self.ship_img = pygame.image.load('images/juanfu.jpg')
        self.rect = self.ship_img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
