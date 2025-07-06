import pygame

from code.GameScreen import GameScreen
from code.MenuScreen import MenuScreen

menu = MenuScreen()

while True:
    menu_return = menu.run()

    if menu_return == 0:
        GameScreen().run()
    elif menu_return == 1:
        print(1)
    elif menu_return == 2:
        pygame.quit()
        quit()
