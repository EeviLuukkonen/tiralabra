import random

class Labyrintti():
    def __init__(self, korkeus, leveys):
        self.korkeus = korkeus
        self.leveys = leveys
        self.suuntax = [0, 1, 0, -1]
        self.suuntay = [-1, 0, 1, 0]

    def luo(self):
        self.labyrintti = []
        for i in range(self.korkeus):
            self.labyrintti.append([])
            for _ in range(self.leveys):
                self.labyrintti[i].append("#")
        self.tulosta()
        
    def DFS(self, x, y):
        self.labyrintti[y][x] = "."
        while True:
            naapurilista = []
            for i in range(4):
                nx = x + self.suuntax[i]
                ny = y + self.suuntay[i]
                if nx >= 0 and nx < self.leveys and ny >= 0 and ny < self.korkeus:
                    if self.labyrintti[ny][nx] == "#":
                        ctr = 0
                        for j in range(4):
                            ex = nx + self.suuntax[j]
                            ey = ny + self.suuntay[j]
                            if ex >= 0 and ex < self.leveys and ey >= 0 and ey < self.korkeus:
                                if self.labyrintti[ey][ex] == ".":
                                    ctr += 1
                        if ctr == 1:
                            naapurilista.append(i)
            if len(naapurilista) > 0:
                ir = naapurilista[random.randint(0, len(naapurilista)-1)]
                x += self.suuntax[ir]
                y += self.suuntay[ir]
                self.DFS(x, y)
            else: break
        return self.labyrintti

    def tulosta(self):
        lab = self.DFS(0,0)
        for i in lab:
            print("".join(i))

