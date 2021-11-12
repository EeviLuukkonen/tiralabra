import random

class Labyrintti():
    """Luokka, joka generoi ratkaistavan labyrintin randomized DFS:lla
       käyttäjän syöttämän koon perustella.

    attributes:
    korkeus: labyrintin korkeus
    leveys: labyrintin leveys
    suuntax: syvyyshakua varten x-koordinaatin suunnat ylös, alas, oikealle ja vasemmalle
    suuntay: syvyyshakua varten y-koordinaatin suunnat ylös, alas, oikealle ja vasemmalle
    """
    def __init__(self, korkeus, leveys):
        """Luokan konstruktori

        Args:
            korkeus: labyrintin korkeus
            leveys: labyrintin leveys
        """
        self.korkeus = korkeus
        self.leveys = leveys
        self.suuntax = [0, 1, 0, -1]
        self.suuntay = [-1, 0, 1, 0]
        self.labyrintti = []

    def luo(self):
        """Metodi, joka luo labyrinttiä kuvaavan verkon/matriisin, joka on pelkkää seinää
        """
        for i in range(self.korkeus):
            self.labyrintti.append([])
            for _ in range(self.leveys):
                self.labyrintti[i].append("#")
        
    def DFS(self, x, y):
        """Metodi, jossa toteutetaan labyrintin luominen satunnaistetulla syvyyshaulla

        Args:
            x: Lähtökoordinaatti
            y: Lähtökoordinaatti

        Returns:
            ratkaisuvalmis labyrintti matriisin muodossa
        """
        self.labyrintti[y][x] = "."
        while True:
            naapurilista = []
            for i in range(4):
                uusix = x + self.suuntax[i]
                uusiy = y + self.suuntay[i]
                if uusix >= 0 and uusix < self.leveys and uusiy >= 0 and uusiy < self.korkeus:
                    if self.labyrintti[uusiy][uusix] == "#":
                        ctr = 0
                        for j in range(4):
                            newx = uusix + self.suuntax[j]
                            newy = uusiy + self.suuntay[j]
                            if newx >= 0 and newx < self.leveys and newy >= 0 and newy < self.korkeus:
                                if self.labyrintti[newy][newx] == ".":
                                    ctr += 1
                        if ctr == 1:
                            naapurilista.append(i)
            if len(naapurilista) > 0:
                arvottu_naapuri = naapurilista[random.randint(0, len(naapurilista)-1)]
                x += self.suuntax[arvottu_naapuri]
                y += self.suuntay[arvottu_naapuri]
                self.DFS(x, y)
            else: break
        return self.labyrintti

    def tulosta(self):
        """Metodi, joka tulostaa valmiin labyrintin selkeässä muodossa
        """
        lab = self.DFS(0,0)
        for i in lab:
            print("".join(i))

