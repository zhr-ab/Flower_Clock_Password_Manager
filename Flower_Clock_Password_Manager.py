import pgzrun
import pygame

# 设置窗口宽高
WIDTH = 1000
HEIGHT = 600

# 设置窗口标题
TITLE = "Flower Clock Password Manager"
def update():
    # 设置窗口图标
    icon = pygame.image.load(r"images\Flower_Clock_Password_Manager.ico")
    pygame.display.set_icon(icon)

def draw():
    screen.clear()

pgzrun.go()
