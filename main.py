import pygame
import math
import copy


import sys
import time
import os

from pygame.locals import *

"""
# TODO:
-Augmenter la résolution de la map genre au lieu de 1/1 faire du 16/1 ou 32/1
-Faire une mini map avec un point de couleur pour montrer ou tu es
-Faire en sorte de pouvoir bouger en laissant appuyer
-Etaler le projet sur plusieurs fichier py
-Modif le systeme pour add des case faut être en bordure et après avoir augmenté la res ça ne seras pas pareil
"""

ColorbyChar = {
        "0":(255,0,0),
        "1":(18,157,249),
        "2":(0,255,0),
        "E":(0,0,0)


}

Map = [["0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
       ["1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0"],
       ["0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
       ["1","0","1","2","1","0","2","0","1","0","1","0","1","0","1","0"],
       ["0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
       ["1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0"],
       ["0","1","0","2","0","1","2","1","0","1","0","1","0","1","0","1"],
       ["1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0"],
       ["0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
       ["1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0"],
       ["0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
       ["1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0"],
       ["0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
       ["1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0"],
       ["0","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
       ["1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","0"]]



pos = {}

OffsetX = 0
OffsetY = 0

w=h=500/16

maxX = 0

for y in range(len(Map)):
    if len(Map[y]) > maxX:
        maxX = len(Map[y])

height = int(w)*(len(Map)+2)+(OffsetY*(len(Map)+2))
width = int(h)*(maxX+2)+(OffsetX*(maxX+2))
size = height, width

class Game():
    def __init__(self):
        self.cam = Camera(0, 0, 8, 8)
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode((width, height))
        self.display.set_caption('2D Cube Test')
        self.canShowMaps = True
        self.run()

    def run(self):
        global width, height
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60) #set framerate
            self.mousex, self.mousey = pygame.mouse.get_pos()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_o:
                        run = False
                    if e.key == pygame.K_z:
                        self.cam.move(0)
                    if e.key == pygame.K_q:
                        self.cam.move(1)
                    if e.key == pygame.K_s:
                        self.cam.move(2)
                    if e.key == pygame.K_d:
                        self.cam.move(3)
                    #self.showMaps()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]: #tuple of boolean (leftclick, middleclick, rightclick)
                        rect = self.getRectangleFromMousePos()
                        if rect is not None:
                            rect.update("color", (0, 255, 0))
                            self.editMap(self.casex-1, self.casey-1, "2")
                    elif pygame.mouse.get_pressed()[2]:
                        rect = self.getRectangleFromMousePos()
                        if rect is not None:
                            self.editMap(self.casex-1, self.casey-1, "1")
                        else:
                            self.addSquare(self.casex-1, self.casey-1, "1")
                            self.canShowMaps = True





            self.casex = int(self.mousex/(width)*(maxX+2))
            self.casey = int(self.mousey/(height)*(len(Map)+2))



            self.cam.update()
            self.canvas()
            self.update() #update screen
            self.showMaps()





        pygame.quit()
        print("\nScreen succesfully closed !")

    def showMaps(self):
        if self.canShowMaps:
            self.canShowMaps = False
            print(self.cam.tostr())

    def getRectangleFromMousePos(self):
        try:
            if Map[self.casey-1][self.casex-1]:
                rect = pos[str(self.casex-1)+","+str(self.casey-1)].get("obj")
                rectx = rect.get("x")
                recty = rect.get("y")
                if self.mousex >= rectx and self.mousey >= recty:
                    return rect
                else:
                    return None
        except:
            return None

    def canvas(self):
        self.screen.fill(color=(255,255,255))
        self.loadMap(self.cam.get())
        self.highlightRectangle()

    def update(self):
        self.display.flip()
        self.screen.fill(color=(255,255,255))

    def highlightRectangle(self):
        rect = self.getRectangleFromMousePos()
        if rect is not None:
            rect.highlight(color=(163, 239, 31))

    def recalculateSize(self):
        global height, width, size, maxX

        for y in range(len(Map)):
            if len(Map[y]) > maxX:
                maxX = len(Map[y])

        height = int(w)*(len(Map)+2)+(OffsetY*(len(Map)+2))
        width = int(h)*(maxX+2)+(OffsetX*(maxX+2))
        size = height, width

        self.display.set_mode((width, height))

    def loadMap(self, map):
        for j in range(len(map)):
            for o in range(len(map[j])):

                y = int(w)*(j+1)+(OffsetY*(j+2))
                x = int(h)*(o+1)+(OffsetX*(o+2))

                #Load Map
                try:
                    if map[j][o] in ColorbyChar.keys():
                        r = Rectangle(self.screen, x, y, w, h, ColorbyChar[map[j][o]])
                        r.draw()

                    else:
                        print(map[j][o])
                        r = Rectangle(self.screen, x, y, w, h, (0,200,50))
                        r.draw()
                except Exception as e:
                    print(e)
                    r = Rectangle(self.screen, x, y, w, h, (255,255,255))
                    r.draw()

                pos[str(o)+","+str(j)] = r

    def editMap(self,x ,y, value):
        newMap = Map.copy()
        newMap[y][x] = value

    def addSquare(self, x, y ,value):
        global Map
        newMap = []
        if x < 0:
            # left side
            self.cam.relnegx -= 1
            if y < 0:
                # top left corner
                self.cam.relposy += 1
                newMap.append([value])
                for i in range(len(Map[0])):
                    newMap[0].append("E")

                for lines in range(len(Map)):
                    newMap.append(["E"])
                    for nodes in Map[lines]:
                        newMap[lines+1].append(copy.deepcopy(nodes))


            elif y >= len(Map):
                # bottom left corner
                self.cam.relnegy += 1
                for lines in range(len(Map)):
                    newMap.append(["E"])
                    for nodes in Map[lines]:
                        newMap[lines].append(copy.deepcopy(nodes))

                newMap.append([value])

                for n in range(len(Map[-1])):
                    newMap[-1].append("E")

            else:
                # left
                for lines in range(len(Map)):
                    if lines == y:
                        newMap.append([value])
                    else:
                        newMap.append(["E"])
                    for nodes in Map[lines]:
                        newMap[lines].append(copy.deepcopy(nodes))


        elif x >= maxX:
            # right side
            self.cam.relposx += 1
            if y < 0:
                # top right corner
                self.cam.relposy += 1
                newMap.append([])
                for i in range(len(Map[0])):
                    newMap[0].append("E")
                newMap[0].append(value)

                for lines in range(len(Map)):
                    newMap.append(copy.deepcopy(Map[lines]))
                    newMap[lines+1].append("E")


            elif y >= len(Map):
                # bottom right corner
                self.cam.relnegy -= 1
                for lines in range(len(Map)):
                    newMap.append(copy.deepcopy(Map[lines]))
                    newMap[lines].append("E")

                newMap.append([])

                for i in range(len(newMap)-1):
                    newMap[-1].append("E")
                newMap[-1].append(value)


            else:
                # right side

                for lines in range(len(Map)):
                    newMap.append(Map[lines].copy())
                    if lines == y:
                        newMap[lines].append(value)
                    else:
                        newMap[lines].append("E")


        elif y < 0:
            # top side
            self.cam.relposy += 1
            newMap.append([])
            for i in range(len(Map[0])):
                if i == x:
                    newMap[0].append(value)
                else:
                    newMap[0].append("E")
            for lines in range(len(Map)):
                newMap.append(copy.deepcopy(Map[lines]))


        elif  y >= len(Map):
            # bottom side
            self.cam.relnegy -= 1
            for lines in range(len(Map)):
                newMap.append(copy.deepcopy(Map[lines]))

            newMap.append([])

            for n in range(len(Map[-1])):
                if n == x:
                    newMap[-1].append(value)
                else:
                    newMap[-1].append("E")


        Map = copy.deepcopy(newMap)

class Rectangle():
    def __init__(self,screen, x, y, width, height, color):
        self.screen = screen
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;
        self.color = color


        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)

        self.obj = self



    def get(self, attrib):
        """
        :param attrib: str
        """
        try:
            return eval("self."+attrib)
        except:
            print(attrib + "is not attribute of Ractangle() there is: screen, x, y, width, height, color or rectangle")



    def update(self, attrib, value):
        """
        :param attrib: str
        """
        try:
            var = eval("self."+attrib)
            var = value
        except:
            print(attrib + "is not attribute of Rectangle() there is: screen, x, y, width, height, color or rectangle")

    def getInfo(self):
        return self.screen, self.x, self.y, self.width, self.height, self.color;

    def draw(self, color=None):
        if color is None:
            color = self.color
        pygame.draw.rect(self.screen, color, self.rectangle)

    def changeColor(self, color):
        self.color = color

    def highlight(self, color):
        self.draw(color = color)

class Camera():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.relposx = (len(Map[0]) - width)
        self.relnegx = -x
        self.relposy = y
        self.relnegy = -(len(Map) - height)
        self.nx = 0
        self.ny = 0
        self.height = height
        self.width = width

    def get(self):
        self.cam = []
        #print("__________start_____________")
        self.ny = (self.relposy - self.y)
        self.nx = (abs(self.relnegx) + self.x)
        if 0 > self.ny or self.ny >(len(Map) -self.height):
            self.ny = 0
        if 0 > self.nx or self.nx >(len(Map[0]) - self.width):
            self.nx = 0

        for y in range(self.height):
            self.ny = (self.relposy - self.y)
            line = copy.deepcopy(Map[self.ny + y])
            #print("".join(line), str(self.ny), str(self.y), str(self.relposy) + "", str(y))
            self.cam.append([])
            for x in range(self.width):
                self.cam[y].append(line[self.nx + x])
            #print("".join(self.cam[y]), str(self.nx), str(self.x), str(self.relnegx))
        #print("___________end______________\n")

        return self.cam

    def tostr(self):
        strng = "Cam:" + " "*(len(self.cam[0])+5) + "Map:\n"
        for line in range(len(Map)):
            try:
                strng += "".join(self.cam[line]) + " "*(len(self.cam[0])+1) + "".join(Map[line])
            except:
                strng += " "*(len(self.cam[0])+9)  + "".join(Map[line])
            strng+="\n"
        return strng

    def update(self):
        self.get()

    def move(self, dir):
        if dir == 0:
            self.y += 1
            if self.y > self.relposy:
                self.y -= 1
        if dir == 1:
            self.x -= 1
            if self.x < self.relnegx:
                self.x += 1
        if dir == 2:
            self.y -= 1
            if self.y < self.relnegy:
                self.y += 1
        if dir == 3:
            self.x += 1
            if self.x > self.relposx:
                self.x -= 1






game = Game()
