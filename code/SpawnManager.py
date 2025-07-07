import pygame

from code.Const import ENT_METEOR_HEALTH, SPAWN_RATE
from code.Entity import Entity
from code.EntityProjectile import EntityProjectile
from code.MyTimer import MyTimer


class SpawnManager:
    def __init__(self, screen):
        self.timer_spawn_rate = MyTimer(SPAWN_RATE)
        self.screen = screen
        self.spawned: list[Entity] = []

        self.slot_spawn: list[tuple] = []
        for i in range(9):
            self.slot_spawn.append((i * 120, -100))

    def run(self, list_entity: list[Entity]):
        self.factory_spawn(list_entity)
        self.timer_spawn_rate.run()

    def factory_spawn(self, list_entity: list[Entity]):
        if self.timer_spawn_rate.seconds >= SPAWN_RATE:
            self.timer_spawn_rate.start_time = pygame.time.get_ticks()
            self.spawn_obg('Alien_ship', 1 , list_entity, self.slot_spawn[0])
            self.spawn_obg('meteor', 1 , list_entity, self.slot_spawn[1])
            self.spawn_obg('meteor', 1 , list_entity, self.slot_spawn[2])
            self.spawn_obg('meteor', 1 , list_entity, self.slot_spawn[3])
            self.spawn_obg('meteor', 2 , list_entity, self.slot_spawn[4])
            self.spawn_obg('meteor', 2 , list_entity, self.slot_spawn[5])
            self.spawn_obg('meteor', 2 , list_entity, self.slot_spawn[6])
            self.spawn_obg('meteor', 2 , list_entity, self.slot_spawn[7])
            self.spawn_obg('meteor', 2 , list_entity, self.slot_spawn[8])

    def spawn_obg(self, img_png: str, speed: int, list_entity: list[Entity], slot_spawn):
        obg = EntityProjectile(self.screen, f'./Assets/{img_png}.png', 'down', (slot_spawn[0] + 36, slot_spawn[1]),
                                   speed,
                                   ENT_METEOR_HEALTH)
        list_entity.append(obg)








