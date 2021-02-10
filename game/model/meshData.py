import numpy as np


class MeshData:
    def __init__(self, meshWidth, meshHeight):
        self.triangleIndex = 0
        self.vertices = list(np.zeros(meshWidth * meshHeight * 2))
        self.triangles = list(np.zeros((meshWidth - 1) * (meshHeight - 1) * 6))

    def addTriangle(self, a, b, c):
        self.triangles[self.triangleIndex] = a
        self.triangles[self.triangleIndex + 1] = b
        self.triangles[self.triangleIndex + 2] = c
        self.triangleIndex += 3
