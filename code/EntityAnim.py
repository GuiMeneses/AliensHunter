import pygame

class EntityAnim:
    def __init__(self, screen, image_path: str, frame_count: int, size: tuple, position: tuple, speed: int):
        self.screen = screen
        self.position = list(position)
        self.speed = speed

        self.width, self.height = size

        self.frames = [
            pygame.transform.scale(
                pygame.image.load(f'{image_path}{i}.png').convert_alpha(),
                size
            )
            for i in range(1, frame_count + 1)
        ]

        self.current_frame = 0
        self.frame_delay = 100
        self.last_update = pygame.time.get_ticks()

        # Cria rect menor e centralizado
        rect_w = self.width // 2
        rect_h = self.height // 2
        rect_x = self.position[0] + (self.width - rect_w) // 2
        rect_y = self.position[1] + (self.height - rect_h) // 2
        self.rect = pygame.Rect(rect_x, rect_y, rect_w, rect_h)

    def update(self):
        self.position[1] += self.speed

        # Atualiza rect para nova posição, mantendo centralizado
        rect_w = self.width // 2
        rect_h = self.height // 2
        rect_x = self.position[0] + (self.width - rect_w) // 2
        rect_y = self.position[1] + (self.height - rect_h) // 2
        self.rect.topleft = (rect_x, rect_y)

        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now

    def draw(self):
        self.screen.blit(self.frames[self.current_frame], self.position)
        # pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)  # opcional: desenha o rect

    def run(self):
        self.update()
        self.draw()
