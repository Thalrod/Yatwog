import pygame

from game.shape.rectangle import Rectangle
from game.world.renderer import Mode


class MasterRenderer():
    def __init__(self, master):
        self.master = master
        self.screen = master.frame.screen
        self.display = master.frame.display
        self.settings = master.settings
        self.loadConfig()
        self.map = master.map
        self.colourmap = master.colourmap

    def render(self):
        self.map = self.master.map
        # self.cam = self.master.cam
        self.screen.fill(color=(255, 255, 255))
        self.renderMap(self.map, self.colourmap, self.RenderMode)
        # self.highlightRectangle()
        self.display.flip()

    def loadConfig(self):
        self.ColorbyChar = {}
        for key, value in self.settings["ColorbyChar"].items():
            value = value.replace('"', "")
            value = value.replace('(', "")
            value = value.replace(")", "")
            value = value.split(',')
            self.ColorbyChar[key] = (int(value[0]), int(value[1]), int(value[2]))

        self.OffsetX = self.settings["Rectangle"]["OffsetX"]
        self.OffsetY = self.settings["Rectangle"]["OffsetX"]
        self.height = self.settings["Frame"]["height"]
        self.width = self.settings["Frame"]["width"]
        self.RenderMode = self.settings["Frame"]["RenderMode"]
        self.mapheight = self.settings["Map"]["Height"]
        self.mapwidth = self.settings["Map"]["Width"]

        self.rectheight = (self.height - 2 * self.OffsetY) / self.mapheight
        self.rectwidth = (self.height - 2 * self.OffsetY) / self.mapwidth
        self.pos = {}

    def renderMap(self, map, colourmap, mode):

        res = len(map)

        if mode == Mode.COLORED.value:
            for j in range(len(map)):
                for o in range(len(map[j])):
                    y = j
                    x = o
                    w = self.rectwidth
                    h = self.rectheight
                    color = colourmap[j * len(map[j]) + o]
                    # Load Map
                    r = Rectangle(self.screen, x, y, w, h, color)
                    r.draw()

                    self.pos[str(o) + "," + str(j)] = r

        elif mode == Mode.GREY.value:
            for j in range(len(map)):
                for o in range(len(map[j])):
                    y = int(self.rectheight) * j
                    x = int(self.rectwidth) * o
                    w = self.rectwidth
                    h = self.rectheight
                    color = colourmap[j * len(map[j]) + o]
                    # Load Map
                    r = Rectangle(self.screen, x, y, w, h, (color[0] * 255, color[1] * 255, color[2] * 255))
                    r.draw()

                    self.pos[str(o) + "," + str(j)] = r

    def getRectangleFromMousePos(self):
        try:
            if self.map[self.master.casex - 1][self.master.casey - 1]:
                rect = self.pos[str(self.master.casex - 1) + "," + str(self.master.casey - 1)].get("obj")
                rectx = rect.get("x")
                recty = rect.get("y")
                if self.master.mousex >= rectx and self.master.mousey >= recty:
                    return rect
                else:
                    return None
        except Exception as e:
            return None

    def highlightRectangle(self):
        rect = self.getRectangleFromMousePos()
        if rect is not None:
            rect.highlight(color=(163, 239, 31))
