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
    """
    响应按键和鼠标事件
    :param ship: 飞船
    :param bullets: 子弹组
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship, bullets)


def check_key_down_events(event, ship, bullets):
    """
    检查按键按下时间
    :param event: 事件
    :param ship: 飞船
    :param bullets: 子弹组
    :return:
    """
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        bullets.firing = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_key_up_events(event, ship, bullets):
    """
    检查按键抬起时间
    :param event: 事件
    :param ship: 飞船
    :return:
    """
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_SPACE:
        bullets.firing = False


def create_fleet(settings, screen, aliens):
    """
    创建外星人列表
    :param settings: 设置
    :param screen: 屏幕
    :param aliens: 外星人组
    :return:
    """
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
    # 重新布置背景
    screen.fill(settings.bg_color)
    # 飞船
    update_ship(ship)
    # 子弹
    update_bullets(bullets, ship)
    # 外星人
    update_aliens(aliens, bullets, ship, screen, settings)
    # 应用最近生效的窗口变化
    pygame.display.flip()


def update_ship(ship):
    """
    更新飞船
    :param ship: 飞船
    :return:
    """
    ship.update()
    ship.blitme()


def update_bullets(bullets, ship):
    """
    更新子弹组
    :param bullets: 子弹组
    :return:
    """
    # 有开火属性并且正在开火，生成子弹
    if hasattr(bullets, 'firing') and bullets.firing:
        bullets.add(Bullet(ship))
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.y < 0:
            bullets.remove(bullet)
    for bullet in bullets:
        bullet.draw_bullet()


def update_aliens(aliens, bullets, ship, screen, settings):
    """
    更新外星人组
    :param aliens: 外星人组
    :param bullets: 子弹组
    :param ship: 飞船
    :param screen: 屏幕
    :param settings: 全局设置
    :return:
    """
    aliens.update()
    for alien in aliens:
        alien.blitme()
    pygame.sprite.groupcollide(aliens, bullets, True, True)
    if len(aliens) == 0:
        create_fleet(settings, screen, aliens)
    if pygame.sprite.spritecollideany(ship, aliens):
        for bullet in bullets.copy():
            bullets.remove(bullet)
        for alien in aliens.copy():
            aliens.remove(alien)
        ship.__init__(screen)
