# Vaatimusmäärittely

[Alustava versio]

## Sovelluksen tarkoitus

Sovelluksen on tarkoitus toimia yksinkertaisena välineenä kieltenopiskelijoille. Käyttäjät voivat kirjautua sisään omilla tunnuksillaan ja sovelluksessa tehdä itselleen sanalistoja ja harjoitella niiden parissa. 


## Käyttäjät

Kaikilla käyttäjillä on yhtäläiset oikeudet sovelluksen käyttöön, eli sovelluksella on vain *normaalikäyttäjiä*. Käyttäjillä on lukuoikeus vain omiin listoihinsa. Mikäli myöhemmin aikaa jää, saatetaan sovellukseen lisätä myös *admin* jolla on oikeudet luoda valmiita listoja (jolloin normaalikäyttäjien ei näitä tarvitsisi itse luoda, vaan esim. opettajan). 

## Käyttöliittymäluonnos

Sovelluksessa on oletuksena vain tekstiliittymä. Sovellukseen saatetaan lisätä graafinen käyttöliittymä, mikäli myöhemmin jää tälle aikaa. Käyttäjälle osoitetaan tekstillä kysymyksiä, joihin syötteen antamalla ohjelman ajo etenee. Käyttäjälle tarjotaan ohjelman jokaisessa vaiheessa ohjeet siitä, millä komennoilla suorituksessa edetään (esim. 'Q = Quit').

## Perusversion tarjoama toiminnallisuus

Kun sovellus käynnistetään, kysyy se onko käyttäjällä olemassaolevia *tunnuksia*. Mikäli ei, ohjataan käyttäjä luomaan itselleen uniikki käyttäjätunnus sekä tälle salasana. Muussa tapauksessa käyttäjä ohjataan kirjautumaan tunnuksillaan. Ohjelma varoittaa mm. jos käyttäjätunnus on jo olemassa tai jos salasana on kirjautuessa väärin.

Kun käyttäjä on kirjautunut sisään, tervehditään käyttäjää ja sovellus antaa listan vaihtoehdoista:
- Sanalistojen hallinta
	- Luo uusi sanalista
	- Lisää sanoja vanhaan listaan
	- Poista sanoja vanhasta listasta
	- Muokkaa sanaa vanhalla listalla
- Harjoittelutila
	- Valitse sanalista, jota haluat harjoitella
	
Sanalistoihin voi lisätä sana-käännös -pareja haluamallaan kielellä. Listan kieli valitaan listaa luodessa.  
Halutessaan harjoitella käyttäjä valitsee yhden luomistaan sanalistoista, jonka jälkeen sovellus syöttää listasta sanoja käyttäjälle yksi kerrallaan. Käyttäjän odotetaan kirjoittavan sovellukselle sanan oikea käännös. Mikäli vastaus on oikein, siirtyy sovellus seuraavaan sanaan. Mikäli käyttäjä vastaa väärin kahdesti, antaa sovellus vinkkinä sanan käännöksen ensimmäisen kirjaimen. Kun sanalista on käyty loppuun, saa käyttäjä onnittelut. Käyttäjä voi keskeyttää suorituksen milloin vain halutessaan. 
	

## Jatkokehitysideoita

Alla mahdollisia ideoita ja lisäyksiä, joita ohjelmaan voisi seuraavien viikkojen aikana tehdä, kun perustoiminnallisuus on saavutettu.
- Graafinen käyttöliittymä
- *Admin*-käyttäjärooli
- Sanoille "prioriteetti"
   - ts. mitä sanoja käyttäjä haluaisi ensisijaisesti listasta harjoitella
- Sanojen dynaaminen lisääminen nk. sanapankkiin
    - Ohjelma voi ehdottaa uusia sanoja listoille
    - Käyttäjä voi listan luomisen sijaan käyttää sanapankkia
- Pisteytysjärjestelmä
    - Aina kun sanan saa oikein, saa pisteitä (*experience points*)
    - Pisteillä käyttäjän taso (*level*) kasvaa
    - Ei oikeaa toiminnallisuutta, vain porkkana käyttäjälle
- Käyttäjän poisto
- Muuta, mitä?