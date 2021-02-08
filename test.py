import pygame


class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode((500, 500))
        self.display.set_caption("test caption")
        self.run()

    def run(self):
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(60)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_o:
                        run = False

            self.update()

    def update(self):
        self.drawTriangle()
        self.display.flip()
        self.screen.fill(color=(255, 255, 255))


    def drawTriangle(self):
        PaddingX = 50
        PaddingY = 150
        pygame.draw.polygon(self.screen, (125, 125, 0), ((0 + PaddingX, 0 + PaddingY), (0 + PaddingX, 50 + PaddingY), (50 + PaddingX, 0 + PaddingY)))
        pygame.draw.polygon(self.screen, (0, 125, 125), ((50 + PaddingX, 0 + PaddingY), (50 + PaddingX, 50 + PaddingY), (0 + PaddingX, 50 + PaddingY)))

class Triangle():
    def __init__(self, location):
        x, y = location


Game()
