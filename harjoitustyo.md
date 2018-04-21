---
layout: default
title: Harjoitustyöohje / JODA 2018
year: 2018
---

Ohje viimeistellään luentoviikon 4.4 aikana. Ilmoita epäjohdonmukaisuuksista [Jukalle](http://www.tut.fi/fi/henkilokortti/index.htm?id=8883).

Johdanto datatieteeseen -harjoitustyössä käydään läpi datatiedeprojektin keskeiset vaiheet.
Voit valita aiheen ja datalähteen vapaasti.
Saat pisteitä julkaisemalla Slackissa kuvauksen [harjoitustyön eri vaiheiden](https://jodatut.github.io/2018/harjoitustyo/) toteutuksesta.
Eräs vaihtoehto on Airbnb-aineiston analyysi datatieteen menetelmin.
Voit vaikkapa toteuttaa hintaennustimen [esimerkkianalyysiä](https://mapr.com/blog/predicting-airbnb-listing-prices-scikit-learn-and-apache-spark/) soveltamalla.

## Vaiheet ja pisteet

| Vaihe  | 1 piste  | 2 pistettä   | 3 pistettä  |
|--------|---|---|---|
| Kehitysympäristö   | Anaconda omalla koneella | [CSC Notebooks](https://www.csc.fi/web/blog/post/-/blogs/notebooks-enemman-aikaa-opetuksen-ytimelle) | Oma pilviympäristö |
| Datan kerääminen   | Valmis datasetti         | Datasettien yhdistely | Oma datasetti |   
| Datan jalostaminen | Siistiä lähtödataa       | Siivoaminen ja piirteiden erottaminen | Web DAD |   
| Datan kuvaileminen | Standardikuvaajat        | Monipuolinen visuaalinen raportti | Vuorovaikutteinen Web-kojelauta |   
| Koneoppiminen      | Lineaarinen regressio    | Monimuuttujaregressio | Hybriditoteutus |   
| Toimeenpano        | Staattinen raportti      | Vuorovaikutteinen raportti  | Ohjaava analytiikka |  

**Kehitysympäristö**
Perusta kehitysympäristö projektiasi varten.
Anacondan asentaminen omalle koneelle on suoraviivaisin vaihtoehto.
CSC Notebooks -palvelun käyttäminen mahdollistaa Jupyterin opettelun.
Voit myös rakentaa oman pilvipalvelupohjaisen analytiikkaympäristösi.
Esimerkiksi [Google Cloud Platform](https://cloud.google.com/) viimeksi mainittuun kategoriaan.

**Datan kerääminen**
Suoraviivaisinta on lähteä liikkeelle valmiista datasta.
Ehdotamme [Inside Airbnb](http://insideairbnb.com/) -datasetin käyttöä.
Analytiikkavälineet tarjoavat myös puhdasta esimerkkidataa, katso vaikkapa
[IBM Watsonin tarjonta](https://www.ibm.com/communities/analytics/watson-analytics-blog/guide-to-sample-datasets/).
Datasettien yhdistely tuo mukanaan lisähaastetta.
Voit myös kerätä oman datasetin Web-ryöminnän, ruudunraavinnan tai API-ohjelmoinnin keinoin.

**Datan jalostaminen**
Analyysi edellyttää aina datan jalostamista ja siivoamista.
Piirteiden erottaminen on keskeisessä roolissa tätä vaihetta.
Siistissä datassa piirteet ovat pääosin valmiina,
mutta usein niiden erottaminen edellyttää lisätyötä.
[Web DAD](https://www.datasciencecentral.com/profiles/blogs/data-scientist-versus-data-engineer)
viittaa tässä itse kerätyn datan jalostamiseen analyysiä varten.

**Datan kuvaileminen**
Datan eksploratiivinen ja kuvaileva analyysi on välttämätöntä analytiikkaprojektin laadun takaamiseksi.
Toteuta minimissään joukko datan ominaisuuksia kuvaavia visualisointeja.
Pandas tarjoaa kätevät apuvälineet aikajanoista pistekaaviomatriiseihin.
Halutessasi voit hyödyntää Web-ohjelmointiosaamistasi ja
toteuttaa monipuolisen visuaalisen raportin tai
vuorovaikutteisen Web-kojelaudan.

**Koneoppiminen**
Kahden muuttujan välistä suhdetta tarkasteleva lineaarinen regressio on
yksinkertaisin koneoppimismenetelmä.
Voit vaikkapa etsiä Airbnb-asunnon hintaa parhaiten selvittävät muuttujat.
Monimuuttujaregressio mahdollistaa esimerkiksi
[Airbnb-asunnon hinnan ennustamisen](https://mapr.com/blog/predicting-airbnb-listing-prices-scikit-learn-and-apache-spark/).
Käytännön sovellukset ovat tyypillisesti useita eri menetelmiä yhdisteleviä hybridejä.

**Toimeenpano**
Datatiedeprojekti tähtää toimenpiteisiin.
Voit esimerkiksi ehdottaa liiketoimintaan liittyviä toimenpiteitä
(kuvitteelliselle tai todelliselle) kohdehenkilölle.
Miten Airbnb-asuntojen sijaintia voisi hyödyntää kahvilaketjun toimipisteiden valinnassa?
Miten Airbnb-asunnosta olisi mahdollista saada nykyistä parempi päivähinta?
Staattinen raportti voi olla tekstiä ja kuvia yhdistelevä tuotos.
Vuorovaikutteisen raportin avulla käyttäjä voi myös itse perehtyä tekemääsi analyysiin.
Suosittelujärjestelmä tai Airbnb-asunnon hinnan käyttäjän syöttämien
ominaisuuksien perusteella määrittelevä sovellus ovat esimerkkejä ohjaavasta analytiikasta.

## Pisteiden kerääminen

Pisteiden kerääminen tapahtuu julkaisemalla kunkin vaiheen kuvaus
toteutuskerran Slackissä **maanantaihin 30. huhtikuuta kello 15 mennessä**.
Pisteet myönnetään täysimääräisenä kun minimivaatimukset täyttyvät ja
palautus on tehty annetun aikataulun puitteissa.

Aihepiiriin jo ennen toteutuskerran alkua perehtyneitä suorittajia kannustetaan
toteuttamaan etenkin ensimmäiset vaiheet annettua aikataulua rivakammin ja
siten jakamaan osaamistaan muille.
Erityisen informatiiviset palautukset huomioidaan kokonaissuoritusta arvosteltaessa.

Yhden vaiheen kuvaus sisältää seuraavat pääkohdat:

1. tiivis kuvaus toteutuksesta,
1. muutamia otteita toteutuksesta (ohjelmakoodista, asetustiedostoista, ...),
1. listaus (siis lista linkkejä) ohjeista tai esimerkiksi verkkolähteistä jotka olivat erityisesti hyödyksi tehtävää tehdessä ja
1. listaus vähintään kolmesta asiasta, jotka olivat valitulla teknologialla joko erityisen helppoja tai vastaavasti hankaloittivat työtäsi merkittävästi.

Kun viesti on valmis, julkaise se Slackissä.
Halutessasi voit kirjoittaa kuvauksen esimerkiksi dillinger.io-palvelulla ja liittää sen Slackiin-viestiin PDF-muodossa.
Löydät Slackistä erillisen kanavan kullekin eri vaiheelle.
Lisää Slack-viestiin sopivat hashtagit (esimerkiksi #jupyter #scikitlearn #pandas) kuvaamaan toteutuksessa käyttämiäsi teknologioita.  

## Yhteistyö on sallittua

Harjoitustyön tekeminen yhteistyössä on sallittua.
Halutessanne voitte myös toteuttaa yhdessä esimerkiksi datan keräämiseen tai
jalostamiseen tarvittavia komponentteja.
Jokainen kuitenkin palauttaa omat kuvauksensa.
Käyttäkää komponenttien jakamiseen versionhallintajärjestelmää.
Harjoitustyöt eivät saa olla identtisiä.

## Loppuraportti

Harjoitustyön palautus tapahtuu lähettämällä oheisen mallin mukainen viesti
**perjantaihin 11. toukokuuta kello 17 mennessä**
osoitteeseen
[jukka.huhtamaki@tut.fi](mailto:jukka.huhtamaki@tut.fi).
Otsikoi viesti #JODATUT: työ valmis.

<blockquote>
  <p>
    Nimi: James Station<br />
    Opiskelijanumero: 213456<br />
    Sähköposti: <a href="mailto:jstat@trolleywatch.org">jstat@trolleywatch.org</a>
  </p>
  <p>Harjoitustyöni aihe: Julkisen liikenteen vaikutus Airbnb-asunnon hintaan</p>
  <p>Harjoitustyö löytyy kokonaisuudessaan oheisesta zip-paketista (jodatut2018-234567.zip).</p>

<p>Oppimispäiväkirjani löytyy osoitteesta:
<a href="http://blog.fi/jamesstation/jodatut2018">http://blog.fi/jamesstation/jodatut2018</a>.</p>

</blockquote>

Palautettavan zip-paketin (jodatut2018-opiskelijanumero.zip) tulee sisältää hakemisto nimeltä jodatut2018-234567 (korvaa lukusarja 234567 omalla opiskelijanumerollasi), jonka sisältä löytyvät työhösi liittyvät koodi- ja asetustiedostot.
Huomaa, että sovelluksen ei tarvitse toimia sellaisenaan. Riittää, että paketin sisältöön voi perehtyä suoraviivaisesti paketin purkamalla.

Merkitse lisäksi harjoitustyön eri ominaisuuksien raportoiduista toteutuksista ja vierailuluennoille osallistumisesta keräämäsi pisteet
[Google-laskentataulukkoon](https://docs.google.com/spreadsheets/d/1v2LnwnQHUKA5xA6CrkQ_JHCR-qUqedBwz68ryUIs-vo/edit?usp=sharing ) (ei edellytä sisäänkirjautumista).
**Merkitse pisteet ainoastaan siinä tapauksessa, että olet julkaissut kuvauksen määräaikaan mennessä.**
