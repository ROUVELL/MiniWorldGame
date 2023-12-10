import json

from image_loader import ImageLoader
from cell import Cell, CellInfo
from uttils import coord_to_pos
from settings import *


class World:
    def __init__(self, game):
        self.game = game
        self.cells = dict()

    def to_json(self) -> str:
        obj = [cell.info.to_dict() for cell in self.cells.values()]
        return json.dumps(obj, indent=4)

    def from_file(self, filename: str):
        with open(MAPS + filename, encoding='utf-8', mode='r') as file:
            map_: dict = json.load(file)

        img_loader = ImageLoader()

        self.cells.clear()
        obj: dict
        for obj in map_.get("list", []):
            x, y = coord_to_pos(obj.get('x'), obj.get('y'))
            is_empty = obj.get('is_empty', True)
            is_water = obj.get('is_water', False)
            is_ground = obj.get('is_ground', True)
            is_blocked = obj.get('is_blocked', False)

            info = CellInfo(x, y , is_empty, is_water, is_ground, is_blocked)
            assert info.validate()
            img = img_loader.new(TEXTURES + 'ground/grass.png').subsurface(32, 0).convert().apply()
            self.cells[(x, y)] = Cell(info, img)

    def add(self, x: int, y: int):
        x, y = coord_to_pos(x, y)
        info = CellInfo(x, y)
        img = ImageLoader(TEXTURES + 'ground/grass.png').subsurface(32, 0).convert().apply()
        self.cells[(x, y)] = Cell(info, img)

    def remove(self, x: int, y: int):
        x, y = coord_to_pos(x, y)
        if (x, y) in self.cells:
            self.cells.pop((x, y))

    def update(self):
        pass

    def draw(self):
        for cell in self.cells.values():
            self.game.sc.blit(cell.image, cell.position)
