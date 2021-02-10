from OpenGL.GL import *
from ctypes import *

from game.shape.rectangle import Rectangle
from game.world.colorMap import Mode


class MasterRenderer():
    def __init__(self, master):

        self.settings = master.settings

        self.pos = {}

        self.master = master
        self.screen = master.frame.screen
        self.display = master.frame.display
        self.mapRenderer = master.mapRenderer

        self.mapdata = master.mapdata
        self.map = self.mapdata[0]
        self.colourmap = self.mapdata[1]

    def render(self):
        self.mapdata = self.master.mapdata

        self.mapRenderer.render(self.map, self.colourmap)

        self.display.flip()
