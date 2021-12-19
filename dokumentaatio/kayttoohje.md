# Käyttöohje

## Ohjelman suoritus

Asenna riippuvuudet komennolla
```
poetry install
```
Käynnistä ohjelma komennolla
```
poetry run invoke start
```

Testit voidaan halutessaan suorittaa komennolla
```
poetry run invoke test
```

## Syöteohjeet

Ohjelma kysyy käyttäjältä labyrintin korkeutta ja leveyttä. Ne syötetään positiivisena kokonaislukuna (maksimikoko noin 65x65) ja painetaan enter.

Seuraavaksi ohjelma kysyy aloituspistettä sekä lopetuspistettä. Syötä ne muodossa `x,y`, jossa piste `0,0` on labyrintin vasen yläkulma.
Varmista, että luodussa labyrintissa on näissä kohdassa piste, muuten syöte ei kelpaa.

Seuraavaksi ohjelma suorittaa algoritmit ja tulostaa näytölle polun pituuden, analyysin algoritmien nopeudesta sekä polun visualisoinnin.
