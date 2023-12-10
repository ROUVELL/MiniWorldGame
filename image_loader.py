import pygame as pg

from uttils import load_img
from settings import CELL_SIZE


class ImageLoader:
    __slots__ = ('__image', )

    def __init__(self, path: str = None):
        self.__image = None
        if path is not None:
            self.__image = load_img(path)

    def new(self, path: str):
        self.__image = load_img(path)
        return self

    def convert(self):
        self.__image = self.__image.convert()
        return self

    def convert_alpha(self):
        self.__image = self.__image.convert_alpha()
        return self

    def subsurface(self, x: int = 0, y: int = 0, width: int = CELL_SIZE, height: int = CELL_SIZE):
        self.__image = self.__image.subsurface(x, y, width, height)
        return self

    def apply(self) -> pg.Surface:
        return self.__image
