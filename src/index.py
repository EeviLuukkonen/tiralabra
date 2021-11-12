from labyrintti import Labyrintti

def main():
    print("Tervetuloa labyrintinratkaisijaan!")
    korkeus = int(input("Anna labyrintin korkeus: "))
    leveys = int(input("Anna labyrintin leveys: "))
    # luo labyrintti
    labyrintti = Labyrintti(korkeus, leveys)
    labyrintti.luo()
    labyrintti.tulosta()
    start = input("Labyrintti luotu. Paina S ratkaistaksesi labyrintin, niin saat tietoja algoritmien tehokkuudesta.")
    print("Lyhyimmän polun pituus on ")



if __name__ == "__main__":
    main()