"""
游戏可移动对象基类
@author HeTongHao
@date 2019/4/4 20:28
@description  
"""
import pygame


class Object:

    def __init__(self, screen, moving_speed=0):
        self.img = None
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.screen_rect = screen.get_rect()
        # 移动状态初始化
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.moving_speed = moving_speed

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.moving_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.moving_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.moving_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.moving_speed

    def blitme(self):
        self.screen.blit(self.img, self.rect)
