import pygame
import json
import os

from OpenGL.GL import *

from game.core.game.mainloop import Game


class Frame():
    def __init__(self):
        self.settings = self.loadConfig()
        pygame.init()
        self.display = pygame.display
        self.processor = self.settings["Frame"]["Processor"]
        print("Graphical Processor:", self.processor)
        if self.processor == "GPU":
            self.screen = self.display.set_mode((self.recalculateSize()), pygame.OPENGL | pygame.DOUBLEBUF, 24)
            self.display.set_caption(self.settings["Frame"]["Title"])
            glClearColor(0.3, 0.4, 0.3, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)
            glEnableClientState(GL_VERTEX_ARRAY)
        elif self.processor == 'CPU':
            self.display = pygame.display
            self.screen = self.display.set_mode((self.recalculateSize()))
            self.display.set_caption(self.settings["Frame"]["Title"])

        game = Game(self, self.processor)
        game.mainloop()

    def loadConfig(self):
        settings = {}
        with open(os.path.join(os.path.dirname(__file__), '../../config/config.json')) as json_file:
            data = json.load(json_file)
            for k, v in data["Settings"].items():
                settings[k] = v
                for k1, v1 in data["Settings"][k].items():
                    settings[k][k1] = v1
        return settings

    def parseConfigToJson(self, data):
        f = open(os.path.join(os.path.dirname(__file__), '../../config/config.json'), "w")
        f.write(data)
        f.close()

    def recalculateSize(self):
        self.OffsetX = self.settings["Rectangle"]["OffsetX"]
        self.OffsetY = self.settings["Rectangle"]["OffsetX"]
        self.height = self.settings["Frame"]["height"]
        self.width = self.settings["Frame"]["width"]
        self.mapheight = self.settings["Map"]["Height"]
        self.mapwidth = self.settings["Map"]["Width"]

        self.rectheight = (self.height - self.OffsetY / 2) / self.mapheight
        self.rectwidth = (self.height - self.OffsetX / 2) / self.mapwidth
        # self.height = int(self.rectheight)*(self.mapheight+2)+(self.OffsetY*(self.mapheight+2))
        # self.width = int(self.rectwidth)*(self.mapwidth+2)+(self.OffsetX*(16+2))
        self.size = self.height, self.width
        return self.size
