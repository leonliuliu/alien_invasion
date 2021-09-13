import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


    # 创建新子弹并将其加入编组bullets中

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    # 响应松开
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    # 响应案件和鼠标移动的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # 更新屏幕的图像，并切换到新的屏幕中
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 造飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最新的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """"更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """"计算每行可容纳多少哥外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    """"创建一个外星儿并将其放在前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """"创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    # 外星人的间距为外星人的宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    # 创建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)
