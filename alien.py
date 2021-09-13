import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人菜菜并设置启动位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人 菜菜图像，并设置rect属性
        self.image = pygame.image.load('images/caicai.bmp')
        self.rect = self.image.get_rect()

        #  每个外星人最初都出现在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的位置
        self.x = float(self.rect.x)

    def blitme(self):
        """ 在指定地方绘制外星人菜菜"""
        self.screen.blit(self.image, self.rect)
