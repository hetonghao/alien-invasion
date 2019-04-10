"""
@author HeTongHao
@date 2019/4/4 19:15
@description  游戏方法
"""

import sys
import pygame

from model.bullet import Bullet
from model.alien import Alien


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


def create_fleet(settings, screen, aliens):
    alien = Alien(screen)
    span = 10
    row_alien_number = int(settings.screen_width / (alien.rect.width + span * 2))
    index_span = 0
    for i in range(row_alien_number):
        alien = Alien(screen)
        alien.rect.left = index_span + span
        index_span = alien.rect.right
        aliens.add(alien)


def update_screen(screen, settings, ship, bullets, aliens):
    """
    更新屏幕画面
    :param screen: 屏幕
    :param settings: 全局设置
    :param ship: 飞机
    :param bullets: 子弹组
    :param aliens: 外星人组
    :return:
    """
    screen.fill(settings.bg_color)  # 重新布置背景
    # 飞船
    ship.update()
    ship.blitme()
    # 子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.y < 0:
            bullets.remove(bullet)
    for bullet in bullets:
        bullet.draw_bullet()
    # 外星人
    aliens.update()
    for alien in aliens:
        alien.blitme()
    pygame.sprite.groupcollide(aliens, bullets, True, False)
    if len(aliens) == 0:
        create_fleet(settings, screen, aliens)
    pygame.sprite.spritecollide(ship, aliens, True, False)
    # 应用最近生效的窗口变化
    pygame.display.flip()
