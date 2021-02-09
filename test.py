import pygame
from OpenGL.GL import *
from ctypes import *

import numpy as np


def with_OpenGl():
    pygame.init()
    screen = pygame.display.set_mode((512, 512), pygame.OPENGL | pygame.DOUBLEBUF, 24)
    pygame.display.set_caption("With OpenGl")
    glViewport(-512, 0, 1024, 1024)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnableClientState(GL_VERTEX_ARRAY)

    res = 64
    width = screen.get_width()
    height = screen.get_height()

    v = []
    v2 = []
    maxX = 0
    maxX1 = 0
    maxY = 0
    maxY1 = 0
    for y in range(res):
        for x in range(res):
            x0 = (width / res) * x / width
            y0 = (height / res) * y / height - 1

            x1 = (width / res) * (x + 1) / width
            y1 = (height / res) * (y + 1) / height - 1

            maxX = x0 if x0 > maxX else maxX
            maxX1 = x1 if x1 > maxX1 else maxX1
            maxY = y0 if y0 > maxY else maxY
            maxY1 = y1 if y1 > maxY1 else maxY1

            v.append(x0)
            v.append(y0)

            v.append(x1)
            v.append(y0)

            v.append(x0)
            v.append(y1)

            v2.append(x1)
            v2.append(y1)

            v2.append(x0)
            v2.append(y1)

            v2.append(x1)
            v2.append(y0)

    vbo = glGenBuffers(1)
    vbo1 = glGenBuffers(1)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, len(v) * 4, (c_float * len(v))(*v), GL_STATIC_DRAW)

    glBindBuffer(GL_ARRAY_BUFFER, vbo1)
    glBufferData(GL_ARRAY_BUFFER, len(v2) * 4, (c_float * len(v2))(*v2), GL_STATIC_DRAW)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(1000)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_o:
                    run = False

        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(88 / 255, 103 / 255, 55 / 255)

        glBindBuffer(GL_ARRAY_BUFFER, vbo)

        glVertexPointer(2, GL_FLOAT, 0, None)

        glDrawArrays(GL_TRIANGLES, 0, len(v) * 4)

        glColor3f(48 / 255, 153 / 255, 5 / 255)

        glBindBuffer(GL_ARRAY_BUFFER, vbo1)

        glVertexPointer(2, GL_FLOAT, 0, None)

        glDrawArrays(GL_TRIANGLES, 0, len(v2) * 4)

        pygame.display.flip()

    run = True
    pygame.quit()

def without_OpenGl():
    pygame.init()
    display = pygame.display
    screen = display.set_mode((512, 512))
    display.set_caption("Without OpenGl")

    run = True
    clock = pygame.time.Clock()

    res = 64
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


while True:
    without_OpenGl()
    with_OpenGl()
