from .generation.color import Color

from enum import Enum


class Mode(Enum):
    COLORED = "colored"
    GREY = "grey"


class ColorMap():
    def __init__(self, noiseMap, regions):
        self.noiseMap = noiseMap
        self.regions = regions
        self.mapWidth = len(self.noiseMap[0])
        self.mapHeight = len(self.noiseMap)

    def generateColorMap(self, mode):

        loadstr = []
        for j in range(15):
            loadstr.append(".")

        colourmap = []

        if mode == Mode.COLORED.value:

            for y in range(self.mapHeight):
                loadstr[int((y / self.mapHeight * 15) // 1)] = "#"
                for x in range(self.mapWidth):
                    colourmap.append(None)
                    currentHeight = self.noiseMap[y][x]
                    for i in range(len(self.regions)):
                        if currentHeight <= self.regions[i].get("height"):
                            colourmap[y * self.mapWidth + x] = self.regions[i].get("colour")
                            break
                print('\r{} '.format(''.join(loadstr)) + ' {}'.format(
                    str(int((y + 1) * 100 / self.mapHeight)) + '/100' + r'%' + " - Creating colored colourMap"), end='')
            print("")

        elif mode == Mode.GREY.value:

            for y in range(self.mapHeight):
                loadstr[int((y / self.mapHeight * 15) // 1)] = "#"
                for x in range(self.mapWidth):
                    colourmap.append(None)
                    colourmap[y * self.mapWidth + x] = Color().lerp((0, 0, 0), (1, 1, 1), self.noiseMap[y][x])
                print('\r{} '.format(''.join(loadstr)) + ' {}'.format(
                    str(int((y + 1) * 100 / self.mapHeight)) + '/100' + r'%' + " - Creating greyed colourMap"), end='')
            print("")

            print(colourmap[0])

        return self.noiseMap, colourmap
