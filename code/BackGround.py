import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, BG_SPEED


class BackGround:
    def __init__(self, name: str, position: tuple, screen):
        self.name = name
        self.screen = screen
        self.surf = pygame.image.load('./Assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    def draw(self):
        self.screen.blit(self.surf, self.rect)

    def move(self, other_img):
        self.rect.centery += BG_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = other_img.rect.top
