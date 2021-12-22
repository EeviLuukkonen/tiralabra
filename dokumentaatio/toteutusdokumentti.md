# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelma koostuu neljästä eri luokasta:

`LabyrintinLuonti` luo labyrintin käyttäen satunnaistettua syvyyshakua.

`Labyrintti` sisältää käyttäjän syöttämät tiedot ratkaistavasta labyrintista: korkeuden, leveyden alku- ja loppupisteet sekä itse labyrintin matriisina.

`BFS` toteuttaa ensimmäisen vertailtavista algoritmeista, leveyshaun.

`DeadEndFilling` toteuttaa toisen vertailtavista algoritmeista.

Lisäksi ohjelman pääasiallisesta kulusta vastaa tiedosto `index.py`. Testit on toteutettu testiluokilla `TestBFs`, `TestDeadEndFilling` ja `TestLabyrintti`.

## Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)

Leveyshaku pseudokoodina:

![Screenshot from 2021-12-10 17-25-29](https://user-images.githubusercontent.com/75749790/145598491-0041924f-92bd-4944-8fcd-c916e023d83f.png)

Leveyshaun aikavaativuus on O(n + m), missä n on solmujen määrä ja m kaarien määrä. Se käyttää aputaulukkoa jo vierailluista solmuista, joten sen tilavaativuus on O(n).

Dead-end filling pseudokoodina:

![Screenshot from 2021-12-10 15-52-24](https://user-images.githubusercontent.com/75749790/145598336-322444e7-ec1e-4bdc-9570-60041de1a7e7.png)

Dead-end fillingin aikavaativuus on 2^n. Sen tilavaativuus on O(1), sillä se muuraa syötteenä olevaa labyrinttia eikä tarvitse apumatriisia.

## Suorituskyky- ja O-analyysivertailu

Syvyyshaku on suorituskyvyltään parempi algoritmi kuin dead-end filling. Tämä johtunee siitä, että ohjelmassa syvyyshaku etsii vain polun pituuden, ei reittiä varsinaiseen labyrinttiin.

Lisää suorituskykyvertailua testausdokumentissa.

## Työn mahdolliset puutteet ja parannusehdotukset

Syvyyshaku etsii vain polun pituuden, ei piirrä polkua labyrinttiin. 

Labyrinttien luomiseen olisin voinut käyttää algoritmia, joka mahdollistaisi suurempien labyrinttien luomisen. Suorituskykyvertailu olisi mielekkäämpää, jos ohjelmassa pystyisi selvittämään esimerkiksi 1000x1000 -kokoisen labyrintin reitin. Tällöin kuitenkin käyttöjärjestelmä olisi tullut toteuttaa jotenkin muuten kuin terminaalissa tai vaihtoehtoisesti jättää visuaalinen puoli ohjelmasta pois.

Lisäksi ohjelman luomat labyrintit ovat "perfect maze" eli niissä on vain yksi polku. Syvyyshaulla voi löytää lyhyimmän polun pituuden labyrintista, joissa reittejä on useita. Dead-end filling taas jättää kaikki mahdolliset polut, joista lyhyin olisi täytynyt etsiä erikseen. Tällaiset labyrintit olisivat joka tapauksessa olleet mielenkiintoinen lisä ohjelmalle.

## Lähteet

Antti Laaksonen, Tietorakenteet ja algoritmit
https://iopscience.iop.org/article/10.1088/1742-6596/1569/2/022059/pdf
