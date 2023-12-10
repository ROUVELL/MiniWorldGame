from functools import lru_cache
import pygame as pg

from settings import *


def coord_to_pos(x: int, y: int) -> tuple[int, int]:
    return (x // CELL_SIZE) * CELL_SIZE, (y // CELL_SIZE) * CELL_SIZE


def coord_to_index(x: int, y: int) -> tuple[int, int]:
    return x // CELL_SIZE, y // CELL_SIZE


def index_to_pos(i: int, j: int) -> tuple[int, int]:
    return i * CELL_SIZE, j * CELL_SIZE


def pos_to_index(x: int, y: int) -> tuple[int, int]:
    return x / CELL_SIZE, y / CELL_SIZE


@lru_cache(maxsize=None)
def load_img(path: str) -> pg.Surface:
    return pg.image.load(path)
