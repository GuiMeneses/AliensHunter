import pygame


class MyTimer:
    def __init__(self, reset):
        self.start_time = pygame.time.get_ticks()
        self.seconds = reset

    def run(self):
        elapsed_ms = pygame.time.get_ticks() - self.start_time
        elapsed_sec = elapsed_ms / 1000
        self.seconds = round(elapsed_sec % 60, 2)