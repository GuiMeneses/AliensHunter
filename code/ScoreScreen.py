import sqlite3
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.BgMediator import BgMediator
from code.Const import WIN_WIDTH, WIN_HEIGHT, SOUND_MENU_VOLUME, SOUND_MENU_BUTTON, C_YELLOW1


class ScoreScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

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

        # 🔽 Busca do banco SQLite
        conn = sqlite3.connect('jogo.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT nick, score, time
            FROM score_data
            ORDER BY score DESC
            LIMIT 10
        ''')
        list_top_10 = cursor.fetchall()
        conn.close()

        # Se não tiver 10, completa com dummy
        while len(list_top_10) < 10:
            list_top_10.append(('----', 0, '00:00'))

        while True:
            clock.tick(60)

            self.screen.fill((0, 0, 0))
            med.run()

            self.menu_text(70, 'top 10 score list', C_YELLOW1, (WIN_WIDTH / 2, 60))
            self.menu_topl(40, 'nick', C_YELLOW1, (150, 120))
            self.menu_topl(40, 'score', C_YELLOW1, (380, 120))
            self.menu_topl(40, 'time', C_YELLOW1, (830, 120))

            for player in range(len(list_top_10)):
                if player > 8:
                    self.menu_topl(40, f'{player + 1}. {list_top_10[player][0]} ', C_YELLOW1, (15, 180 + 60 * player))
                else:
                    self.menu_topl(40, f'{player + 1}. {list_top_10[player][0]} ', C_YELLOW1, (50, 180 + 60 * player))
                self.menu_topl(40, f'{list_top_10[player][1]} ', C_YELLOW1, (380, 180 + 60 * player))
                self.menu_topl(40, f'{list_top_10[player][2]} ', C_YELLOW1, (830, 180 + 60 * player))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

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
