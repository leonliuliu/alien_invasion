import pygame


class Ship():

    def __init__(self, screen):
        # 初始化飞船并设置其的初始位置
        self.screen = screen

        # 加载飞船图像并获取其外接矩图
        self.image = pygame.image.load('images/ship.bmp')  # 调用加载的图片
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个新飞船放在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # 在指定的地方绘制飞船
        self.screen.blit(self.image, self.rect)
