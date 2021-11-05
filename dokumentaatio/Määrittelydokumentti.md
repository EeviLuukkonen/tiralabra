## Määrittelydokumentti


Ohjelmassa etsitään lyhyin reitti labyrintin läpi käyttäen kahta eri algoritmia.
Työssä vertaillaan Dijkstran ja IDA*:n algoritmien tehokkuutta löytää lyhyin mahdollinen polku. Tietorakenteista käytössä ovat ainakin pinorakenne ja verkko.

Ohjelmassa on tekstikäyttöliittymä, jossa labyrintti muodostuu #- ja . -merkeistä (# tarkoittaen seinää ja . merkiten polkua). 
Ohjelma kysyy käyttäjältä, minkä kokoinen labyrintti generoidaan. Labyrintin alkupiste on oikea yläkulma ja loppupiste vasen alakulma.

Aikavaativuus Dijkstran algoritmissa on O(|E|+|V|log|V|). IDA*:n aikavaativuus riippuu paljon tilanteesta, mutta on samaa luokkaa Dijkstran algoritmin kanssa. 
Tilavaativuus on molemmissa O(|V|).

Projekti toteutetaan ainoalla hallitsemallani ohjelmointikielellä Pythonilla. Olen toisen vuoden TKT-pääaineopiskelija.

Lähteet:

https://en.wikipedia.org/wiki/Iterative_deepening_A*

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
