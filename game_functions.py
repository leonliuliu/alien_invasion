import sys
import pygame

def check_events():
    #响应案件和鼠标移动的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()