import numpy as np
import pygame
import ctypes
from OpenGL.GL import *


class MeshData:
    def __init__(self, meshWidth, meshHeight, vaoID=None, vertexCount=None):
        self.triangleIndex = 0
        self.vertices = list(np.zeros(meshWidth * meshHeight * 2))
        self.triangles = list(np.zeros((meshWidth - 1) * (meshHeight - 1) * 6))
        self.vaoID = vaoID
        self.vertexCount = vertexCount

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

    # Creating vertices and indices
    vertices = [-0.5, 0.5,
                -0.5, -0.5,
                0.5, -0.5,
                0.5, 0.5]

    indices = [0, 1, 3,
               3, 2, 1]

    # Creating VAO and binding it
    vaoID = glGenVertexArrays(1)
    vaos.append(vaoID)
    glBindVertexArray(vaoID)

    # Creating VBO for verticices and binding it
    verticesID = glGenBuffers(1)
    vbos.append(verticesID)
    glBindBuffer(GL_ARRAY_BUFFER, verticesID)

    # Creating bufferData to store vertices position
    verticesBuffer = np.array(vertices, dtype='f')
    glBufferData(GL_ARRAY_BUFFER, verticesBuffer, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 2, GL_FLOAT, False, 0, None)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    # Creating VBO for indices and binding it
    indicesID = glGenBuffers(1)
    vbos.append(indicesID)

    # Creating bufferData to store indices
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indicesID)
    indicesBuffer = np.array(indices, dtype='uint32')
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
        glBindVertexArray(vaoID)

        # enabling VertexAttribArray to get vertices
        glEnableVertexAttribArray(0)

        # draw elements
        glDrawElements(GL_TRIANGLES, len(indices) * 4, GL_UNSIGNED_INT, None)

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
