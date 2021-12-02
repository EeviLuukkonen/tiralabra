# Viikko 5

## Mitä tein:

- Lisäsin ohjelmaan aikaominaisuuden, joka mittaa ratkaisualgoritmeihin kuluvan ajan.
- Pieniä koodimuutoksia ja rakenteellisia parannuksia
- Paransin koodin laatua (pylint)
- Pieniä testimuutoksia
- Suorituskykytestauksen aloittaminen
- Toteutusdokumentin päivitys

## Ensi viikolla aion:

- Labyrinttien luomiseen kuluvan ajan mittaus ja suorituskykytestaus myös tälle
- Lisää suorituskykytestausta ja dokumentointia

## Viikko kokonaisuudessaan:

Aikaominaisuus oli hetkessä valmis ja viikko oli lähinnä yleistä korjailua, testailua ja debuggausta.

Olen epävarma siitä, onko dead-end -filling toteutettu oikein. Sen aikavaativuus on suorituskykytestien mukaan O(n²), 
mutta netistä en löydä vastausta siihen, kuuluisiko aikavaativuuden olla eksponentiaalinen. Oma toteutukseni käy labyrintin läpi kahdesti: ensin etsien dead endit ja 
sitten laskien polun pituuden. Siksi aika kasvaa suuresti isommilla syötteillä.

Tässä vaiheessa projektia huomaan myös, mitä olisin aluksi tehnyt toisin. Kiirehdin algoritmien toimimaan saamisessa koodin laadun kustannuksella, ja 
nyt muuttamisyritykset ovat johtaneet bugeihin. Luokat olisin voinut jakaa pienempiin ja selkeämpiin metodeihin alusta asti.

Muuten kaikki tuntuu olevan ihan hyvällä mallilla.

Työmäärä: 6h
