import pygame

class Animation:
    def __init__(self, image_paths: str, frame_delay: int, pos: tuple, size: tuple, loop: bool):
        self.loop = loop
        self.frames = [
            pygame.transform.scale(
                pygame.image.load(path).convert_alpha(), size
            )
            for path in [f'{image_paths}{i}.png' for i in range(1, 10)]
        ]
        self.current_frame = 0
        self.frame_delay = frame_delay
        self.last_update = pygame.time.get_ticks()
        self.pos = pos


    def run(self, screen):
        self.update()
        self.draw(screen)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_delay:
            if self.loop:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.last_update = now
            else:
                self.current_frame = (self.current_frame + 1)
                self.last_update = now



    def draw(self, surface):
        if self.loop:
            surface.blit(self.frames[self.current_frame], self.pos)
        else:
            if self.current_frame < len(self.frames):
                surface.blit(self.frames[self.current_frame], self.pos)
