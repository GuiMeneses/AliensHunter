import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, PS_SPEED, P_KEY_UP, P_KEY_RIGHT, P_KEY_DOWN, P_KEY_LEFT, P_KEY_SHOT
from code.Entity import Entity
from code.EntityProjectile import EntityProjectile


class EntityPlayer(Entity):
    def __init__(self, screen, img_png: str, position: tuple):
        super().__init__(screen, img_png, position)

    def run(self, list_pj):
        self.draw_entity()
        self.move(P_KEY_UP, P_KEY_RIGHT, P_KEY_DOWN, P_KEY_LEFT)
        self.shot(list_pj)

    def move(self, key_up, key_right, key_down, key_left):
        keys = pygame.key.get_pressed()
        if keys[key_up]:
            self.vector_y -= 1 * PS_SPEED
        if keys[key_down]:
            self.vector_y += 1 * PS_SPEED
        if keys[key_right]:
            self.vector_x += 1 * PS_SPEED
        if keys[key_left]:
            self.vector_x -= 1 * PS_SPEED

        if self.vector_y < 0:
            self.vector_y = 0
        elif self.vector_y > WIN_HEIGHT - 49:
            self.vector_y = WIN_HEIGHT - 49
        if self.vector_x > WIN_WIDTH - 49:
            self.vector_x = WIN_WIDTH - 49
        elif self.vector_x < 0:
            self.vector_x = 0

        self.position = (self.vector_x, self.vector_y)

    def shot(self, list_pj: list[EntityProjectile]):
        keys = pygame.key.get_pressed()
        if keys[P_KEY_SHOT]:
            pj = EntityProjectile(self.screen, './Assets/Player_shot.png', 'up', (self.position[0] + 16, self.position[1]))
            list_pj.append(pj)
            print(len(list_pj))





