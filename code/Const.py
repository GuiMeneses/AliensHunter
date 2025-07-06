# C
import pygame

C_WHITE = (255, 255, 255)
C_YELLOW1 = (254, 167,17)
C_YELLOW2 = (255, 213,0)
C_YELLOW3 = (255, 235,136)
C_GREY = (80, 80, 80)
C_BLUE = (62, 160, 204)
C_RED = (214, 64, 64)



# E
ENTITY_HEALTH = {
    'Player': 100
}

ENTITY_COLLISION_DAMAGE = {
    'Player_ship': 5
}

ENTITY_SPEED = {
    'Background_1': 2,# 2
    'Background_2': 3,# 3
    'Background_3': 4,# 4
    'Background_4': 1,# 1
}

# K
KP_UP = pygame.K_w
KP_RIGHT = pygame.K_d
KP_DOWN = pygame.K_s
KP_LEFT = pygame.K_a
KP_SHOT = pygame.K_p

# P
PS_SUBTRACT_ENERGY = 0.15
PS_SPEED = 3
PS_SHOT_SPEED = 8

P_KEY_UP = pygame.K_w
P_KEY_RIGHT = pygame.K_d
P_KEY_DOWN = pygame.K_s
P_KEY_LEFT = pygame.K_a
P_KEY_SHOT = pygame.K_p


# S
SOUND_MENU_VOLUME = 0  #0.3
SOUND_MENU_BUTTON = 0 #0.05
SOUND_GAME_VOLUME = 0 #0.07

# W
WIN_WIDTH = 1080
WIN_HEIGHT = 810
