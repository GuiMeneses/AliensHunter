import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT


class Entity:
    def __init__(self, screen, img_png: str, position: tuple):
        self.screen = screen
        self.position = position
        self.surf = pygame.image.load(img_png).convert_alpha()
        self.rect = self.surf.get_rect(topleft=self.position)
        self.vector_x = self.position[0]
        self.vector_y = self.position[1]

    def draw_entity(self):
        self.rect = self.surf.get_rect(topleft=self.position)
        self.screen.blit(self.surf, self.rect)
