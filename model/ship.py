"""
@author HeTongHao
@date 2019/4/4 18:51
@description  
"""

import pygame
from .object import Object
from pygame.sprite import Sprite


class Ship(Object, Sprite):

    def __init__(self, screen, moving_speed=5):
        super().__init__(screen, moving_speed)
        super(Object, self).__init__()
        self.ship_img = pygame.image.load('images/ship.jpg')
        self.rect = self.ship_img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
