import pygame.image
from pygame import Surface


class Wall:
    """
    Класс для описания стен

    Атрибуты:
    x : int
        Координата по x
    y : int
        Координата по y
    sprite: Surface
        Картинка стены

    Методы:
    draw(screen)
        Отображает картинку на экране
    """
    def __init__(self, x, y):
        x: int
        y: int
        sprite: Surface

        self.x = x
        self.y = y
        self.sprite = pygame.image.load("img/wall.png")

    def draw(self, screen):
        """
        Отображает картинку на экране

        :param screen: дисплей игры
        :type screen: Surface
        """
        screen.blit(self.sprite, (self.x, self.y))
