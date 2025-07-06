import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WHITE, C_YELLOW1, SOUND_VOLUME, C_YELLOW2, C_YELLOW3, KP_DOWN, KP_UP
from code.Mediator import Mediator


class MenuScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./Assets/Sounds/menu.mp3')
        pygame.mixer.music.set_volume(SOUND_VOLUME)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        med = Mediator(self.screen)

        menu_option = 0

        while True:
            clock.tick(60)
            pygame.init()

            self.screen.fill((0, 0, 0))
            med.bg()

            self.menu_text(80, 'Aliens Hunter', C_YELLOW1, (WIN_WIDTH / 2, 220))
            self.menu_text(40, 'Play', C_YELLOW2, (WIN_WIDTH / 2, 450))
            self.menu_text(40, 'Score', C_YELLOW2, (WIN_WIDTH / 2, 530))
            self.menu_text(40, 'Exit', C_YELLOW2, (WIN_WIDTH / 2, 610))

            if menu_option == 0:
                self.menu_text(40, 'Play', C_YELLOW3, (WIN_WIDTH / 2, 450))
            elif menu_option == 1:
                self.menu_text(40, 'Score', C_YELLOW3, (WIN_WIDTH / 2, 530))
            elif menu_option == 2:
                self.menu_text(40, 'Exit', C_YELLOW3, (WIN_WIDTH / 2, 610))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == KP_DOWN:
                        menu_option += 1
                        if menu_option == 3:
                            menu_option = 0

                    elif event.key == KP_UP:
                        menu_option -= 1
                        if menu_option == -1:
                            menu_option = 2

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./Assets/Joystixmonospace.otf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)
