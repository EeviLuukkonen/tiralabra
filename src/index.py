from labyrintti import Labyrintti

def main():
    print("Tervetuloa labyrintinratkaisijaan!")
    while True:
        try:
            korkeus = int(input("Anna labyrintin korkeus: "))
            break
        except:
            print("Virheellinen syöte.")
            continue
    while True:
        try:
            leveys = int(input("Anna labyrintin leveys: "))
            break
        except:
            print("Virheellinen syöte.")
            continue
    # luo labyrintti
    labyrintti = Labyrintti(korkeus, leveys)
    labyrintti.luo()
    labyrintti.tulosta()
    print("Labyrintti luotu.")
    while True:
        try:
            alkusyote = input("Valitse labyrintin alkupiste muodossa x,y (piste 0,0 on vasemmalla ylhäällä): ")
            alku = labyrintti.alku_ja_loppu(alkusyote.split(","))
            break
        except:
            print("Kelvoton syöte")
            continue
    while True:
        try:
            loppusyote = input("Valitse loppupiste muodossa x,y: ")
            loppu = labyrintti.alku_ja_loppu(loppusyote.split(","))
            break
        except:
            print("Kelvoton syöte.")
            continue
    print(alku, loppu)
    print("Lyhyimmän polun pituus on ")

if __name__ == "__main__":
    main()
    