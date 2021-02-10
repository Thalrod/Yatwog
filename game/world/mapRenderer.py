from game.model.meshData import MeshData
from game.world.colorMap import Mode
from game.shape.rectangle import Rectangle
from OpenGL.GL import *


class MapRenderer:

    def __init__(self, processor, instance):
        self.processor = processor
        self.main = instance
        self.screen = instance.frame.screen
        self.settings = instance.settings

        self.mode = self.settings["Frame"]["RenderMode"]

        self.OffsetY = self.settings["Rectangle"]["OffsetX"]
        self.OffsetX = self.settings["Rectangle"]["OffsetX"]

        self.width = self.settings["Frame"]["width"]
        self.height = self.settings["Frame"]["height"]

        self.mapheight = self.settings["Map"]["Height"]
        self.mapwidth = self.settings["Map"]["Width"]

        self.rectwidth = (self.height - 2 * self.OffsetY) / self.mapwidth
        self.rectheight = (self.height - 2 * self.OffsetY) / self.mapheight

        self.pos = {}

    def GenerateTerrainMesh(self, map, colormap):
        if self.processor == "CPU":
            res = len(map)

            if self.mode == Mode.COLORED.value:
                for j in range(len(map)):
                    for o in range(len(map[0])):
                        y = j
                        x = o

                        w = self.rectwidth
                        h = self.rectheight
                        color = colormap[j * len(map[j]) + o]
                        # Load Map
                        r = Rectangle(self.screen, x, y, w, h, color)
                        r.draw()

                        self.pos[str(o) + "," + str(j)] = r

            elif self.mode == Mode.GREY.value:
                for j in range(len(map)):
                    for o in range(len(map[j])):
                        y = int(self.rectheight) * j
                        x = int(self.rectwidth) * o
                        w = self.rectwidth
                        h = self.rectheight
                        color = colormap[j * len(map[j]) + o]
                        # Load Map
                        r = Rectangle(self.screen, x, y, w, h, (color[0] * 255, color[1] * 255, color[2] * 255))
                        r.draw()

                        self.pos[str(o) + "," + str(j)] = r
        elif self.processor == "GPU":
            heightMap = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]

            width = len(heightMap[0])
            height = len(heightMap)

            topLeftX = (width - 1) / -2
            topLeftY = (height - 1) / 2
            meshData = MeshData(width, height)
            vertexIndex = 0

            for y in range(height):
                for x in range(width):

                    meshData.vertices[vertexIndex] = topLeftX + x
                    meshData.vertices[vertexIndex + 1] = topLeftY - y

                    if x < width - 1 and y < height - 1:
                        meshData.addTriangle(vertexIndex, vertexIndex + width + 1, vertexIndex + width)
                        meshData.addTriangle(vertexIndex + width, vertexIndex, vertexIndex + 1)

                    vertexIndex += 2

            vbo = glGenBuffers(1)

            glDrawElements(GL_TRIANGLES, len(meshData.vertices) * 4, GL_UNSIGNED_INT, 0)

            # print(width, height, meshData.vertices, len(meshData.vertices), meshData.triangles,
            # len(meshData.triangles))

        else:
            print("Invalid Processor !", self.processor)

    def render(self, map, colormap):
        self.GenerateTerrainMesh(map, colormap)
