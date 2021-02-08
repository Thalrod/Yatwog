from .noise import Noise


class MapGenerator():
    def __init__(self, mapWidth, mapHeight, seed, scale, octaves, persistance, lacunarity, offset):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.seed = seed
        self.scale = scale
        self.octaves = octaves
        self.persistance = persistance
        self.lacunarity = lacunarity
        self.offset = offset

    def generate(self):
        self.noiseMap = Noise().GenerateNoiseMap(self.mapWidth, self.mapHeight, self.seed, self.scale, self.octaves,
                                                 self.persistance, self.lacunarity, self.offset)
        # self.noiseMap = Noise().load()

        return self.noiseMap
