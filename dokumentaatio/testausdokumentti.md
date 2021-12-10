# Testausdokumentti

## Yksikkötestaus

![Screenshot from 2021-12-02 17-49-54](https://user-images.githubusercontent.com/75749790/144456011-f31d1f6f-e217-4f4d-91dd-0e686251f310.png)

Yksikkötestaus on toteutettu unittestin avulla. Testattuna ovat testiluokat sekä sovelluslogiikan luokat `Labyrintti`, `LabyrintinLuonti` `DeadEndFilling` ja `BFS`. Haarautumakattavuus on näiden luokkien osalta 98%.
Testauskattavuudesta on jätetty pois `index.py` sekä käyttöjärjestelmätiedosto `ui.py`.

Yksikkötestauksen haarauskattavuusraportin voi suorittaa komennolla 
```
poetry run invoke coverage-report
```

Se löytyy tiedostosta 
```
htmlcov/index.html
```

## Suorituskykytestaus

Algoritmeja on testattu erikokoisilla n * n syötteillä (1-65). Pienillä syötteillä nopeuserot ovat melko pieniä, mutta ero kasvaa syötteen kasvaessa. Testattavana ovat sekä ratkaisualgoritmit että generoiva algoritmi.

![Screenshot from 2021-12-10 17-11-37](https://user-images.githubusercontent.com/75749790/145596958-d3f78f49-cc54-4404-ac32-e61ec32baed8.png)
![Screenshot from 2021-12-10 17-16-43](https://user-images.githubusercontent.com/75749790/145597187-bd7e63ee-fb69-44fb-87de-9d785f43915a.png)
![Screenshot from 2021-12-10 17-16-54](https://user-images.githubusercontent.com/75749790/145597199-54155f53-6aac-4a2f-934a-c0e425fe8a8f.png)
![Screenshot from 2021-12-10 17-17-00](https://user-images.githubusercontent.com/75749790/145597225-78f3398d-6f18-4119-9f49-e9570ee00ce9.png)

## Koodin laatu

Pylint-arvosanan voi suorittaa komennolla
```
poetry run invoke lint
```

Pylint-score on tällä hetkellä 9.93.
