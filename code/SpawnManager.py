import pygame

from code.Const import ENT_METEOR_HEALTH, SPAWN_RATE, ENT_ALIEN_HEALTH
from code.Entity import Entity
from code.EntityAnim import EntityAnim
from code.EntityProjectile import EntityProjectile
from code.MyTimer import MyTimer

import random

class SpawnManager:
    def __init__(self, screen, ps):
        self.timer_spawn_rate = MyTimer(SPAWN_RATE)
        self.screen = screen
        self.ps = ps

        self.slot_spawn: list[tuple] = []
        for i in range(9):
            self.slot_spawn.append((i * 120, -100))

        self.energy_spawned_300 = False
        self.energy_spawned_200 = False
        self.energy_spawned_100 = False

    def run(self, list_entity: list[Entity], list_energy):
        self.factory_spawn(list_entity, list_energy)
        self.timer_spawn_rate.run()

    def factory_spawn(self, list_entity: list[Entity], list_energy):
        if self.timer_spawn_rate.seconds >= SPAWN_RATE:
            self.timer_spawn_rate.start_time = pygame.time.get_ticks()

            slot_energy = random.choice(self.slot_spawn)

            for slot in self.slot_spawn:
                if slot == slot_energy:
                    if self.ps.energy >= 300:
                        self.energy_spawned_300 = False
                    if self.ps.energy >= 200:
                        self.energy_spawned_200 = False
                    if self.ps.energy >= 100:
                        self.energy_spawned_100 = False

                    if self.ps.energy < 300 and not self.energy_spawned_300:
                        self.spawn_energy(120, 2, list_energy, slot)
                        self.energy_spawned_300 = True
                        continue

                    elif self.ps.energy < 200 and not self.energy_spawned_200:
                        self.spawn_energy(120, 2, list_energy, slot)
                        self.energy_spawned_200 = True
                        continue

                    elif self.ps.energy < 100 and not self.energy_spawned_100:
                        self.spawn_energy(120, 2, list_energy, slot)
                        self.energy_spawned_100 = True
                        continue

                rand = random.random()
                if rand < 0.7:
                    self.spawn_obg('Alien_ship', random.randint(1, 2), list_entity, slot)
                elif rand < 0.9:
                    self.spawn_obg('meteor', random.randint(1, 2), list_entity, slot)

    def spawn_obg(self, img_png: str, speed: int, list_entity: list[Entity], slot_spawn):
        if img_png == 'meteor':
            obg = EntityProjectile(
                self.screen,
                f'./Assets/{img_png}.png',
                'down',
                (slot_spawn[0] + 36, slot_spawn[1]),
                speed,
                ENT_METEOR_HEALTH
            )
        else:
            obg = EntityProjectile(
                self.screen,
                f'./Assets/{img_png}.png',
                'down',
                (slot_spawn[0] + 36, slot_spawn[1]),
                speed,
                ENT_ALIEN_HEALTH
            )
        list_entity.append(obg)

    def spawn_energy(self, size: int, speed: int, list_entity: list[EntityAnim], slot_spawn):
        obg = EntityAnim(
            self.screen,
            './Assets/Energy_',
            9,
            (size, size),
            (slot_spawn[0], slot_spawn[1]),
            speed
        )
        list_entity.append(obg)
