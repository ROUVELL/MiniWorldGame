import json
import pygame as pg

from settings import *


class WorldEditor:
    def __init__(self, game):
        self.game = game
        self.running = True

    def process_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                elif event.key == pg.K_s:
                    with open(MAPS + 'map1.json', encoding='utf-8', mode='w') as file:
                        file.write(self.game.world.to_json())

    def update(self):
        if pg.mouse.get_pressed()[0]:
            self.game.world.add(*pg.mouse.get_pos())
        if pg.mouse.get_pressed()[2]:
            self.game.world.remove(*pg.mouse.get_pos())

        self.game.world.update()

    def draw(self):
        self.game.sc.fill(BG)
        self.game.world.draw()
        pg.display.flip()

    def run(self):
        self.game.world.from_file('map1.json')
        while self.running:
            self.game.clock.tick(60)

            self.process_events()
            self.update()
            self.draw()
