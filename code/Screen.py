from abc import ABC, abstractmethod

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT


class Screen(ABC):
    def __init__(self):
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    @abstractmethod
    def run(self):
        pass

    def text(self):
        pass

    def bg_star(self):
        pass

