"""
@author HeTongHao
@date 2019/4/4 19:15
@description  游戏方法
"""

import sys

import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.moving_up = True if event.type == pygame.KEYDOWN else False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True if event.type == pygame.KEYDOWN else False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True if event.type == pygame.KEYDOWN else False
            elif event.key == pygame.K_RIGHT:
                ship.moving_right = True if event.type == pygame.KEYDOWN else False


def update_screen(settings, *ships):
    """更新屏幕画面"""
    ships[0].screen.fill(settings.bg_color)  # 重新布置背景
    for ship in ships:
        ship.update()
        ship.blitme()
    pygame.display.flip()  # 应用最近生效的窗口变化
