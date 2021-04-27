# Arkkitehtuurikuvaus

[Alustava]

## Käyttöliittymä

Sovelluksessa on toistaiseksi vain tekstikäyttöliittymä.

## Sovelluslogiikka

Sovelluksessa on käyttöliittymä [Interface](https://github.com/saanap17/ot-harjoitustyo/blob/master/src/interface.py), joka vastaa luonnollisesti ohjelman suorituksen näyttämisestä käyttäjälle. Tämän lisäksi meillä on kaksi pakettia, *repositories* ja *entities*, sekä palveluluokka *wordapp_service*.

![](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/package.png)  

(Kuva pitää päivittää) 'Entities' sisältää oliot *Word* ja *User*, jotka kuvaavat yksittäistä sanaa (käännöksineen) sekä käyttäjää. Kansiossa 'repositories' on kaikki todellinen sovelluslogiikka. *Users* vastaa käyttäjätietokannan ylläpidosta (käyttäjien poisto, lisääminen yms.), ja *Wordlist* vastaavasti huolehtii sanojen ylläpidosta, sanalistojen hakemisesta tiedostosta ynnä muusta. Käyttöliittymän ja repositorien välillä on luokka *WordAppService*, joka toimii välikätenä eri toimintojen suorituksessa.

## Tietojen pysyväistallennus

Sovelluksen käyttäjät talletetaan SQL-tietokantaan taulukkoon *Users*, kun taas sanat säilytetään CSV-tekstitiedostossa muodossa "*käyttäjä,sana,käännös,kieli*". Aiemmin esitellyt luokat ovat vastuussa näiden tietokantojen ylläpidosta.

## Päätoiminnallisuudet

### Sanapelin pelaaminen

Sanapelin pelaaminen tapahtuu vastaavasti:  
![](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekv_play_game.png) 
Käyttöliittymä pyytää palveluluokkaa tarjoamaan kaikki kielet, joilla pelaaja pystyy pelaamaan. `Wordlist` hakee csv-tiedostosta kaikki kyseisen käyttäjän sanat ja muodostaa listan kaikista käytössä olevista kielistä. `WordAppService` heittää käyttäjälle tiedon siitä, onko mitään kieliä olemassa vaiko ei. Käyttöliittymä ohjastaa käyttäjän luomaan itselleen sanoja, jos niitä ei ole. Käyttäjä syöttää haluamansa kielen listasta, ja palveluluokka noutaa kaikki sanat vastaavalla kielellä. Luokka antaa taas käyttäjälle virheilmoituksen, jos kielellä ei löydy mitään sanoja (esim. kirjoitusvirheen vuoksi). Kun kielellä löytyvät sanat on haettu, siirtyy käyttöliittymä *playing_game()*-näkymään, jossa itse pelaaminen sitten tapahtuu.


