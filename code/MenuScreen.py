import pygame

from code.Screen import Screen


class MenuScreen(Screen):
    def __init__(self):
        super().__init__()


    def run(self):
        pygame.init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End Pygame
            pass


