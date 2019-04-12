"""
游戏主函数
@author HeTongHao
@date 2019/4/4 09:53
@description  
"""
from time import sleep

import pygame
from pygame.sprite import Group

import game_functions as gf
from model.ship import Ship
from settings import Settings

if __name__ == '__main__':
    pygame.init()
    # 设置对象
    settings = Settings()
    # 游戏标题
    pygame.display.set_caption(settings.sys_title)
    # 屏幕高宽
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # ✈️飞船
    ship = Ship(screen)
    # 子弹组
    bullets = Group()
    # 👽外星人组
    aliens = Group()
    # 游戏主循环
    while True:
        # 检查飞船碰撞
        is_crash = gf.check_collision(ship, aliens, bullets)
        # 更新屏幕
        gf.update_screen(screen, settings, ship, bullets, aliens)
        # 检查事件
        gf.check_events(ship, bullets)
        if is_crash:
            sleep(0.5)
