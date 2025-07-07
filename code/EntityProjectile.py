from code.Const import WIN_WIDTH, PS_SHOT_SPEED
from code.Entity import Entity


class EntityProjectile(Entity):
    def __init__(self, screen, img_png: str, direction: str, position: tuple, speed: int, health: int, damage_collision: int ):
        super().__init__(screen, img_png, position)
        self.direction = direction
        self.speed = speed
        self.health = health
        self.damage_collision = damage_collision

    def run(self):
        self.draw_entity()
        self.move(self.direction)


    def move(self, direction: str):
        if direction == 'up':
            self.vector_y -= self.speed
        elif direction == 'down':
            self.vector_y += self.speed
        self.position = (self.vector_x, self.vector_y)
