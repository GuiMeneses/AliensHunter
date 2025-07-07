import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Animation import Animation
from code.BgMediator import BgMediator
from code.Const import WIN_WIDTH, WIN_HEIGHT, SOUND_GAME_VOLUME, C_YELLOW1, C_GREY, C_BLUE, C_RED, \
    PS_SUBTRACT_ENERGY, SOUND_SHOT_VOLUME, SOUND_EXPLOSION, SOUND_HURT_VOLUME
from code.EntityMediator import EntityMediator
from code.EntityPlayer import EntityPlayer
from code.PlayerStatus import PlayerStatus
from code.SpawnManager import SpawnManager


class GameScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        ps = PlayerStatus()
        player = EntityPlayer(self.screen, './Assets/Player_ship.png', (WIN_WIDTH / 2 - 24, WIN_HEIGHT / 2))

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('./Assets/Sounds/sound1.mp3')
        pygame.mixer.music.set_volume(SOUND_GAME_VOLUME)
        pygame.mixer.music.play(-1)

        sound_shot = pygame.mixer.Sound('./Assets/Sounds/effects/laser.mp3')
        sound_shot.set_volume(SOUND_SHOT_VOLUME)
        sound_explosion = pygame.mixer.Sound('./Assets/Sounds/effects/explosion.mp3')
        sound_explosion.set_volume(SOUND_EXPLOSION)
        sound_hurt = pygame.mixer.Sound('./Assets/Sounds/effects/hurt.mp3')
        sound_hurt.set_volume(SOUND_HURT_VOLUME)

        clock = pygame.time.Clock()
        bg_med = BgMediator(self.screen)
        entity_med = EntityMediator(self.screen, sound_explosion, sound_hurt, player, ps)
        spawn_manager = SpawnManager(self.screen)




        list_player_shoot = []
        list_entity = []
        list_animation = []

        while True:
            clock.tick(60)
            self.screen.fill((0, 0, 0))
            bg_med.run()
            entity_med.run([list_player_shoot, list_entity], ps, list_animation)
            spawn_manager.run(list_entity)

            ps.timer()

            for i in range(len(list_player_shoot)):
                if len(list_player_shoot) != 0:
                    list_player_shoot[i].run()

            for i in range(len(list_entity)):
                if len(list_entity) != 0:
                    list_entity[i].run()

            for i in range(len(list_animation)):
                if len(list_animation) != 0:
                    list_animation[i].run(self.screen)

            player.run(list_player_shoot, ps, sound_shot)

            self.drawn_icon('./Assets/storm.png', (8, 5))
            self.drawn_icon('./Assets/heart.png', (5, 25))

            pygame.draw.rect(self.screen, C_GREY, (45, 15, 400, 6))
            pygame.draw.rect(self.screen, C_BLUE, (45, 15, ps.energy, 6))
            ps.subtract_energy(PS_SUBTRACT_ENERGY)

            pygame.draw.rect(self.screen, C_GREY, (45, 25, 400, 18))
            pygame.draw.rect(self.screen, C_RED, (45, 25, ps.health, 18))

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
