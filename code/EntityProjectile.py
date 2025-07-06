from code.Const import WIN_WIDTH, PS_SHOT_SPEED
from code.Entity import Entity


class EntityProjectile(Entity):
    def __init__(self, screen, img_png: str, direction: str, position: tuple):
        super().__init__(screen, img_png, position)
        self.direction = direction

    def run(self):
        self.draw_entity()
        self.move(self.direction)


    def move(self, direction: str):
        if direction == 'up':
            self.vector_y -= PS_SHOT_SPEED
        elif direction == 'down':
            self.vector_y += PS_SHOT_SPEED
        self.position = (self.vector_x, self.vector_y)
