# Käyttöohje

Projektin uusimman julkaisun saat ladattua [tältä](https://github.com/saanap17/ot-harjoitustyo/releases) sivulta.

## Konfigurointi

Mikäli missään vaiheessa haluat muokata ohjelman käyttämää dataa ohjelman ulkopuolella, löytyvät *data*-kansiosta käyttäjien tiedot SQLite-tietokannasta sekä sanalistojen sisällöt csv-tekstitiedostosta. Ohjelma luo nämä tiedostot automaattisesti käynnistyksen yhteydessä. Tietorakenteiden nimiä ei valitettavasti voi muuttaa ohjelmasta käsin, mutta editoimalla *index.py*-tiedostoa voi tietorakenteiden nimiä ja osoitteita muuttaa vapaasti.

## Ohjelman käynnistäminen

Ohjelman juurikansiossa suoritetaan ensin seuraava komento:

	poetry install

Tämän jälkeen ohjelma käynnistetään komennolla:

	poetry run python src/index.py

Ohjelman _voi_ käynnistää komennolla `poetry run invoke start`, mutta syötteet eivät toimi kunnolla joten käytäthän vain tätä edeltävää komentoa sataprosenttisen toimivuuden säilyttämiseksi.

## Ohjelmassa navigoiminen

Ohjelma aukeaa aloitusvalikkoon ja tarjoaa komentoja, joilla ohjelmassa voidaan navigoida. Kukin kirjain (esim. "Q = Quit") vastaa siis syötettä, joka ohjelmalle on kirjoitettava. Enteriä painamalla ohjelman suoritus etenee. Mikäli unohdat komennot, voit missä vain vaiheessa kirjoittaa ohjelmalle komennon `help`, jolloin ohjelma tulostaa käytössä olevat komennot uudestaan. Siirtyminen taaksepäin ohjelmassa tapahtuu joko syöttellä `b` tai `back`, riippuen suoritusvaiheesta - ohjelma informoi myös tästä.

