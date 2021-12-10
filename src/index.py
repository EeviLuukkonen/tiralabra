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

    alkuaika = time.time_ns()
    lab_matriisina = luonti.tulosta()
    loppuaika = time.time_ns()
    kesto1 = loppuaika-alkuaika
    alku, loppu = ui.koordinaattien_valinta(luonti)

    labyrintti = Labyrintti(lab_matriisina, korkeus, leveys, alku, loppu)
    tulos1 = BFS(labyrintti)
    tulos2 = DeadEndFilling(labyrintti)

    alkuaika = time.time_ns()
    tulos1 = tulos1.leveyshaku()
    loppuaika = time.time_ns()
    kesto2 = loppuaika-alkuaika

    alkuaika = time.time_ns()
    tulos2.dead_end_filling()
    loppuaika = time.time_ns()
    kesto3 = loppuaika-alkuaika
    tulos2 = tulos2.polku_labyrinttiin()

    ui.tulos(tulos2, kesto1, kesto2, kesto3)


if __name__ == "__main__":
    main()
