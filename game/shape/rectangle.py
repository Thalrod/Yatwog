import pygame


class Rectangle():
    def __init__(self, screen, x, y, width, height, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.rectangle = pygame.Rect(self.x, self.y, self.width, self.height)

        self.obj = self

    def get(self, attrib):
        """
        :param attrib: str
        """
        try:
            return eval("self." + attrib)
        except:
            print(attrib + "is not attribute of Ractangle() there is: screen, x, y, width, height, color or rectangle")

    def update(self, attrib, value):
        """
        :param attrib: str
        """
        try:
            var = eval("self." + attrib)
            var = value
        except:
            print(attrib + "is not attribute of Rectangle() there is: screen, x, y, width, height, color or rectangle")

    def getInfo(self):
        return self.screen, self.x, self.y, self.width, self.height, self.color

    def draw(self, color=None):
        if color is None:
            color = self.color

        width = self.width
        height = self.height

        x0 = width * self.x
        y0 = height * self.y

        x1 = width * (self.x + 1)
        y1 = height * (self.y + 1)

        vertexCoord = (((x0, y0), (x1, y0), (x0, y1)), ((x1, y0), (x1, y1), (x0, y1)))

        pygame.draw.polygon(self.screen, color, vertexCoord[0])
        pygame.draw.polygon(self.screen, color, vertexCoord[1])

    def changeColor(self, color):
        self.color = color

    def highlight(self, color):
        self.draw(color=color)
