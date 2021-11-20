
# Viikko 3


## Mitä tein:

- Lisäsin ominaisuuden, jolla käyttäjä voi valita alku- ja päätepisteen labyrintissa
- Erotin käyttöjärjestelmän index.py-tiedostosta omaan tiedostoonsa ui.py
- Toteutin BFS-algoritmin toiminnallisuuden
- Yksikkötestit BFS-luokalle ja Labyrinttiluokan testien täydennys
- Yksikkötestauksen ulkopuolelle käyttöjärjestelmä, index.py sekä testitiedostot
- Pylint-korjauksia
- Lisäsin ohjelmaan Invoken: suorituksen, pylintin ja testit voi nyt suorittaa komennolla `poetry run invoke *toiminto*`

## Ensi viikolla aion:

- Toteuttaa toisen vertailtavan algoritmin eli Dead end fillingin
- Mahdollisesti jo koodata aikaominaisuuden, joka mittaa vertailtaviin algoritmeihin kuluvan ajan.

## Viikko kokonaisuudessaan:

Viime viikkoon verrattuna projekti eteni helpommin eikä suurempia ongelmia ilmennyt. 
Virheellisten käyttäjäsyötteiden käsittely tuotti ehkä eniten päänvaivaa, mutta onnistui lopulta melko kivuttomasti.
Syvyyyshaku oli melko yksinkertainen toteuttaa pohjatietojen perusteella.

Tämänhetkinen ohjelma toimii, mutta olen hiukan epävarma siitä, onko sen rakenne riittävän hyvä: onko riippuvuuksien injektointi kunnossa ja ovatko testit tarpeeksi järkeviä. Ensi viikon Dead end filling saattaa myös aiheuttaa harmaita hiuksia, sillä en ole perehtynyt sen toimintaan vielä lainkaan.

Työmäärä: 8h
