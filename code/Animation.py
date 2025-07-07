import pygame

class Animation:
    def __init__(self, image_paths: list[str], frame_delay: int, pos: tuple, size: tuple):
        # Carrega e redimensiona os frames
        self.frames = [
            pygame.transform.scale(
                pygame.image.load(path).convert_alpha(), size
            )
            for path in image_paths
        ]
        self.current_frame = 0
        self.frame_delay = frame_delay  # ms entre frames
        self.last_update = pygame.time.get_ticks()
        self.pos = pos  # posição (x, y)

    def run(self, screen):
        self.update()
        self.draw(screen)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now

    def draw(self, surface):
        surface.blit(self.frames[self.current_frame], self.pos)
