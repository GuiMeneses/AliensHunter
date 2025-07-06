import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.BgMediator import BgMediator
from code.Const import WIN_WIDTH, WIN_HEIGHT, SOUND_GAME_VOLUME, C_YELLOW1, C_GREY, C_BLUE, C_RED, \
    PS_SUBTRACT_ENERGY
from code.EntityPlayer import EntityPlayer
from code.EntityProjectile import EntityProjectile
from code.PlayerStatus import PlayerStatus


class GameScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('./Assets/Sounds/sound1.mp3')
        pygame.mixer.music.set_volume(SOUND_GAME_VOLUME)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        med = BgMediator(self.screen)

        ps = PlayerStatus()

        player = EntityPlayer(self.screen, './Assets/Player_ship.png', (WIN_WIDTH / 2, WIN_HEIGHT / 2))
        list_pj = []

        while True:
            clock.tick(60)
            self.screen.fill((0, 0, 0))
            med.run()

            ps.timer()

            for i in range(len(list_pj)):
                if len(list_pj) != 0:
                    list_pj[i].run()

            player.run(list_pj)

            self.drawn_icon('./Assets/storm.png', (8, 5))
            self.drawn_icon('./Assets/heart.png', (5, 25))

            pygame.draw.rect(self.screen, C_GREY, (45, 15, 400, 6))
            pygame.draw.rect(self.screen, C_BLUE, (45, 15, ps.energy, 6))
            ps.subtract_energy(PS_SUBTRACT_ENERGY)

            pygame.draw.rect(self.screen, C_GREY, (45, 25, 400, 18))
            pygame.draw.rect(self.screen, C_RED, (45, 25, ps.heath, 18))

            self.game_text(40, ps.time, C_YELLOW1, (WIN_WIDTH - 180, 5))
            self.game_text(40, str(ps.score), C_YELLOW1, (10, 50))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def drawn_icon(self, img_png: str, position: tuple):
        surf = pygame.image.load(img_png).convert_alpha(self.screen)
        rect = surf.get_rect(left=position[0], top=position[1])
        self.screen.blit(surf, rect)

    def game_text(self, text_size: int, text: str, text_color: tuple, text_top_left_pos: tuple):
        text_font: Font = pygame.font.Font("./Assets/JoystixMonoSpace.otf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_top_left_pos)
        self.screen.blit(source=text_surf, dest=text_rect)
