from collections import deque

class BFS:
    """Luokka, jossa on leveyshaun toiminnallisuus
    """
    def __init__(self, labyrintti_olio):
        self.labyrintti_olio = labyrintti_olio
        self.vierailtu = [
        [False for _ in range(self.labyrintti_olio.leveys)] for _ in range(self.labyrintti_olio.korkeus)]
        self.etaisyys = [
        [0 for _ in range(self.labyrintti_olio.leveys)] for _ in range(self.labyrintti_olio.korkeus)]


    def syvyyshaku(self):
        """Metodi joka toteuttaa syvyyshaun

        Returns:
            etaisyys tai -1, jos reittiä ei ole olemassa
        """
        suuntax = [0, 1, 0, -1]
        suuntay = [-1, 0, 1, 0]
        self.vierailtu[self.labyrintti_olio.alku[0]][self.labyrintti_olio.alku[1]] = True
        jono = deque()
        jono.append(self.labyrintti_olio.alku)
        while len(jono) > 0:
            solmu = jono.popleft()
            if solmu[0] == self.labyrintti_olio.loppu[0] and solmu[1] == self.labyrintti_olio.loppu[1]:
                return self.etaisyys[self.labyrintti_olio.loppu[0]][self.labyrintti_olio.loppu[1]]
            for i in range(4):
                naapurix = solmu[1] + suuntax[i]
                naapuriy = solmu[0] + suuntay[i]
                if 0 <= naapurix < self.labyrintti_olio.leveys and 0 <= naapuriy < self.labyrintti_olio.korkeus:
                    if not self.vierailtu[naapuriy][naapurix] and \
                        self.labyrintti_olio.labyrintti[naapuriy][naapurix] == ".":
                        self.vierailtu[naapuriy][naapurix] = True
                        jono.append((naapuriy, naapurix))
                        self.etaisyys[naapuriy][naapurix] = (self.etaisyys[solmu[0]][solmu[1]])+1
        return -1
