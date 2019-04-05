"""
@author HeTongHao
@date 2019/4/4 09:53
@description  
"""
import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from model.ship import Ship
from model.alien import Alien

pygame.init()
settings = Settings()  # 设置
pygame.display.set_caption(settings.sys_title)
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
screen_rect = screen.get_rect()
ship = Ship(screen)
alien = Alien(screen)
bullets = Group()
while True:
    gf.check_events(ship, bullets)
    gf.update_screen(settings, bullets, ship, alien)
