from enum import Enum

import pygame.image


class PacmanImage(Enum):
    """
    Набор возможных картинок пакмена
    """
    pacman_up_close = pygame.image.load('img/pacman_up_close.png')
    pacman_up_open = pygame.image.load('img/pacman_up_open.png')
    pacman_down_close = pygame.image.load('img/pacman_down_close.png')
    pacman_down_open = pygame.image.load('img/pacman_down_open.png')
    pacman_left_close = pygame.image.load('img/pacman_left_close.png')
    pacman_left_open = pygame.image.load('img/pacman_left_open.png')
    pacman_right_close = pygame.image.load('img/pacman_right_close.png')
    pacman_right_open = pygame.image.load('img/pacman_right_open.png')
    pacman_stay = pygame.image.load('img/pacman_stay.png')
