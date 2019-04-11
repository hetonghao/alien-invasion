"""
飞船
@author HeTongHao
@date 2019/4/4 18:51
@description  
"""

import pygame
from .object import Object


class Ship(Object):

    def __init__(self, screen, moving_speed=5):
        super().__init__(screen, moving_speed)
        super(Object, self).__init__()
        self.img = pygame.image.load('images/ship.jpg')
        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
