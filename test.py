import pygame

import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def with_OpenGl():
    def myInit():
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glPointSize(10.0)
        gluOrtho2D(0, 500, 0, 500)

    def display():
        res = 64
        width = 500
        height = 500
        glClear(GL_COLOR_BUFFER_BIT)

        for y in range(int(res)):
            for x in range(int(res)):
                glBegin(GL_TRIANGLE_STRIP)
                x0 = (width / res) * x
                y0 = (height / res) * y

                x1 = (width / res) * (x + 1)
                y1 = (height / res) * (y + 1)

                glColor3f(88/255, 103/255, 55/255)
                glVertex2f(x0, y0)
                glVertex2f(x1, y0)
                glVertex2f(x0, y1)
                # x1, y0), (x1, y1), (x0, y1)
                glColor3f(48/255, 153/255, 5/255)
                glVertex2f(x1, y0)
                glVertex2f(x1, y1)
                glVertex2f(x0, y1)

                glEnd()

        glFlush()

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(512, 512)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("My OpenGL Code")
    myInit()
    glutDisplayFunc(display)
    glutMainLoop()
    glutDestroyWindow(0)


def without_OpenGl():
    pygame.init()
    display = pygame.display
    screen = display.set_mode((512, 512))
    display.set_caption("Pygame Test")

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

    pygame.quit()

without_OpenGl()
