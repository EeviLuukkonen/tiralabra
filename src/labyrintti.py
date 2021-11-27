class Labyrintti:
    def __init__(self, labyrintti, korkeus, leveys, alku, loppu):
        """Luokka, joka luo labyrinttiolion ratkaisua varten

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
