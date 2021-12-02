
def aloitus():
    print("Tervetuloa labyrintinratkaisijaan!")
    while True:
        try:
            leveys = int(input("Anna labyrintin leveys: "))
            labyrintin_koon_syote_kelpaa(leveys)
            break
        except ValueError:
            print("Virheellinen syöte.")
            continue
    while True:
        try:
            korkeus = int(input("Anna labyrintin korkeus: "))
            labyrintin_koon_syote_kelpaa(korkeus)
            break
        except ValueError:
            print("Virheellinen syöte.")
            continue

    return leveys, korkeus

def labyrintin_koon_syote_kelpaa(koko):
    if not koko > 0:
        raise ValueError

def koordinaattien_valinta(labyrintti):
    print("Labyrintti luotu.")
    while True:
        try:
            alkusyote = input(
                "Valitse labyrintin alkupiste muodossa x,y (piste 0,0 on vasemmalla ylhäällä): ")
            alku = labyrintti.alku_ja_loppu(alkusyote.split(","))
            break
        except ValueError:
            print("Kelvoton syöte")
            continue
    while True:
        try:
            loppusyote = input("Valitse loppupiste muodossa x,y: ")
            loppu = labyrintti.alku_ja_loppu(loppusyote.split(","))
            break
        except ValueError:
            print("Kelvoton syöte.")
            continue

    return alku, loppu

def tulos(polun_pituus, kesto1, kesto2):
    print("\nTULOKSET:")
    print(f"\nLyhyimmän polun pituus on {polun_pituus}.")
    print(f"Syvyyshaulla ratkaisun saaminen kesti {kesto1} nanosekuntia.")
    print(f"Dead-end filling -algoritmilla ratkaisun saaminen kesti {kesto2} nanosekuntia.\n")
