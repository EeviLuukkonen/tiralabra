from labyrintti import Labyrintti
from ui import ui, valinta
from bfs import BFS
from dead_end_filling import DeadEndFilling

def main():
    leveys, korkeus = ui()
    labyrintti = Labyrintti(korkeus, leveys)
    labyrintti.luo()
    lab_matriisina = labyrintti.tulosta()
    alku, loppu = valinta(labyrintti)
    tulos = BFS(lab_matriisina, korkeus, leveys, alku, loppu)
    tulos2 = DeadEndFilling(lab_matriisina,korkeus,leveys,alku,loppu)
    tulos = tulos.syvyyshaku()
    tulos2.dead_end_filling()
    tulos2 = tulos2.polun_pituus()
    print(f"Lyhyimmän polun pituus on {tulos} eli {tulos2}")

if __name__ == "__main__":
    main()
