import pygame as pg

from world import World
from editor import WorldEditor
from settings import *


class Game:
    def __init__(self):
        pg.display.init()
        pg.event.set_blocked(None)
        pg.event.set_allowed(pg.KEYUP)

        self.sc = pg.display.set_mode(SCREEN_SIZE, flags=pg.NOFRAME)
        self.clock = pg.time.Clock()
        self.running = False

        self.world = World(self)
        self.editor = WorldEditor(self)

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
                self.running = False

    def update(self):
        self.world.update()

    def draw(self):
        self.sc.fill(BG)
        self.world.draw()
        pg.display.flip()

    def run(self):
        self.editor.run()

        self.running = True
        self.world.from_file('map1.json')
        while self.running:
            self.clock.tick(60)

            self.process_events()
            self.update()
            self.draw()

        pg.quit()


if __name__ == '__main__':
    Game().run()
