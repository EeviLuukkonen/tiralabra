import time
from labyrintin_luonti import LabyrintinLuonti
from labyrintti import Labyrintti
import ui
from bfs import BFS
from dead_end_filling import DeadEndFilling

def main():
    leveys, korkeus = ui.aloitus()
    luonti = LabyrintinLuonti(korkeus, leveys)
    luonti.luo()
    lab_matriisina = luonti.tulosta()
    alku, loppu = ui.koordinaattien_valinta(luonti)

    labyrintti = Labyrintti(lab_matriisina, korkeus, leveys, alku, loppu)
    tulos1 = BFS(labyrintti)
    tulos2 = DeadEndFilling(labyrintti)

    alku = time.time_ns()
    tulos1 = tulos1.syvyyshaku()
    loppu = time.time_ns()
    kesto1 = loppu-alku

    alku = time.time_ns()
    tulos2 = tulos2.dead_end_filling()
    loppu = time.time_ns()
    kesto2 = loppu-alku

    ui.tulos(tulos2, kesto1, kesto2)


if __name__ == "__main__":
    main()
