import pygame

from game.world.map import Map
from game.core.rendering.masterRenderer import MasterRenderer
from game.world.mapRenderer import MapRenderer


class Game:
    def __init__(self, Frame, processor):
        self.settings = Frame.settings
        self.frame = Frame
        self.mapdata = Map().loadMap()
        self.mapRenderer = MapRenderer(processor, self)
        self.renderer = MasterRenderer(self)

    def mainloop(self):
        clock = pygame.time.Clock()
        run = True
        self.canShowMaps = True

        while run:
            clock.tick(1000)

            self.mousex, self.mousey = pygame.mouse.get_pos()
            self.casex = int(self.mousex / self.frame.width * (16 + 2))
            self.casey = int(self.mousey / self.frame.height * (16 + 2))

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_o:
                        run = False

            self.renderer.render()

        pygame.quit()
        print("\nScreen succesfully closed !")
