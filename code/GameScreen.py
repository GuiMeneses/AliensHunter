import sys
from tokenize import String
from xml.etree.ElementTree import tostring

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, SOUND_MENU_VOLUME, SOUND_GAME_VOLUME, C_YELLOW1, C_GREY, C_BLUE, C_RED
from code.BgMediator import BgMediator
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



        while True:
            clock.tick(60)
            self.screen.fill((0, 0, 0))
            med.run()

            ps.timer()


            self.drawn_icon('./Assets/storm.png', (8,5))
            self.drawn_icon('./Assets/heart.png', (5,25))

            pygame.draw.rect(self.screen, C_GREY, (45,15,400,6))
            pygame.draw.rect(self.screen, C_BLUE, (45,15,ps.energy,6))
            ps.subtract_energy(0.2)


            pygame.draw.rect(self.screen, C_GREY, (45,25,400,18))
            pygame.draw.rect(self.screen, C_RED, (45,25,ps.heath,18))

            self.game_text(40, ps.time , C_YELLOW1, (WIN_WIDTH - 180, 5))
            self.game_text(40, str(ps.score) , C_YELLOW1, (10, 50))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        ps.add_energy(50)


    def drawn_icon(self, img_png: str, position: tuple):
        surf = pygame.image.load(img_png).convert_alpha(self.screen)
        rect = surf.get_rect(left=position[0], top=position[1])
        self.screen.blit(surf, rect)

    def game_text(self, text_size: int, text: str, text_color: tuple, text_topleft_pos: tuple):
        text_font: Font = pygame.font.Font("./Assets/Joystixmonospace.otf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(topleft=text_topleft_pos)
        self.screen.blit(source=text_surf, dest=text_rect)
