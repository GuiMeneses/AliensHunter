import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.BgMediator import BgMediator
from code.Const import WIN_WIDTH, WIN_HEIGHT, SOUND_MENU_VOLUME, SOUND_MENU_BUTTON, C_RED2
from code.MenuScreen import MenuScreen


class GameOverScreen:
    def __init__(self, score, time):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.score = score
        self.time = time

    def run(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('./Assets/Sounds/menu.mp3')
        pygame.mixer.music.set_volume(SOUND_MENU_VOLUME)
        pygame.mixer.music.play(-1)

        sound_button = pygame.mixer.Sound('./Assets/Sounds/effects/hurt.mp3')
        sound_button.set_volume(SOUND_MENU_BUTTON)

        clock = pygame.time.Clock()
        med = BgMediator(self.screen)

        nick = ''
        max_length = 4


        while True:
            clock.tick(60)

            self.screen.fill((0, 0, 0))
            med.run()

            self.menu_text(80, 'GAME OVER', C_RED2, (WIN_WIDTH / 2, 220))
            self.menu_text(15, 'You lose', C_RED2, (WIN_WIDTH / 2 , 270))
            self.menu_text(30, f'Score: {self.score}', C_RED2, (WIN_WIDTH / 2 , 380))
            self.menu_text(30, f'Time: ({self.time})', C_RED2, (WIN_WIDTH / 2 , 410))
            self.menu_text(30, 'Write your nick', C_RED2, (WIN_WIDTH / 2 , 440))
            self.menu_text(150, '____', C_RED2, (WIN_WIDTH / 2 , 550))
            self.menu_topl(150, nick, C_RED2, (292 , 450))





            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        nick = nick[:-1]
                    elif len(nick) < max_length:
                        if event.unicode.isalpha():
                            nick += event.unicode.upper()
                    elif event.key == pygame.K_RETURN and len(nick) == max_length:
                        return nick




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./Assets/JoystixMonoSpace.otf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)

    def menu_topl(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./Assets/JoystixMonoSpace.otf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)
