# Testausdokumentti

## Yksikkötestaus

![Screenshot from 2021-11-27 16-40-30](https://user-images.githubusercontent.com/75749790/143687531-7b10bd7e-264a-45d7-a59e-9bdc6838bfda.png)

Yksikkötestaus on toteutettu unittestin avulla. Testattuna ovat luokat `Labyrintti`, `LabyrintinLuonti` `DeadEndFilling` ja `BFS`. Haarautumakattavuus on näiden luokkien osalta 99%.
Testauskattavuudesta on jätetty pois `index.py`, käyttöjärjestelmätiedosto `ui.py` sekä testiluokat.

Yksikkötestauksen haarauskattavuusraportin voi suorittaa komennolla 
```
poetry run invoke coverage-report
```

Se löytyy tiedostosta 
```
htmlcov/index.html
```

## Suorituskykytestaus
