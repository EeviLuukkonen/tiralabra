
def aloitus():
    """UI ohjelman aloitukselle
    """
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
    """Tarkistaa, syöttääkö käyttäjä negatiivisen luvun
    """
    if not koko > 0:
        raise ValueError

def koordinaattien_valinta(labyrintti):
    """UI lähtö- ja päätekoordinaattien valinnalle
    """
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

def tulokset(tulos, kesto1, kesto2, kesto3):
    """UI loppuratkaisun tulostukseen
    """
    print("\nRATKAISU: \n")
    for i in tulos[1]:
        print("".join(i))
    print("\nTULOKSET:")
    print(f"\nLyhyimmän polun pituus on {tulos[0]}.")
    print(f"Ratkaistavan labyrintin generointiin kului satunnaistetulla syvyyshaulla {kesto1} nanosekuntia eli {kesto1/1000000000} sekuntia.")
    print(f"Leveyshaulla ratkaisun saaminen kesti {kesto2} nanosekuntia eli {kesto2/1000000000} sekuntia.")
    print(f"Dead-end filling -algoritmilla ratkaisun saaminen kesti {kesto3} nanosekuntia eli {kesto3/1000000000} sekuntia.\n")
