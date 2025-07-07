import random

import pygame

from code.AlienShot import AlienShot
from code.Const import WIN_WIDTH, PS_SHOT_SPEED, ALIEN_FIRE_RATE, WIN_HEIGHT
from code.Entity import Entity
from code.MyTimer import MyTimer


class EntityProjectile(Entity):
    def __init__(self, screen, img_png: str, direction: str, position: tuple, speed: int, health: int,
                 damage_collision: int = None):
        super().__init__(screen, img_png, position)
        self.direction = direction
        self.speed = speed
        self.health = health
        self.damage_collision = damage_collision
        self.shot: list[AlienShot] = []
        self.timer_alien_shot = MyTimer(ALIEN_FIRE_RATE)

    def run(self):
        if self.img_png == './Assets/Alien_ship.png':
            self.timer_alien_shot.run()
            if len(self.shot) > 0:
                for shot in self.shot:
                    shot.run()
                    self.verify_alien_shot_in_window(shot, self.shot)
                    print(len(self.shot))

            if self.timer_alien_shot.seconds >= ALIEN_FIRE_RATE:
                self.timer_alien_shot.start_time = pygame.time.get_ticks()
                shot = AlienShot(self.screen, './Assets/Alien_shot.png', (self.position[0] + 17, self.position[1]))
                self.shot.append(shot)
        self.draw_entity()
        self.move(self.direction)

    def move(self, direction: str):
        if direction == 'up':
            self.vector_y -= self.speed
        elif direction == 'down':
            self.vector_y += self.speed
        self.position = (self.vector_x, self.vector_y)

    def verify_alien_shot_in_window(self, alien_shot: AlienShot, list_alien_shot: list[AlienShot]):
        if alien_shot.rect.top > WIN_HEIGHT:
            list_alien_shot.remove(alien_shot)
