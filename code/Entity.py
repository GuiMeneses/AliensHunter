from abc import ABC

import pygame

from code.Const import ENTITY_HEALTH, ENTITY_COLLISION_DAMAGE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./Assets/'+self.name+'.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.collision_damage = ENTITY_COLLISION_DAMAGE[self.name]

    
