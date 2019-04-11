"""
子弹
@author HeTongHao
@date 2019/4/4 23:31
@description  
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ship):
        super().__init__()
        self.screen = ship.screen
        self.rect = pygame.Rect(0, 0, 2, 8)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color = (99, 60, 60)
        self.speed_factor = 6

    def update(self):
        self.rect.y -= self.speed_factor

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
