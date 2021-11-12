from labyrintti import Labyrintti

def main():
    print("Tervetuloa labyrintinratkaisijaan!")
    korkeus = int(input("Anna labyrintin korkeus: "))
    leveys = int(input("Anna labyrintin leveys: "))
    # luo labyrintti
    labyrintti = Labyrintti(korkeus, leveys)
    labyrintti.luo()
    labyrintti.tulosta()
    start = input("Labyrintti luotu. Valitse labyrintin alkupiste muodossa (x,y):")
    print("Lyhyimmän polun pituus on ")

if __name__ == "__main__":
    main()
    