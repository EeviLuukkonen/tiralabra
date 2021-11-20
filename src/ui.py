
def ui():
    print("Tervetuloa labyrintinratkaisijaan!")
    while True:
        try:
            leveys = int(input("Anna labyrintin leveys: "))
            break
        except ValueError:
            print("Virheellinen syöte.")
            continue
    while True:
        try:
            korkeus = int(input("Anna labyrintin korkeus: "))
            break
        except ValueError:
            print("Virheellinen syöte.")
            continue

    return leveys, korkeus


def valinta(labyrintti):
    print("Labyrintti luotu.")
    while True:
        try:
            alkusyote = input("Valitse labyrintin alkupiste muodossa x,y (piste 0,0 on vasemmalla ylhäällä): ")
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
