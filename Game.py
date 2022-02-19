from typing import Union

import pygame
from pygame import Surface
from pygame.surface import SurfaceType

from Direction import Direction
from Food import Food
from GameSettings import GameSettings
from Ghost import Ghost
from Pacman import Pacman
from Wall import Wall


class Game:
    """
    Класс для описания игры

    Атрибуты:
    game_settings: GameSettings
        Основные констаны игры.
    screen: Union[Surface, SurfaceType]
        Дисплей игры.
    pacman: Union[None, Pacman]
        Объект пакмена.
        Равен None до момента парсинга, который происходит в момент создания игры.
    food: list[Food]
        Список объектов еды.
    coordinates_food: dict[tuple[int, int], Food]
        Словарь для быстрого обращения к еде.
        Ключ - кортеж координат еды.
        Значение - объект еды по этим координатам.
    ghosts: list[Ghost]
        Список призраков.
    walls: list[Wall]
        Список стен.
    coordinates_walls: dict[tuple[int, int], Wall]
        Словарь для быстрого обращения к стенам.
        Ключ - кортеж координат стены.
        Значение - объект стен по этим координатам.
    ticks: int
        Ход пакмена осуществляется раз в 60 тиков.

    Методы:
    parse_map():
        Парсинг карты и создание объектов.
    launch():
        Фукнция запуска игры. Здесь расположен вызов всего функционала.
    is_win():
        Проверка на победу
    is_pacman_dead():
        Проверка, не врезался ли пакмен в призрака
    key_check(key):
        Проверка нажатия на клавиши.
    eat_food():
        Попытка съесть еду пакменом.
    is_pacman_can_move():
        Проверка, может ли пакмен двигаться.
    draw():
        Метод для отрисовки всех объектов на экране
    """
    game_settings: GameSettings
    screen: Union[Surface, SurfaceType]
    pacman: Union[None, Pacman]
    food: list[Food]
    coordinates_food: dict[tuple[int, int], Food]
    ghosts: list[Ghost]
    walls: list[Wall]
    coordinates_walls: dict[tuple[int, int], Wall]
    ticks: int

    def __init__(self):
        self.game_settings = GameSettings()

        pygame.init()
        self.screen = pygame.display.set_mode((self.game_settings.WINDOW_WIDTH, self.game_settings.WINDOW_HEIGHT))

        self.pacman = None
        self.food = []
        self.coordinates_food = {}
        self.ghosts = []
        self.walls = []
        self.coordinates_walls = {}

        self.ticks = 0

        self.parse_map()

    def parse_map(self):
        """
        Парсинг карты и создание объектов.
        """
        x = 0
        y = 0
        for row in self.game_settings.MAP_CONFIGURATION:
            for cell in row:
                if cell == 'P':
                    self.pacman = Pacman(x, y)
                elif cell == 'G':
                    self.ghosts.append(Ghost(x, y))
                elif cell == '1':
                    self.food.append(Food(x, y, True))
                    self.coordinates_food[(x, y)] = self.food[-1]
                elif cell == '0':
                    self.food.append(Food(x, y, False))
                    self.coordinates_food[(x, y)] = self.food[-1]
                else:
                    self.walls.append(Wall(x, y))
                    self.coordinates_walls[(x, y)] = self.walls[-1]
                x += 40
            x = 0
            y += 40

    def launch(self):
        """
        Фукнция запуска игры. Здесь расположен вызов всего функционала.
        """
        while True:
            self.ticks += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    self.key_check(event.key)
            if self.is_pacman_dead():
                # TODO: написать сообщение о поражении
                pygame.quit()
                return
            self.draw()
            if self.ticks % 60 == 0:
                self.ticks = 0
                if self.is_pacman_can_move():
                    self.pacman.move()
                else:
                    self.pacman.direction = Direction.none
            self.eat_food()
            if self.is_win():
                # TODO: написать сообщение о победе
                pygame.quit()
                return

    def is_win(self):
        """
        Проверка на победу
        :return: true, если вся еда съедена
        :rtype: bool
        """
        return len(self.food) == 0

    def is_pacman_dead(self):
        """
        Проверка, не врезался ли пакмен в призрака
        :return: true, если пакмена убили
        :rtype: bool
        """
        for ghost in self.ghosts:
            if self.pacman.x == ghost.x and self.pacman.y == ghost.y:
                return True
        return False

    def key_check(self, key):
        """
        Проверка нажатия на клавиши.
        :param key: id нажатия кнопки
        :type key: int
        """
        if key == pygame.K_w:
            self.pacman.direction = Direction.up
        if key == pygame.K_s:
            self.pacman.direction = Direction.down
        if key == pygame.K_a:
            self.pacman.direction = Direction.left
        if key == pygame.K_d:
            self.pacman.direction = Direction.right

    def eat_food(self):
        """
        Попытка съесть еду пакменом.
        В случае поедания еды, её объект удаляется.
        """
        pacman_coordinates = self.pacman.get_coordinates()
        if pacman_coordinates in self.coordinates_food:
            self.food.remove(self.coordinates_food[pacman_coordinates])
            del self.coordinates_food[pacman_coordinates]

    def is_pacman_can_move(self) -> bool:
        """
        Проверка, может ли пакмен двигаться
        :return: true, если может двигаться
        :rtype: bool
        """
        new_coordinates = self.pacman.calculate_new_coordinates()
        return new_coordinates not in self.coordinates_walls

    def draw(self):
        """
        Метод для отрисовки всех объектов на экране
        """
        self.screen.fill((0, 0, 0))
        self.pacman.draw(self.screen)
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        for food in self.food:
            food.draw(self.screen)
        for wall in self.walls:
            wall.draw(self.screen)
        pygame.display.update()


game = Game()
game.launch()
