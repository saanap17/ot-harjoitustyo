# Testausdokumentti

Ohjelmaa on testattu manuaalisen, luonnollisen käytön lisäksi automatisoiduilla *unittest*-testeillä.

## Sovelluslogiikka

Ohjelmassa sovelluslogiikasta vastaa *WordAppService*-luokka, jonka testiluokka on [TestWordAppService](https://github.com/saanap17/ot-harjoitustyo/blob/master/src/tests/wordapp_service_test.py). Pytestin *fixtures*-funktion avulla testiluokka luo ennen jokaisen testin suorittamista väliaikaisen tietokannan ja sanatiedoston ja poistaa nämä testauksen päätteeksi.

## Repositoriot

Ohjelmassa on kaksi repositoriota, *Users* ja *Wordlist*, joilla on testiluokat [TestWordlist](https://github.com/saanap17/ot-harjoitustyo/blob/master/src/tests/wordlist_test.py) ja [TestUsers](https://github.com/saanap17/ot-harjoitustyo/blob/master/src/tests/users_test.py). Jälleen *fixtures*-funktion avulla kumpikin testiluokka luo ennen kutakin testiä väliaikaiset tietorakenteet testausta varten ja poistaa nämä myöhemmin.

## Testikattavuus

![](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/testaus.png) 

Ohjelman testikattavuus (poislukien käyttöliittymään kuuluva lähdekoodi) on 98 prosenttia. Automatisoidut testit eivät ota huomioon käyttöliittymän käyttöön kuuluvia virheitä, eli esimerkiksi ei-toivottuihin syötemuotoihin (esim. string-syötteet kokonaislukujen sijaan) ei testeissä oteta kantaa. 