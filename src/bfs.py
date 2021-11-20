from collections import deque

class BFS:
    """Luokka, jossa on leveyshaun toiminnallisuus
    """
    def __init__(self, labyrintti, korkeus, leveys, alku, loppu):
        """ Konstruktori, joka luo labyrinttiolion leveyshakua varten

        Args:
            labyrintti: ratkaistava labyrintti matriisina
            korkeus: labyrintin korkeus
            leveys: labyrintin leveys
            alku: lähtöpiste
            loppu: pättöpiste
            vierailtu: matriisi, johon talletetaan tieto jo vierailluista solmuista
            etaisyys: matriisi, johon talletetaan tieto reitin pituudesta kussakin solmussa
        """
        self.labyrintti = labyrintti
        self.korkeus = korkeus
        self.leveys = leveys
        self.alku = alku # y,x
        self.loppu = loppu # y,x
        self.vierailtu = [[False for _ in range(self.leveys)] for _ in range(self.korkeus)]
        self.etaisyys = [[0 for _ in range(self.leveys)] for _ in range(self.korkeus)]


    def syvyyshaku(self):
        print(self.labyrintti, self.korkeus, self.leveys, self.alku, self.loppu)
        """Metodi joka toteuttaa syvyyshaun

        Returns:
            etaisyys tai -1, jos reittiä ei ole olemassa
        """
        suuntax = [0, 1, 0, -1]
        suuntay = [-1, 0, 1, 0]
        self.vierailtu[self.alku[0]][self.alku[1]] = True
        jono = deque()
        jono.append(self.alku)
        while len(jono) > 0:
            solmu = jono.popleft()
            if solmu[0] == self.loppu[0] and solmu[1] == self.loppu[1]:
                return self.etaisyys[self.loppu[0]][self.loppu[1]]
            for i in range(4):
                naapurix = solmu[1] + suuntax[i]
                naapuriy = solmu[0] + suuntay[i]
                if 0 <= naapurix < self.leveys and 0 <= naapuriy < self.korkeus:
                    if not self.vierailtu[naapuriy][naapurix] and \
                        self.labyrintti[naapuriy][naapurix] == ".":
                        self.vierailtu[naapuriy][naapurix] = True
                        jono.append((naapuriy, naapurix))
                        self.etaisyys[naapuriy][naapurix] = (self.etaisyys[solmu[0]][solmu[1]])+1
        return -1
