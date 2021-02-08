import pygame


class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode((1280, 720))
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
        self.screen.fill(color=(255, 255, 255))
        self.drawTriangle()
        self.display.flip()

    def drawTriangle(self):
        width = self.screen.get_width()
        height = self.screen.get_height()
        res = 1024
        for y in range(int((height / width * res) // 1)):
            for x in range(int(res)):
                x0 = width / res * x
                y0 = width / res * y
                x1 = width / res * (x + 1)
                y1 = width / res * (y + 1)

                pygame.draw.polygon(self.screen, (0, 0, 0), ((x0, y0), (x1, y0), (x0, y1)))
                pygame.draw.polygon(self.screen, (50, 50, 150), ((x1, y0), (x1, y1), (x0, y1)))


Game()
