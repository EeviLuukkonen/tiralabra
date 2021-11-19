from collections import deque

class BFS:
    def __init__(self, labyrintti, korkeus, leveys, alku, loppu):
        self.labyrintti = labyrintti
        self.korkeus = korkeus
        self.leveys = leveys
        self.alku = alku
        self.loppu = loppu
        self.suuntax = [0, 1, 0, -1]
        self.suuntay = [-1, 0, 1, 0]
        self.vierailtu = [[False for _ in range(self.leveys)] for _ in range(self.korkeus)]
        self.etaisyys = [[0 for _ in range(self.leveys)] for _ in range(self.korkeus)]

    
    def haku(self):
        self.vierailtu[self.alku[0]][self.alku[1]] = True
        jono = deque()
        jono.append(self.alku)
        while len(jono) > 0:
            solmu = jono.popleft()
            if solmu[0] == self.loppu[0] and solmu[1] == self.loppu[1]:
                return self.etaisyys[self.loppu[1]][self.loppu[0]]
            for i in range(4):
                naapurix = solmu[0] + self.suuntax[i]
                naapuriy = solmu[1] + self.suuntay[i]
                if 0 <= naapurix < self.leveys and 0 <= naapuriy < self.korkeus:
                    if not self.vierailtu[naapuriy][naapurix] and self.labyrintti[naapuriy][naapurix] == ".":
                        self.vierailtu[naapuriy][naapurix] = True
                        jono.append((naapurix, naapuriy))
                        self.etaisyys[naapuriy][naapurix] = (self.etaisyys[solmu[1]][solmu[0]])+1

