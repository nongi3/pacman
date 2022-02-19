from enum import Enum


class Direction(Enum):
    """
    Набор возможных направлений.
    Используется пакменом.
    """
    none = None
    right = 'right'
    left = 'left'
    up = 'up'
    down = 'down'
