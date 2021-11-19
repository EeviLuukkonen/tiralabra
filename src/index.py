from labyrintti import Labyrintti
from ui import ui, valinta
from bfs import BFS

def main():
    leveys, korkeus = ui()
    labyrintti = Labyrintti(korkeus, leveys)
    labyrintti.luo()
    lab_matriisina = labyrintti.tulosta()
    alku, loppu = valinta(labyrintti)
    print(alku, loppu)
    tulos = BFS(lab_matriisina, korkeus, leveys, alku, loppu)
    tulos = tulos.haku()
    print(f"Lyhyimmän polun pituus on {tulos}")

if __name__ == "__main__":
    main()
