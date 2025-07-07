import pygame

from code.Const import ENT_METEOR_DAMAGE_COLLISION, ENT_METEOR_HEALTH, SPAWN_RATE
from code.Entity import Entity
from code.EntityProjectile import EntityProjectile


class SpawnManager:
    def __init__(self, screen):
        self.screen = screen
        self.start_time = pygame.time.get_ticks()
        self.seconds = SPAWN_RATE
        self.spawned: list[Entity] = []

        self.slot_spawn: list[tuple] = []
        for i in range(9):
            self.slot_spawn.append((i * 120, -100))

    def run(self, list_entity: list[Entity]):
        self.factory_spawn(list_entity)
        self.timer()

    def timer(self):
        elapsed_ms = pygame.time.get_ticks() - self.start_time
        elapsed_sec = elapsed_ms / 1000
        self.seconds = round(elapsed_sec % 60, 2)

    def factory_spawn(self, list_entity: list[Entity]):
        if self.seconds >= SPAWN_RATE:
            self.start_time = pygame.time.get_ticks()
            self.spawn_meteor(list_entity,self.slot_spawn[0])
            self.spawn_meteor(list_entity,self.slot_spawn[1])
            self.spawn_meteor(list_entity,self.slot_spawn[2])
            self.spawn_meteor(list_entity,self.slot_spawn[3])
            self.spawn_meteor(list_entity,self.slot_spawn[4])
            self.spawn_meteor(list_entity,self.slot_spawn[5])
            self.spawn_meteor(list_entity,self.slot_spawn[6])
            self.spawn_meteor(list_entity,self.slot_spawn[7])
            self.spawn_meteor(list_entity,self.slot_spawn[8])

    def spawn_meteor(self, list_entity: list[Entity], slot_spawn):
        meteor = EntityProjectile(self.screen, './Assets/meteor.png', 'down', tuple(sum(x) for x in zip(slot_spawn, (36, 0))), 2, ENT_METEOR_HEALTH, ENT_METEOR_DAMAGE_COLLISION)
        list_entity.append(meteor)
