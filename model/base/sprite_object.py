"""
可创建精灵组的可移动对象基类
@author HeTongHao
@date 2019/4/12 10:28
@description  
"""
from pygame.sprite import Sprite

from model.base.object import Object


class SpriteObject(Object, Sprite):

    def __init__(self, screen, img_address=None, moving_speed=0):
        super().__init__(screen, img_address, moving_speed)
        super(Object, self).__init__()
