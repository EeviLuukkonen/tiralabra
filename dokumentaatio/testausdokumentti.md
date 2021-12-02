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

Alustavan suorituskykytestauksen mukaan dead-end fillingin aikavaativuus on eksponentiaalinen ja syvyyshaun lineaarinen. Algoritmeja on testattu eri syötteiden koolla (1-65). Pienillä syötteillä nopeuserot ovat melko pieniä, mutta ero kasvaa syötteen kasvaessa.

![Screenshot from 2021-12-02 18-07-12](https://user-images.githubusercontent.com/75749790/144458911-8a3860ea-64ce-435a-8696-5bce60aaee8e.png)

![Screenshot from 2021-12-02 18-07-19](https://user-images.githubusercontent.com/75749790/144458888-a6f295a6-5766-440f-a94c-aa969bb07dfe.png)

## Koodin laatu

Pylint-arvosanan voi suorittaa komennolla
```
poetry run invoke lint
```

Pylint-score on tällä hetkellä 9.93.
