import json
import os
import numpy as np

from game.world.colorMap import ColorMap, Mode
from game.world.generation.mapGenerator import MapGenerator
from game.world.terrainType import TerrainType


class Map():
    def __init__(self):
        self.loadConfig()

        waterdeep = TerrainType("Water Deep", 0.3, (50, 99, 195))
        watershallow = TerrainType("Water Shallow", 0.4, (54, 103, 199))
        sand = TerrainType("Sand", 0.45, (210, 208, 125))
        grass = TerrainType("Grass", 0.55, (86, 152, 23))
        highgrass = TerrainType("High Grass", 0.6, (62, 107, 18))
        rock = TerrainType("Rock", 0.7, (90, 69, 60))
        highrock = TerrainType("High Rock", 0.9, (75, 60, 53))
        snow = TerrainType("Snow", 1, (255, 255, 255))

        plain = TerrainType("Plain", 1, (0, 153, 0))
        self.regions = [waterdeep, watershallow, sand, grass,
                        highgrass, rock, highrock, snow]

        self.noiseMap = MapGenerator(self.mapWidth, self.mapHeight, self.seed, self.scale, self.octaves,
                                     self.persistence, self.lacunarity, self.offset).generate()

    def loadMap(self):
        self.maps = ColorMap(self.noiseMap, self.regions).generateColorMap(self.RenderMode)
        return self.maps

    def getMaps(self):
        return self.maps

    def loadConfig(self):

        self.settings = {}
        with open(os.path.join(os.path.dirname(__file__), '../config/config.json')) as json_file:
            data = json.load(json_file)
            for k, v in data["Settings"].items():
                self.settings[k] = v
                for k1, v1 in data["Settings"][k].items():
                    self.settings[k][k1] = v1

        self.mapHeight = self.settings["Map"]["Height"]
        self.mapWidth = self.settings["Map"]["Width"]
        self.seed = self.settings["Map"]["seed"]
        self.scale = self.settings["Map"]["scale"]
        self.octaves = self.settings["Map"]["octaves"]
        self.persistence = self.settings["Map"]["persistence"]
        self.lacunarity = self.settings["Map"]["lacunarity"]
        self.RenderMode = self.settings["Frame"]["RenderMode"]

        value = self.settings["Map"]["offset"]
        value = value.replace('"', "")
        value = value.replace('(', "")
        value = value.replace(")", "")
        value = value.split(',')
        self.offset = (int(value[0]), int(value[1]))
