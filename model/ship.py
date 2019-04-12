"""
飞船
@author HeTongHao
@date 2019/4/4 18:51
@description  
"""

from model.base.object import Object


class Ship(Object):

    def __init__(self, screen, moving_speed=5):
        super().__init__(screen, 'images/ship.jpg', moving_speed)
        self.init_position()

    def init_position(self):
        """
        初始化飞船位置
        :return:
        """
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
