import copy

class Editor():
    def __init__(self, master):
        self.master = master
        self.settings = master.settings
        self.map = master.map
        self.cam = master.cam
        self.maxX = 16

    def editMap(self,x ,y, value):
        self.map[y][x] = value

    def addSquare(self, x, y ,value):
        newMap = []
        if x < 0:
            # left side
            self.cam.relnegx -= 1
            if y < 0:
                # top left corner
                self.cam.relposy += 1
                newMap.append([value])
                for i in range(len(self.map[0])):
                    newMap[0].append("E")

                for lines in range(len(self.map)):
                    newMap.append(["E"])
                    for nodes in self.map[lines]:
                        newMap[lines+1].append(copy.deepcopy(nodes))


            elif y >= len(self.map):
                # bottom left corner
                self.cam.relnegy += 1
                for lines in range(len(self.map)):
                    newMap.append(["E"])
                    for nodes in self.map[lines]:
                        newMap[lines].append(copy.deepcopy(nodes))

                newMap.append([value])

                for n in range(len(self.map[-1])):
                    newMap[-1].append("E")

            else:
                # left
                for lines in range(len(self.map)):
                    if lines == y:
                        newMap.append([value])
                    else:
                        newMap.append(["E"])
                    for nodes in self.map[lines]:
                        newMap[lines].append(copy.deepcopy(nodes))


        elif x >= self.maxX:
            # right side
            self.cam.relposx += 1
            if y < 0:
                # top right corner
                self.cam.relposy += 1
                newMap.append([])
                for i in range(len(self.map[0])):
                    newMap[0].append("E")
                newMap[0].append(value)

                for lines in range(len(self.map)):
                    newMap.append(copy.deepcopy(self.map[lines]))
                    newMap[lines+1].append("E")


            elif y >= len(self.map):
                # bottom right corner
                self.cam.relnegy -= 1
                for lines in range(len(self.map)):
                    newMap.append(copy.deepcopy(self.map[lines]))
                    newMap[lines].append("E")

                newMap.append([])

                for i in range(len(newMap)-1):
                    newMap[-1].append("E")
                newMap[-1].append(value)


            else:
                # right side

                for lines in range(len(self.map)):
                    newMap.append(self.map[lines].copy())
                    if lines == y:
                        newMap[lines].append(value)
                    else:
                        newMap[lines].append("E")


        elif y < 0:
            # top side
            self.cam.relposy += 1
            newMap.append([])
            for i in range(len(self.map[0])):
                if i == x:
                    newMap[0].append(value)
                else:
                    newMap[0].append("E")
            for lines in range(len(self.map)):
                newMap.append(copy.deepcopy(self.map[lines]))


        elif  y >= len(self.map):
            # bottom side
            self.cam.relnegy -= 1
            for lines in range(len(self.map)):
                newMap.append(copy.deepcopy(self.map[lines]))

            newMap.append([])

            for n in range(len(self.map[-1])):
                if n == x:
                    newMap[-1].append(value)
                else:
                    newMap[-1].append("E")


        self.map = copy.deepcopy(newMap)
        self.master.map = self.map
        for line in range(len(self.map)):
            print("".join(self.map[line]))
