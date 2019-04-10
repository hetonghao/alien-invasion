"""
@author HeTongHao
@date 2019/4/4 18:51
@description  
"""

import pygame
from .object import Object
from pygame.sprite import Sprite


class Alien(Object, Sprite):

    def __init__(self, screen, moving_speed=2):
        super().__init__(screen, moving_speed)
        super(Object, self).__init__()
        self.ship_img = pygame.image.load('images/juanfu.jpg')
        self.rect = self.ship_img.get_rect()
        self.rect.centerx = self.rect.width
        self.moving_right = True
        self.moving_down = True

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.moving_speed * 2
            if self.screen_rect.right - self.rect.right <= self.moving_speed * 2:
                self.moving_right = False
                self.moving_left = True
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.moving_speed * 2
            if self.rect.left <= self.moving_speed * 2:
                self.moving_left = False
                self.moving_right = True
        self.rect.centery += self.moving_speed / 2
