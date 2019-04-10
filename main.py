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

pygame.init()
settings = Settings()  # 设置
pygame.display.set_caption(settings.sys_title)
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
screen_rect = screen.get_rect()
ship = Ship(screen)
bullets = Group()
aliens = Group()
while True:
    # 检查事件
    gf.check_events(ship, bullets)
    # 更新屏幕
    gf.update_screen(screen, settings, ship, bullets, aliens)
