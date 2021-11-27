
class DeadEndFilling:
    def __init__(self, labyrintti, korkeus, leveys, alku, loppu):
        """Konstruktori, joka luo labyrinttiolion ratkaisua varten

        Args:
            labyrintti: ratkaistava labyrintti matriisina
            korkeus: labyrintin korkeus
            leveys: labyrintin leveys
            alku: lähtöpiste
            loppu: pättöpiste

        """
        self.labyrintti = labyrintti
        self.korkeus = korkeus
        self.leveys = leveys
        self.alku = alku # y,x
        self.loppu = loppu # y,x

    def dead_end_filling(self):
        """Metodi joka toteuttaa DEF algoritmin
        """
        self.labyrintti[self.alku[0]][self.alku[1]] = "alku/loppu"
        self.labyrintti[self.loppu[0]][self.loppu[1]] = "alku/loppu"
        change = True
        while change:
            change = False
            for i in range(self.korkeus):
                for j in range(self.leveys):
                    if self.onko_dead_end(i, j):
                        change = True
        for i in range(self.korkeus):
            for j in range(self.leveys):
                if self.labyrintti[i][j] == "." or self.labyrintti[i][j] == "alku/loppu":
                    self.labyrintti[i][j] = "polku"

    def onko_dead_end(self, i, j):
        """Dead end filling apumetodi, joka kertoo onko solmu dead end
        eli onko sen naapureina 3 seinää

        Args:
            i: labyrintin x-koordinaatti
            j: labyrintin y-koordinaatti

        Returns:
            True, jos solmu on dead end, muuten False
        """
        laskuri = 0
        if self.labyrintti[i][j] == ".":
            if i>0 and self.labyrintti[i-1][j] == "#":
                laskuri += 1
            if i < self.korkeus-1 and self.labyrintti[i+1][j] == "#":
                laskuri += 1
            if j > 0 and self.labyrintti[i][j-1] == "#":
                laskuri += 1
            if j < self.leveys-1 and self.labyrintti[i][j+1] == "#":
                laskuri += 1
            if i==0:
                laskuri += 1
            if j==0:
                laskuri += 1
            if i==self.korkeus-1:
                laskuri += 1
            if j == self.leveys-1:
                laskuri += 1
            if laskuri == 3:
                self.labyrintti[i][j] = "#"
                return True
        return False

    def polun_pituus(self):
        """Metodi, joka käy läpi labyrintin algoritmin jälkeen ja laskee polun pituuden

        Returns:
            polun pituus integraalina
        """
        pituus=0
        for i in range(self.korkeus):
            for j in range(self.leveys):
                if self.labyrintti[i][j] == "polku":
                    pituus += 1
        return pituus-1
