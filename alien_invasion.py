import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # screen = pygame.display.set_mode((1200,800)) 以上的代码的调用和替换
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    # 创建一艘飞船
    pygame.display.update()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)  # 每次循环都绘制屏幕
        # bg_color = (230,230,230) #背景加上颜色  代码的替换和调用
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
