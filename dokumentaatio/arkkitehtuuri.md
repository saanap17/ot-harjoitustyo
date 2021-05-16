# Arkkitehtuurikuvaus

## Käyttöliittymä

Sovelluksessa on tekstikäyttöliittymä, jossa navigoiminen näkymästä toiseen tapahtuu käyttäjän antamilla syötteillä.

## Rakenne

![](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/structure.png) 

Sovellus on rakennettu kolmitasoisen kerrosarkkitehtuurin mukaisesti, eli sovelluslogiikka on jaoteltu kolmeen luokkaan: *entities*, *repositories* ja *services*. Pakkaus *entities* vastaa sovelluksessa käytettävien olioiden rakenteesta, pakkauksen *repositories* luokat vastaavat tietorakenteiden ylläpidosta ja hauista, kun taas *services* toimii repositorioiden ja käyttöliittymän välissä. Käyttöliittymän (*ui*) toiminta on näistä erillinen, ja ne vastaavat täysin käyttäjän kanssa kommunikoimisesta.

## Sovelluslogiikka

Sovelluksessa on käyttöliittymä [Interface](https://github.com/saanap17/ot-harjoitustyo/blob/master/src/interface.py), joka vastaa luonnollisesti ohjelman suorituksen näyttämisestä käyttäjälle. Tämän lisäksi meillä on kaksi pakettia, *repositories* ja *entities*, sekä palveluluokka *wordapp_service*.

![](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/package.png)  

'Entities' sisältää oliot *Word* ja *User*, jotka kuvaavat yksittäistä sanaa (käännöksineen ja kielineen) sekä käyttäjää (nimi ja salasana). Kansiossa 'repositories' on kaikki todellinen sovelluslogiikka. *Users* vastaa käyttäjätietokannan ylläpidosta (käyttäjien poisto, lisääminen yms.), ja *Wordlist* vastaavasti huolehtii sanojen ylläpidosta, sanalistojen hakemisesta tiedostosta ynnä muusta. Käyttöliittymän ja repositorien välillä on luokka *WordAppService*, joka toimii välikätenä eri toimintojen suorituksessa (esim. käyttäjän kokemuspisteiden nouto, olemassaolevien sanojen editointi). Käyttöliittymä on jaettu kahteen osaan, *Interface* ja *Commands*, joista *Commands* vastaa laajaosaisten komentojen suorituksesta ja kommunikoi myös palveluluokan kanssa.

## Tietojen pysyväistallennus

Sovelluksen käyttäjät talletetaan SQL-tietokantaan taulukkoon *Users* muodossa *nimi|salasana|kokemuspisteet*, kun taas sanat säilytetään CSV-tekstitiedostossa muodossa "*käyttäjä,sana,käännös,kieli*". Aiemmin esitellyt luokat ovat vastuussa näiden tietokantojen ylläpidosta. Tietokanta ja tiedosto löytyvät oletuksena juurikansion *data*-kansiosta, mutta tämä on muutettavissa editoimalla *index.py*-tiedostoa.

## Päätoiminnallisuudet

Ohjelmassa on muutamia päätoiminnallisuuksia:
- Käyttäjäkohtaiset
	- Käyttäjän luominen
	- Sisäänkirjautuminen
	- Käyttäjän poisto
- Sanakohtaiset
	- Sanan luominen
	- Sanan poistaminen
	- Sanan muokkaaminen
- Sanapelin pelaaminen

Alla kuvataan sekvenssikaavioiden avulla muutamaa näistä toiminnallisuuksista.

### Käyttäjän luominen ja sisäänkirjautuminen

![](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekv_add_user.png) 

Käyttäjä antaa käyttöliittymässä *create_user()*-näkymässä haluamansa käyttäjänimen ja salasanan, jonka käyttöliittymä taas antaa `WordAppService`-palveluluokalle. Palveluluokka lähettää taas käyttäjäolion `Users`-repositoriolle, joka tarkistaa tietokannasta onko nimimerkkiä jo olemassa. Käyttöliittymälle palautetaan *True*, jos lisääminen onnistui. Käyttäjän kirjautuessa sisään `WordAppService` lähettää taas kutsun repositoriolle, joka tarkistaa tietokannasta onko vastaavalle käyttäjänimelle olemassa salasanaa, joka vastaa annettua. Jälleen palautetaan käyttöliittymälle *True*, mikäli kirjautuminen onnistuu. Käyttöliittymä siirtyy *logged_in()*-näkymään.

### Sanapelin pelaaminen

Sanapelin pelaaminen tapahtuu vastaavasti:  
![](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekv_play_game.png) 

Käyttöliittymä pyytää palveluluokkaa tarjoamaan kaikki kielet, joilla pelaaja pystyy pelaamaan. `Wordlist` hakee csv-tiedostosta kaikki kyseisen käyttäjän sanat ja muodostaa listan kaikista käytössä olevista kielistä. `WordAppService` heittää käyttäjälle tiedon siitä, onko mitään kieliä olemassa vaiko ei. Käyttöliittymä ohjastaa käyttäjän luomaan itselleen sanoja, jos niitä ei ole. Käyttäjä syöttää haluamansa kielen listasta, ja palveluluokka noutaa kaikki sanat vastaavalla kielellä. Luokka antaa taas käyttäjälle virheilmoituksen, jos kielellä ei löydy mitään sanoja (esim. kirjoitusvirheen vuoksi). Kun kielellä löytyvät sanat on haettu, siirtyy käyttöliittymä *playing_game()*-näkymään, jossa itse pelaaminen sitten tapahtuu.

### Sanan muokkaaminen

![](https://github.com/saanap17/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekv_edit_word.png) 

Sanojen lisääminen ja poisto on melko suoraviivaista, mutta sanaa muokatessa tapahtuu jo hieman enemmän. Käyttöliittymästä kutsutaan ensin `WordAppService`-palveluluokkaa, joka pyytää `Wordlist`-repositoriolta käyttäjälle tarjolla olevia sanoja. Käyttäjä valitsee sanan, jota haluaa editoida, jolloin palveluluokka kutsuu repositoriota poistamaan vanhan sanan sekä lisäämään uuden sanan tietokantaan halutuilla spekseillä. Palveluluokka palauttaa käyttöliittymälle *True*, mikäli sanan muokkaus onnistuu. Sanaa ei muokata esimerkiksi tapauksessa, jossa jokin syöte on tyhjä.


