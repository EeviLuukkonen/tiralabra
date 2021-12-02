# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma koostuu neljästä eri luokasta:

`LabyrintinLuonti` luo labyrintin käyttäen satunnaistettua syvyyshakua.

`Labyrintti` sisältää käyttäjän syöttämät tiedot ratkaistavasta labyrintista: korkeuden, leveyden alku- ja loppupisteet sekä itse labyrintin matriisina.

`BFS` toteuttaa ensimmäisen vertailtavista algoritmeista, leveyshaun.

`DeadEndFilling` toteuttaa toisen vertailtavista algoritmeista.

Lisäksi ohjelman pääasiallisesta kulusta vastaa tiedosto `index.py`. Testit on toteutettu testiluokilla `TestBFs`, `TestDeadEndFilling` ja `TestLabyrintti`.

## Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)

## Suorituskyky- ja O-analyysivertailu

Syvyyshaku on suorituskyvyltään parempi algoritmi kuin dead-end filling.

## Työn mahdolliset puutteet ja parannusehdotukset

Labyrinttien luomiseen olisin voinut käyttää algoritmia, joka mahdollistaisi suurempien labyrinttien luomisen. Suorituskykyvertailu olisi mielekkäämpää, jos ohjelmassa pystyisi selvittämään esimerkiksi 1000x1000 -kokoisen labyrintin reitin. Tällöin kuitenkin käyttöjärjestelmä olisi tullut toteuttaa jotenkin muuten kuin terminaalissa tai vaihtoehtoisesti jättää visuaalinen puoli ohjelmasta pois.

Lisäksi ohjelman luomat labyrintit ovat "perfect maze" eli niissä on vain yksi polku. Syvyyshaulla voi löytää lyhyimmän polun labyrintista, joissa reittejä on useita. Dead-end filling taas jättää kaikki mahdolliset polut, joista lyhyin olisi täytynyt etsiä erikseen. Tällaiset labyrintit olisivat joka tapauksessa olleet mielenkiintoinen lisä ohjelmalle.

## Lähteet
