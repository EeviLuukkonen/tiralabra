# Testausdokumentti

## Yksikkötestaus

![Screenshot from 2021-11-20 16-42-26](https://user-images.githubusercontent.com/75749790/142730467-5c6d2a5f-2ce1-4e7c-90d6-08fdc414036c.png)

Yksikkötestaus on toteutettu unittestin avulla. Testattuna ovat luokat `Labyrintti` ja `BFS`. Haarautumakattavuus on näiden luokkien osalta 98%.
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
