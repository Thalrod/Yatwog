class Color():
    # 0 -> 255

    r = 0.0
    g = 0.0
    b = 0.0
    a = 1.0

    def __init__(self, r=0.0, g=0.0, b=0.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = 1

    def GetTuple(self):
        return int(self.r), int(self.g), int(self.b)

    def SetColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def Copy(self, color):
        self.r = color.r
        self.g = color.g
        self.b = color.b

    def SetWhite(self):
        self.SetColor(1, 1, 1)

    def SetBlack(self):
        self.SetColor(0, 0, 0)

    def SetColorFromGrayscale(self, f=0.0):
        self.SetColor(f, f, f)

    def lerp(self, colora, colorb, amt):
        if amt < 0 or amt > 1:
            amt = 0.5

        r = colora[0] * amt + colorb[0] * (1 - amt)
        g = colora[1] * amt + colorb[1] * (1 - amt)
        b = colora[2] * amt + colorb[2] * (1 - amt)

        return round(r,2), round(g,2), round(b,2)
