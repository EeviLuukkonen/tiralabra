from labyrintin_luonti import LabyrintinLuonti
from labyrintti import Labyrintti
from ui import aloitus, valinta
from bfs import BFS
from dead_end_filling import DeadEndFilling

def main():
    leveys, korkeus = aloitus()
    luonti = LabyrintinLuonti(korkeus, leveys)
    luonti.luo()
    lab_matriisina = luonti.tulosta()
    alku, loppu = valinta(luonti)

    labyrintti = Labyrintti(lab_matriisina, korkeus, leveys, alku, loppu)

    tulos1 = BFS(labyrintti)
    tulos1 = tulos1.syvyyshaku()

    tulos2 = DeadEndFilling(labyrintti)
    tulos2.dead_end_filling()
    tulos2 = tulos2.polun_pituus()
    print(f"Lyhyimmän polun pituus on BFS mukaan {tulos1} ja Dead end fillingin mukaan {tulos2}")

if __name__ == "__main__":
    main()
