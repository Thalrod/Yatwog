import pygame
import math
import copy

import sys
import time
import os

from game.world.map import Map
#from game.world.editor import Editor
from game.entity.camera import Camera
from game.core.rendering.masterRenderer import MasterRenderer

class Game():
    def __init__(self, Frame):
        self.settings = Frame.settings
        self.frame = Frame
        self.map, self.colourmap = Map().loadMap()
        #self.cam = Camera(0,0, self)
        self.renderer = MasterRenderer(self)
        #self.editor = Editor(self)

    def mainloop(self):
        clock = pygame.time.Clock()
        run = True
        self.canShowMaps = True
        while run:
            clock.tick(60)
            self.mousex, self.mousey = pygame.mouse.get_pos()
            self.casex = int(self.mousex/(self.frame.width)*(16+2))
            self.casey = int(self.mousey/(self.frame.height)*(16+2))

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_o:
                        run = False
                    '''if e.key == pygame.K_z:
                        self.cam.move(0)
                    if e.key == pygame.K_q:
                        self.cam.move(1)
                    if e.key == pygame.K_s:
                        self.cam.move(2)
                    if e.key == pygame.K_d:
                        self.cam.move(3)
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]: #tuple of boolean (leftclick, middleclick, rightclick)
                        rect = self.renderer.getRectangleFromMousePos()
                        if rect is not None:
                            rect.update("color", (0, 255, 0))
                            self.editor.editMap(self.casex-1, self.casey-1, "1")
                    elif pygame.mouse.get_pressed()[2]:
                        rect = self.renderer.getRectangleFromMousePos()
                        if rect is not None:
                            self.editor.editMap(self.casex-1, self.casey-1, "2")
                        else:
                            self.editor.addSquare(self.casex-1, self.casey-1, "1")
                            self.canShowMaps = True'''




            #self.cam.update()
            self.renderer.render()
            self.showMaps()

        pygame.quit()
        print("\nScreen succesfully closed !")

    def showMaps(self):
        if self.canShowMaps:
            self.canShowMaps = False
            #print(self.cam.tostr())
