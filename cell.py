from dataclasses import dataclass
import pygame as pg

from uttils import pos_to_index


@dataclass(eq=False, slots=True)
class CellInfo:
    x: int
    y: int
    is_empty: bool = True     # Does the cell contain anything inside it (objects, npc, etc.)
    is_water: bool = False    # Does the cell is water
    is_ground: bool = True    # Does the cell is ground
    is_blocked: bool = False  # Is it possible to go through the cell (for pathfinding algorithm)

    def validate(self) -> bool:
        if (not isinstance(self.x, int)) or (not isinstance(self.y, int)):
            return False

        if self.is_water and self.is_ground:
            return False

        return True

    def to_dict(self) -> dict:
        return {
            "x": self.x,
            "y": self.y,
            "is_empty": self.is_empty,
            "is_water": self.is_water,
            "is_ground": self.is_ground,
            "is_blocked": self.is_blocked
        }



class Cell:
    def __init__(self, info: CellInfo, img: pg.Surface = None):
        self.info = info
        self.image = img

    @property
    def position(self) -> tuple[int, int]:
        return self.info.x, self.info.y

    @property
    def index(self) -> tuple[int, int]:
        return pos_to_index(self.info.x, self.info.y)

    def set_img(self, img: pg.Surface):
        self.image = img
        return self

    def __hash__(self):
        return hash((self.info.x, self.info.y))

    def __repr__(self):
        return self.info.__repr__()
