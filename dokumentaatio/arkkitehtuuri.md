# Arkkitehtuurikuvaus

[Alustava]

## Käyttöliittymä

Sovelluksessa on toistaiseksi vain tekstikäyttöliittymä.

## Sovelluslogiikka

Sovelluksessa on käyttöliittymä [Interface](https://github.com/saanap17/ot-harjoitustyo/blob/master/src/interface.py), joka vastaa luonnollisesti ohjelman suorituksen näyttämisestä käyttäjälle. Tämän lisäksi meillä on kaksi pakettia, *repositories* ja *entities*.  

[Ohjelman pakkausrakenne](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/package.png)  

'Entities' sisältää oliot *Word* ja *User*, jotka kuvaavat yksittäistä sanaa (käännöksineen) sekä käyttäjää. Kansiossa 'repositories' on kaikki todellinen sovelluslogiikka. *Users* vastaa käyttäjätietokannan ylläpidosta (käyttäjien poisto, lisääminen yms.), ja *Wordlist* vastaavasti huolehtii sanojen ylläpidosta, sanalistojen hakemisesta tiedostosta ynnä muusta.

## Tietojen pysyväistallennus

Sovelluksen käyttäjät talletetaan SQL-tietokantaan taulukkoon *Users*, kun taas sanat säilytetään CSV-tekstitiedostossa muodossa "*käyttäjä,sana,käännös*". Aiemmin esitellyt luokat ovat vastuussa näiden tietokantojen ylläpidosta.


