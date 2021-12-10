from collections import deque

class BFS:
    """Luokka, jossa on leveyshaun toiminnallisuus
    """
    def __init__(self, labyrintti):
        self.labyrintti = labyrintti
        self.vierailtu = [
        [False for _ in range(self.labyrintti.leveys)] for _ in range(self.labyrintti.korkeus)]
        self.etaisyys = [
        [0 for _ in range(self.labyrintti.leveys)] for _ in range(self.labyrintti.korkeus)]


    def leveyshaku(self):
        """Metodi joka toteuttaa leveyshaun

        Returns:
            etaisyys tai -1, jos reittiä ei ole olemassa
        """
        suuntax = [0, 1, 0, -1]
        suuntay = [-1, 0, 1, 0]
        self.vierailtu[self.labyrintti.alku[0]][self.labyrintti.alku[1]] = True
        jono = deque()
        jono.append(self.labyrintti.alku)
        while len(jono) > 0:
            solmu = jono.popleft()
            if self.onko_paatepiste(solmu):
                return self.etaisyys[self.labyrintti.loppu[0]][self.labyrintti.loppu[1]]
            for i in range(4):
                naapurix = solmu[1] + suuntax[i]
                naapuriy = solmu[0] + suuntay[i]
                if 0 <= naapurix < self.labyrintti.leveys and \
                    0 <= naapuriy < self.labyrintti.korkeus:
                    if not self.vierailtu[naapuriy][naapurix] and \
                        self.labyrintti.labyrintti[naapuriy][naapurix] == ".":
                        self.vierailtu[naapuriy][naapurix] = True
                        jono.append((naapuriy, naapurix))
                        self.etaisyys[naapuriy][naapurix] = (self.etaisyys[solmu[0]][solmu[1]])+1
        return -1

    def onko_paatepiste(self, solmu):
        """Metodi, joka tarkistaa onko käsiteltävä solmu päätepiste

        Args:
            solmu: käsiteltävä kohta labyrintissa

        Returns:
            True, jos piste on päätepiste, muuten False
        """
        if solmu[0] == self.labyrintti.loppu[0] and solmu[1] == self.labyrintti.loppu[1]:
            return True
        return False
