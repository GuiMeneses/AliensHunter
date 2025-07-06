import pygame


class PlayerStatus:
    def __init__(self):
        self.heath = 400
        self.energy = 400
        self.score = 0
        self.start_time = pygame.time.get_ticks()
        self.time = '00:00'

    def timer(self):
        elapsed_ms = pygame.time.get_ticks() - self.start_time
        elapsed_sec = elapsed_ms // 1000

        seconds = elapsed_sec % 60
        minutes = elapsed_sec // 60

        self.time = f"{minutes:02}:{seconds:02}"

    def add_score(self, score):
        self.score += score

    def add_energy(self, energy):
        self.energy += energy
        if self.energy > 400:
            self.energy = 400

    def subtract_energy(self, energy):
        self.energy -= energy

    def subtract_health(self, health):
        self.heath -= health
