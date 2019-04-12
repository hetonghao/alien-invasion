"""
外星人👽
@author HeTongHao
@date 2019/4/4 18:51
@description  
"""

from model.base.sprite_object import SpriteObject


class Alien(SpriteObject):

    def __init__(self, screen, moving_speed=2):
        super().__init__(screen, 'images/juan_fu.jpg', moving_speed)
        self.rect.centerx = self.rect.width
        self.moving_right = True
        self.moving_down = True

    def update(self):
        """
        更新位置
        :return:
        """
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
