import pygame.image
from pygame import Surface


class Ghost:
    """
    Класс для описания призраков

    Атрибуты:
    x : int
        Координата по x
    y : int
        Координата по y
    sprite : Surface
        Картинка призрака

    Методы:
    draw(screen):
        Отображает картинку на экране
    """
    x: int
    y: int
    ghost_picture: Surface

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load("img/ghost.png")

    def draw(self, screen):
        """
        Отображает картинку на экране

        :param screen: дисплей игры
        :type screen: Surface
        """
        screen.blit(self.sprite, (self.x, self.y))
