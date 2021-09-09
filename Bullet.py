import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """这是一个对飞船子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        # 在飞船的位置创建一个子弹对象
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0，0）处创建一个表示子弹的矩形，在设置正确的地方
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        # 这里的centerx是为了确定子弹是从飞机的位置射出
        self.rect.top = ship.rect.top
        # 这里的top就是为了让子弹是从飞机的头部射出而设置

        # 存储用小数点表示子弹的位置
        self.y = float(self.rect.y)
        # 以下就设置了子弹的颜色和速度的储存位置
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 为了更新子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
