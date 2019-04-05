"""
@author HeTongHao
@date 2019/4/4 19:15
@description  游戏方法
"""

import sys
import pygame

from model.bullet import Bullet


def check_events(ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def check_key_down_events(event, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        bullets.add(Bullet(ship))
    elif event.key == pygame.K_q:
        sys.exit()


def check_key_up_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False


def update_screen(settings, bullets, *ships):
    """更新屏幕画面"""
    ships[0].screen.fill(settings.bg_color)  # 重新布置背景
    bullets.update()
    for ship in ships:
        for bullet in bullets.copy():
            if bullet.rect.y < 0:
                bullets.remove(bullet)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.update()
        ship.blitme()
    pygame.display.flip()  # 应用最近生效的窗口变化
