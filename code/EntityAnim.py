import pygame

class EntityAnim:
    def __init__(self, screen, image_path: str, frame_count: int, size: tuple, pos: tuple, speed: int):
        self.screen = screen
        self.pos = list(pos)
        self.speed = speed

        # Carregar frames com redimensionamento
        self.frames = [
            pygame.transform.scale(
                pygame.image.load(f'{image_path}{i}.png').convert_alpha(),
                size
            )
            for i in range(1, frame_count + 1)
        ]

        self.current_frame = 0
        self.frame_delay = 100  # ms
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.pos[1] += self.speed

        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now

    def draw(self):
        self.screen.blit(self.frames[self.current_frame], self.pos)

    def run(self):
        self.update()
        self.draw()
