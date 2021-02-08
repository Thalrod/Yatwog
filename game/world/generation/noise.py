import matplotlib.pyplot as plt
import random
import os
import sys

from game.utils.Constants import Float
from game.utils import Mathf
from game.utils.Vector import Vector2
from opensimplex import OpenSimplex


class Noise():
    def __init__(self):
        pass

    def GenerateNoiseMap(self, mapWidth, mapHeight, seed, scale, octaves, persistence, lacunarity, offset):
        """
        :type mapWidth: int
        :type mapHeight: int
        :type seed: int
        :type scale: float
        :type octaves: int
        :type persistence: float
        :type lacunarity: float
        :type offset: Vector2
        """

        prng = random
        prng.seed(seed)

        octavesOffsets = []
        for i in range(octaves):
            octavesOffsets.append(None)
            offsetX = prng.randint(-100000, 100000) + offset[0]
            offsetY = prng.randint(-100000, 100000) + offset[1]
            octavesOffsets[i] = Vector2(offsetX, offsetY)

        noise = OpenSimplex(seed)
        noiseMap = []
        for j in range(mapHeight):
            noiseMap.append([])
            for o in range(mapWidth):
                noiseMap[j].append(None)

        if scale <= 0:
            scale = 0.0001

        maxNoiseHeight = Float.MinValue.value
        minNoiseHeight = Float.MaxValue.value

        halfWidth = mapWidth / 2
        halfHeight = mapHeight / 2

        loadstr = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]

        for y in range(mapHeight):
            loadstr[int((y / mapHeight * 15) // 1)] = "#"

            for x in range(mapWidth):

                amplitude = 1
                frequency = 1
                noiseHeight = 0

                for i in range(octaves):
                    sampleY = (y - halfHeight) / scale * frequency + octavesOffsets[i][0]
                    sampleX = (x - halfWidth) / scale * frequency + octavesOffsets[i][1]

                    perlinValue = noise.noise2d(x=sampleX, y=sampleY)
                    noiseHeight += perlinValue * amplitude

                    amplitude *= persistence
                    frequency *= lacunarity
                    """print("sampleX",sampleX)
                    print("sampleY",sampleY)
                    print("perlinValue",perlinValue)
                    print("\n")"""

                if noiseHeight > maxNoiseHeight:
                    maxNoiseHeight = noiseHeight
                elif noiseHeight < minNoiseHeight:
                    minNoiseHeight = noiseHeight

                noiseMap[y][x] = noiseHeight

                """print("amplitude",amplitude)
                print("frequency",frequency)
                print("noiseHeight",noiseHeight)
                print("octaves",octaves)
                print("maxNoiseHeight", maxNoiseHeight)
                print("minNoiseHeight", minNoiseHeight)
            print("\n\n\n")"""
            print('\r{} '.format(''.join(loadstr)) + ' {}'.format(
                str(int((y + 1) * 100 / mapHeight)) + '/100' + r'%' + " - Creating noiseMap"), end='')

        print("")
        loadstr = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]

        for y in range(mapHeight):
            loadstr[int((y / mapHeight * 15) // 1)] = "#"
            for x in range(mapWidth):
                noiseMap[y][x] = Mathf.inverse_lerp(minNoiseHeight, maxNoiseHeight, noiseMap[y][x])
            print('\r{} '.format(''.join(loadstr)) + ' {}'.format(
                str(int((y + 1) * 100 / mapHeight)) + '/100' + r'%' + " - Interpolating noiseMap"), end='')
        print("")
        self.save(noiseMap)
        return noiseMap

    def save(self, noiseMap):
        loadstr = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]

        with open(os.path.join(os.path.dirname(__file__), '../../../map/noiseMap.txt'), "w") as txt:
            for i in range(len(noiseMap)):
                loadstr[int((i / len(noiseMap) * 15) // 1)] = "#"
                txt.write(str(noiseMap[i]) + '\n')
            print('\r{} '.format(''.join(loadstr)) + ' {}'.format(
                str(int((i + 1) * 100 / len(noiseMap))) + '/100' + r'%' + " - Saving noiseMap"), end='')

        print("")

    def load(self):
        noiseMap = []

        with open(os.path.join(os.path.dirname(__file__), '../../../map/noiseMap.txt'), encoding='utf-8') as f:
            j = 0
            for line in f:
                loadstr = [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]

                line = line.replace("\n", "")
                line = line.replace("[", "")
                line = line.replace("]", "")
                values = line.split(",")

                noises = []
                for i in range(len(values)):
                    loadstr[int((i / len(values) * 15) // 1)] = "#"
                    try:
                        noises.append(float(values[i]))
                    except:
                        pass

                    print('\r{} '.format(''.join(loadstr)) + ' {}'.format(
                        str(i + 1) + '/' + str(len(values)) + " - Loading Map"), end='')

                noiseMap.append(noises)
                j += 1

        print("")

        return noiseMap
