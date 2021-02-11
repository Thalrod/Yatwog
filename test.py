import numpy as np
import pygame
import ctypes
from OpenGL.GL import *


class MeshData:
    def __init__(self, meshWidth, meshHeight, vaoID=None):
        self.triangleIndex = 0
        self.vertices = list(np.zeros(meshWidth * meshHeight))
        self.triangles = list(np.zeros((meshWidth - 1) * (meshHeight - 1) * 6))
        self.vaoID = vaoID

    def addTriangle(self, a, b, c):
        self.triangles[self.triangleIndex] = a
        self.triangles[self.triangleIndex + 1] = b
        self.triangles[self.triangleIndex + 2] = c
        self.triangleIndex += 3


def with_OpenGl():
    vaos = []
    vbos = []
    pygame.init()
    screen = pygame.display.set_mode((512, 512), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption("With OpenGl")
    glViewport(0, 0, 512, 512)

    heightMap = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

    indices = [0, 4, 3,
               0, 1, 4,
               2, 6, 5]
    # 0, 4, 3, 3, 0, 1, 2, 6, 5, 5, 2, 3, 6, 10, 9, 9, 6, 7, 8, 12, 11, 11, 8, 9

    width = len(heightMap[0])
    height = len(heightMap)

    topLeftX = (width - 1) / -2
    topLeftY = (height - 1) / 2
    meshData = MeshData(width, height)
    vertexIndex = 0

    for y in range(height):
        for x in range(width):

            meshData.vertices[vertexIndex] = (topLeftX + x, topLeftY - y)

            if x < width - 1 and y < height - 1:
                meshData.addTriangle(vertexIndex, vertexIndex + width + 1, vertexIndex + width)
                # meshData.addTriangle(vertexIndex + width + 1, vertexIndex, vertexIndex + 1)

            vertexIndex += 1

    # Creating VAO and binding it
    meshID = glGenVertexArrays(1)
    vaos.append(meshID)
    meshData.vaoID = meshID
    glBindVertexArray(meshID)

    # Creating VBO for verticices and binding it
    verticesID = glGenBuffers(1)
    vbos.append(verticesID)
    glBindBuffer(GL_ARRAY_BUFFER, verticesID)

    # Creating bufferData to store vertices position
    verticesBuffer = np.array(meshData.vertices, dtype='f')
    glBufferData(GL_ARRAY_BUFFER, verticesBuffer.flatten(), GL_STATIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, False, 0, None)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    # Creating VBO for indices and binding it
    indicesID = glGenBuffers(1)
    vbos.append(indicesID)

    # Creating bufferData to store indices
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indicesID)
    indicesBuffer = np.array(meshData.triangles, dtype='uint32')
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indicesBuffer, GL_STATIC_DRAW)

    # unbind VAO because I finished to use it
    glBindVertexArray(0)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_o:
                    run = False

        # Preparing screen
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1, 0, 0, 1)

        # Rendering
        # binding VAO
        glBindVertexArray(meshData.vaoID)

        # enabling VertexAttribArray to get vertices
        glEnableVertexAttribArray(0)

        # draw elements
        glDrawElements(GL_TRIANGLES, meshData.triangleIndex, GL_UNSIGNED_INT, None)

        # disabling VertexAttribArray and unbind VAO because I finished to use them
        glDisableVertexAttribArray(0)
        glBindVertexArray(0)

        pygame.display.flip()

    # Cleanup
    for vao in vaos:
        glDeleteVertexArrays(1, vao)

    for vbo in vbos:
        glDeleteBuffers(1, vbo)

    pygame.quit()


def without_OpenGl():
    pygame.init()
    display = pygame.display
    screen = display.set_mode((512, 512))
    display.set_caption("Without OpenGl")

    run = True
    clock = pygame.time.Clock()

    res = 16
    width = screen.get_width()
    height = screen.get_height()

    while run:

        clock.tick(100)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_o:
                    run = False

        for y in range(int(res)):

            for x in range(int(res)):
                x0 = (width / res) * x
                y0 = (height / res) * y

                x1 = (width / res) * (x + 1)
                y1 = (height / res) * (y + 1)

                vertices = np.array((((x0, y0), (x1, y0), (x0, y1)), ((x1, y0), (x1, y1), (x0, y1))), dtype='int')

                pygame.draw.polygon(screen, (88, 103, 55), vertices[0])
                pygame.draw.polygon(screen, (48, 153, 5), vertices[1])

        display.flip()
        screen.fill((255, 255, 255))

    run = True
    pygame.quit()


with_OpenGl()
