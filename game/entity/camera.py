import copy

class Camera():
    def __init__(self, x, y, master):
        self.master = master
        self.settings = master.settings
        self.loadConfig()
        self.map = master.map
        self.x = x
        self.y = y
        self.relposx = (len(self.map[0]) - self.width)
        self.relnegx = -x
        self.relposy = y
        self.relnegy = -(len(self.map) - self.height)
        self.nx = 0
        self.ny = 0

    def loadConfig(self):
        self.height = self.settings["Camera"]["height"]
        self.width = self.settings["Camera"]["width"]

    def get(self):
        self.cam = []
        #print("__________start_____________")
        self.ny = (self.relposy - self.y)
        self.nx = (abs(self.relnegx) + self.x)
        if 0 > self.ny or self.ny >(len(self.map) -self.height):
            self.ny = 0
        if 0 > self.nx or self.nx >(len(self.map[0]) - self.width):
            self.nx = 0

        for y in range(self.height):
            self.ny = (self.relposy - self.y)
            line = copy.deepcopy(self.map[self.ny + y])
            #print("".join(line), str(self.ny), str(self.y), str(self.relposy) + "", str(y))
            self.cam.append([])
            for x in range(self.width):
                self.cam[y].append(line[self.nx + x])
            #print("".join(self.cam[y]), str(self.nx), str(self.x), str(self.relnegx))
        #print("___________end______________\n")

        return self.cam

    def tostr(self):
        strng = "Cam:" + " "*(len(self.cam[0])+5) + "Map:\n"
        for line in range(len(self.map)):
            try:
                strng += "".join(self.cam[line]) + " "*(len(self.cam[0])+1) + "".join(self.map[line])
            except:
                strng += " "*(len(self.cam[0])+11)  + "".join(self.map[line])
            strng+="\n"
        return strng

    def update(self):
        self.cam = self.get()
        self.map = self.master.map



    def move(self, dir):
        print(dir)
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
