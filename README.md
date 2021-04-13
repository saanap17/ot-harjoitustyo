# Sanastonharjoittaja, OHTE-harjoitustyö

Ohjelman avulla kieltenopiskelijat voivat luoda itselleen sanalistoja käännöksineen ja terästää muistisolujaan pienen "muistipelin" muodossa. 

## Dokumentaatio

[Tuntikirjanpito](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)  
[Vaatimusmäärittely](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

## Asennus

Asenna ensin riippuvuudet komennolla:

	`poetry install`

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman suoritusta on testattu vain `Python 3.9.0` -versiolla. 
Ohjelman saa suoritettua komennolla:

	`poetry run invoke start`
	
Toistaiseksi tuntemattomasta syystä ylläoleva komento kuitenkin näytti sotkevan jonkin verran ohjelman suoritusta käyttäjän antaessa syötteitä, joten painathan vaikka nuolinäppäimiä etkä esim. enteriä jos ohjelma tulostaa ylimääräisiä rivejä eikä suoritus jatku. Allaolevalla komennolla ohjelma toimi itselläni tosin moitteettomasti:

	`poetry run python src/index.py
	
### Testaus

Testit saa suoritettua komennolla:

	`poetry run invoke test`

Testikattavuusraportin saa HTML-muodossa komennolla:

	`poetry run invoke coverage-report`

Linkki raporttiin löytyy komennon suorituksen jälkeen juurikansion *htmlcov*-kansiosta.