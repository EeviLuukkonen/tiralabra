import random

class Labyrintti():
    """Luokka, joka generoi ratkaistavan labyrintin randomized dfs:lla
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

    def dfs(self, x, y):
        """Metodi, jossa toteutetaan labyrintin luominen \
            rekursiivisesti satunnaistetulla syvyyshaulla

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
                naapurix = x + self.suuntax[i]
                naapuriy = y + self.suuntay[i]
                if naapurix >= 0 and naapurix < self.leveys and \
                     naapuriy >= 0 and naapuriy < self.korkeus:
                    if self.labyrintti[naapuriy][naapurix] == "#":
                        ctr = 0
                        for j in range(4):
                            uusix = naapurix + self.suuntax[j]
                            uusiy = naapuriy + self.suuntay[j]
                            if uusix >= 0 and uusix < self.leveys and \
                            uusiy >= 0 and uusiy < self.korkeus:
                                if self.labyrintti[uusiy][uusix] == ".":
                                    ctr += 1
                        if ctr == 1:
                            naapurilista.append(i)
            if len(naapurilista) > 0:
                arvottu_naapuri = naapurilista[random.randint(0, len(naapurilista)-1)]
                x += self.suuntax[arvottu_naapuri]
                y += self.suuntay[arvottu_naapuri]
                self.dfs(x, y)
            else: break
        return self.labyrintti

    def tulosta(self):
        """Metodi, joka tulostaa valmiin labyrintin selkeässä muodossa

        Returns: ratkaisuvalmis labyrintti matriisin muodossa
        """
        lab = self.dfs(0,0)
        for i in lab:
            print("".join(i))
        return lab

    def alku_ja_loppu(self, koordinaattilista): # ["10","0"]
        """Metodi, joka testaa onko käyttäjän syöttämät koordinaatit kelvollisia

        Args:
            koordinaattilista: käyttäjän syöttämät koordinaatit listana

        Raises:
            ValueError: jos syötteessä on liikaa lukuja
            ValueError: jos x-koordinaatti on isompi kuin labyrintin leveys
            ValueError: jos y-koordinaatti on isompi kuin labyrintin korkeus
            ValueError: jos koordinaatin osoittama kohta on seinää

        Returns:
            kelvollinen koordinaatti tuplena
        """
        if not len(koordinaattilista) == 2:
            raise ValueError
        if not int(koordinaattilista[0]) <= self.leveys-1:
            raise ValueError
        if not int(koordinaattilista[1]) <= self.korkeus-1:
            raise ValueError
        if not self.labyrintti[int(koordinaattilista[1])][int(koordinaattilista[0])] == ".":
            raise ValueError

        return (int(koordinaattilista[1]), int(koordinaattilista[0]))
