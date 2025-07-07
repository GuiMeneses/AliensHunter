import random

from code.Const import ALIEN_SPEED_SHOT
from code.Entity import Entity


class AlienShot(Entity):
    def __init__(self, screen, img_png: str, position: tuple):
        super().__init__(screen, img_png, position)
        self.speed = random.randint(ALIEN_SPEED_SHOT[0], ALIEN_SPEED_SHOT[1])

    def run(self):
        self.draw_entity()
        self.move()


    def move(self):
        self.vector_y += self.speed
        self.position = (self.vector_x, self.vector_y)