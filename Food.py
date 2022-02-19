import pygame.image
from pygame import Surface


class Food:
    """
    Класс для описания еды

    Атрибуты:
    x : int
        Координата по x
    y : int
        Координата по y
    bonus : bool
        Является ли еда бонусом
    value : int
        Количество очков, получаемых за сбор этой еды
    sprite : Surface
        Картинка призрака

    Методы:
    draw(screen):
        Отображает картинку на экране
    get_coordinates():
        Получение координат в виде кортежа
    """
    x: int
    y: int
    bonus: bool
    value: int
    sprite: Surface

    def __init__(self, x, y, bonus):
        self.x = x
        self.y = y
        # TODO: бонус в данный момент ничего не дает, кроме доп. очков; надо бы исправить
        self.bonus = bonus
        self.value = 10 if bonus else 1
        self.sprite = pygame.image.load("img/bonus_food.png") if bonus else pygame.image.load("img/food.png")

    def draw(self, screen):
        """
        Отображает картинку на экране

        :param screen: дисплей игры
        :type screen: Surface
        """
        screen.blit(self.sprite, (self.x, self.y))

    def get_coordinates(self):
        """
        Возвращает координаты в виде кортеж
        :return: кортеж координат
        :rtype: tuple
        """
        return self.x, self.y
