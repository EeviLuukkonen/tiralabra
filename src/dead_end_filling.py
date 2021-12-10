
class DeadEndFilling:
    def __init__(self, labyrintti):
        self.labyrintti = labyrintti

    def dead_end_filling(self):
        """Metodi joka toteuttaa DEF-algoritmin
        """
        self.labyrintti.labyrintti[self.labyrintti.alku[0]][self.labyrintti.alku[1]] = "alku/loppu"
        self.labyrintti.labyrintti[self.labyrintti.loppu[0]][self.labyrintti.loppu[1]]= "alku/loppu"
        change = True
        while change:
            change = False
            for i in range(self.labyrintti.korkeus):
                for j in range(self.labyrintti.leveys):
                    if self.onko_dead_end(i, j):
                        change = True

    def onko_dead_end(self, i, j):
        """Dead end fillingin apumetodi, joka kertoo onko solmu dead end
        eli onko sen naapureina 3 seinää tai reuna-aluetta,
        sekä muuraa dead-endit umpeen

        Args:
            i: labyrintin x-koordinaatti
            j: labyrintin y-koordinaatti

        Returns:
            True, jos solmu on dead end, muuten False
        """
        laskuri = 0
        if self.labyrintti.labyrintti[i][j] == ".":
            if i>0 and self.labyrintti.labyrintti[i-1][j] == "#":
                laskuri += 1
            if i < self.labyrintti.korkeus-1 and self.labyrintti.labyrintti[i+1][j] == "#":
                laskuri += 1
            if j > 0 and self.labyrintti.labyrintti[i][j-1] == "#":
                laskuri += 1
            if j < self.labyrintti.leveys-1 and self.labyrintti.labyrintti[i][j+1] == "#":
                laskuri += 1
            if i==0:
                laskuri += 1
            if j==0:
                laskuri += 1
            if i==self.labyrintti.korkeus-1:
                laskuri += 1
            if j == self.labyrintti.leveys-1:
                laskuri += 1
            if laskuri == 3:
                self.labyrintti.labyrintti[i][j] = "#"
                return True
        return False

    def polku_labyrinttiin(self):
        """Metodi, joka laskee polun pituuden
        """
        pituus = 0
        for i in range(self.labyrintti.korkeus):
            for j in range(self.labyrintti.leveys):
                if self.labyrintti.labyrintti[i][j] == ".":
                    pituus += 1
                elif self.labyrintti.labyrintti[i][j] == "alku/loppu":
                    pituus +=1
        return pituus -1
