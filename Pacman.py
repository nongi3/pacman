from Direction import Direction
from PacmanImage import PacmanImage


class Pacman:
    """
    Класс для описания пакмена

    Атрибуты:
    x : int
        Координата по x
    y : int
        Координата по y
    open_mouth : bool
        Открыт ли рот у макмена
    direction : Union(Direction)
        Направление пакмена
    speed : int
        Скорость пакмена.
        По умолчанию равна ширине клетки

    Методы:
    draw(screen):
        Отображает картинку на экране
    move():
        Движение пакмена в зависимости от направления
    calculate_new_coordinates():
        Высчитывает координаты после следующего шага
    get_coordinates():
        Получение координат в виде кортежа
    """
    def __init__(self, x, y):
        x: int
        y: int
        open_mouth: bool
        direction: Direction
        speed: int

        self.x = x
        self.y = y
        self.open_mouth = False
        self.direction = Direction.none
        self.speed = 40

    def draw(self, screen):
        """
        Отображает картинку на экране

        :param screen: дисплей игры
        :type screen: Surface
        """
        if self.direction == Direction.none:
            screen.blit(PacmanImage.pacman_stay.value, (self.x, self.y))
        elif self.direction == Direction.down:
            if self.open_mouth:
                screen.blit(PacmanImage.pacman_down_open.value, (self.x, self.y))
            else:
                screen.blit(PacmanImage.pacman_down_close.value, (self.x, self.y))
        elif self.direction == Direction.up:
            if self.open_mouth:
                screen.blit(PacmanImage.pacman_up_open.value, (self.x, self.y))
            else:
                screen.blit(PacmanImage.pacman_up_close.value, (self.x, self.y))
        elif self.direction == Direction.left:
            if self.open_mouth:
                screen.blit(PacmanImage.pacman_left_open.value, (self.x, self.y))
            else:
                screen.blit(PacmanImage.pacman_left_close.value, (self.x, self.y))
        elif self.direction == Direction.right:
            if self.open_mouth:
                screen.blit(PacmanImage.pacman_right_open.value, (self.x, self.y))
            else:
                screen.blit(PacmanImage.pacman_right_close.value, (self.x, self.y))

    def move(self):
        """
        Изменение координат пакмена в зависимости от направления.
        Каждый шаг также меняет флаг открытия рта.
        """
        if self.direction == Direction.up:
            self.y -= self.speed
        elif self.direction == Direction.down:
            self.y += self.speed
        elif self.direction == Direction.left:
            self.x -= self.speed
        elif self.direction == Direction.right:
            self.x += self.speed
        self.open_mouth = not self.open_mouth

    def calculate_new_coordinates(self) -> tuple:
        """
        Вычисляет координаты, которые будут после следующего шага.
        :return: кортеж координат
        :rtype: tuple
        """
        if self.direction == Direction.up:
            return self.x, self.y - self.speed
        elif self.direction == Direction.down:
            return self.x, self.y + self.speed
        elif self.direction == Direction.left:
            return self.x - self.speed, self.y
        elif self.direction == Direction.right:
            return self.x + self.speed, self.y
        return self.x, self.y

    def get_coordinates(self) -> tuple:
        """
        Возвращает координаты в виде кортеж
        :return: кортеж координат
        :rtype: tuple
        """
        return self.x, self.y
