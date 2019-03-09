---
layout: default
title: Luentopäiväkirja / JODA 2019
year: 2019
---

Tämä on Johdanto datatieteeseen -opintojakson kevään 2019 toteutuskerran luentopäiväkirja.
<!-- Vastaisen varalle:
Toteutus noudattelee [vuoden 2018 toteutuskertaa](https://jodatut.github.io/2018/luentopaivakirja).
Alan dynaamisuudesta johtuen sisältöjä ja toteutustapaa kuitenkin kehitetään jatkuvasti.
-->
Toteutuskerta etenee alla olevan luentorungon mukaisesti, vuoden 2018 luentosarjaa iteratiivisesti kehittäen. Alla näkyvät aiheet ovat viime vuoden toteutuksen mukaisia ja päivittyvät luentosarjan edetessä

Totetutuskerran käytössä on
[Slack-kanava](https://join.slack.com/t/tampere-university/shared_invite/enQtNTYxNjY2OTkwOTYyLWQ2M2EyODJkYWU5OWEwOGQzM2I5NDAwZDVhNWVhNzNlMjI5ZDgzNmQ4MTEyOWRlNTkzMWU2OTBkNWU4Y2UxMmU).

Toteutuskerran aikana pyritään myös aktiivisesti Twiittaan hashtag:llä #jodatuni

# Luentopäiväkirja

## Luento 23.4: Kertaus
Kerrataan luentojen ja harjoitusten keskeiset osat ja verrataan opittua oppimistavoitteisiin. Esitetään hyviä kysymyksiä ja katsotaan mihin tästä voi jatkaa. 

## Luento 16.4: Datan visualisointi

Viimeisellä varsinaisella luentokerralla käydään läpi datan vuorovaikutteista eksploratiivista analytiikka ja luodaan tiekarttaa kohti datatuotteiden kehittämistä. Lue artikkeli [Designing and Developing Analytics-Based Data Products](https://sloanreview.mit.edu/article/designing-and-developing-analytics-based-data-products/) ja katso Jeffrey Heerin [keynote-esitys visuaalisesta analytiikasta](https://www.youtube.com/watch?v=hsfWtPH2kDg).

[Koodiklinikalla](https://jodatut.github.io/2018/Datan-visualisointi) päästään tekemään visualisointeja siihen tarkoitettujen kirjastojen avulla sekä luomaan yksinkertainen web-sovellus datan ympärille.

## Luento 9.4: Ohjaamaton koneoppiminen

Miten ohjattu ja ohjaamaton oppiminen eroavat toisistaan?
Ohjaamaton oppiminen (ks. [Unsupervised learning workflow](https://goo.gl/images/dCm55z)),
[ostoskorianalyysi](http://pbpython.com/market-basket-analysis.html),
[verkostoanalyysi](https://github.com/jukkahuhtamaki/demo-twitter-collector/blob/master/README.md) (ks. [Marvel social graph](https://blog.dataiku.com/2015/05/19/marvel-social-graph-analysis)),
ryvästäminen (ks. [k-means-clustering](https://www.datascience.com/blog/k-means-clustering)),
aihemallinnus eli [topic modeling](https://medium.com/mlreview/topic-modeling-with-scikit-learn-e80d33668730) ja sen [riskit](https://rajapinta.co/2017/07/08/varovaisuutta-aihemallinnuksen-kanssa/).

Koodiklinikalla tutustutaan [ryvästämiseen ostoskorianalyysin kautta](https://jodatut.github.io/2018/Ostoskorianalyysi).

## Luento 26.3: Harjoitustyöhön tutustuminen

Lue ennen luentoa: [Predicting Airbnb Listing Prices with Scikit-Learn and Apache Spark](https://mapr.com/blog/predicting-airbnb-listing-prices-scikit-learn-and-apache-spark/)

Johdanto datatieteeseen -harjoitustyössä käydään läpi datatiedeprojektin keskeiset vaiheet.
Voit valita aiheen ja datalähteen vapaasti.
Saat pisteitä julkaisemalla Slackissa kuvauksen [harjoitustyön eri vaiheiden](https://jodatut.github.io/2018/harjoitustyo/) toteutuksesta.
Eräs vaihtoehto on Airbnb-aineiston analysointi.
Voit vaikkapa toteuttaa hintaennustimen [esimerkkianalyysiä](https://mapr.com/blog/predicting-airbnb-listing-prices-scikit-learn-and-apache-spark/) soveltamalla.

Koodiklinikalla [syvennytään lineaariregressioon](https://jodatut.github.io/2018/Kategoriset-muuttujat-ja-puuttuva-data).

## Luento 19.3: Koneoppimisen periaatteet

Lue ennen luentoa: [Näin laadullinen tieto jalostuu laskennalliseksi: piirteet sosiaalisen median analytiikassa](https://rajapinta.co/2017/10/16/nain-laadullinen-tieto-jalostuu-laskennalliseksi-piirteet-sosiaalisen-median-analytiikassa/)

Koneoppimisen työnkulku (ks. [Supervised learning workflow](https://twitter.com/jnkka/status/973566383899455488)),
sovellusesimerkki: [asiakaspoistuma-analyysi](http://www.louhia.fi/2014/08/27/asiakaspoistuma-analyysi-ja-miljoona-lisamyyntia/),
piirteiden erottaminen (ks. [esilukemisto]((https://rajapinta.co/2017/10/16/nain-laadullinen-tieto-jalostuu-laskennalliseksi-piirteet-sosiaalisen-median-analytiikassa/))),
piirteiden jalostaminen (ks.
[feature engineering](https://medium.com/mindorks/what-is-feature-engineering-for-machine-learning-d8ba3158d97a)),
luokittelu Pythonilla ([step-by-step tutorial](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)), dataesimerkkejä (ks. [IBM Watson datasets](https://www.ibm.com/communities/analytics/watson-analytics-blog/guide-to-sample-datasets/)),
dataan tutustuminen käyntiin (ks.
[explore](https://github.com/jodatut/2018/tree/master/koodiesimerkit/explore)).

Koodiklinikalla [esimerkkejä lineaariregressiosta](https://jodatut.github.io/2018/Lineaariregressio).

## Luento 12.3: Datan kerääminen ja jalostaminen

Datatiedeprosessin vaiheet ([Data Science Workflow](https://cacm.acm.org/blogs/blog-cacm/169199-data-science-workflow-overview-and-challenges/fulltext)),
kerääminen ja jalostaminen [datatieteen metrokartassa](http://nirvacana.com/thoughts/2013/07/08/becoming-a-data-scientist/),
[ETL vs. DAD](https://www.datasciencecentral.com/profiles/blogs/data-scientist-versus-data-engineer),
ryömijät ja raapijat
([Web crawler](https://en.wikipedia.org/wiki/Web_crawler),
[Web scraping](https://en.wikipedia.org/wiki/Web_scraping),
[Web Scraping in Python](https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/),
[Scrapy](https://scrapy.org/)),
[Scraping for journalists](https://leanpub.com/scrapingforjournalists))
dataformaatit ja niiden ohjelmallinen käsittely,
data wrangling (ks. [DataWrangler](http://vis.stanford.edu/wrangler/)),
datan jalostaminen Pythonilla
(ks. [Pandas-toimintokooste](https://www.datacamp.com/community/blog/pandas-cheat-sheet-python),
vrt. OpenRefine.

Koodiklinikalla käsittelyssä [raapijat ja ryömijät](https://jodatut.github.io/2018/Raapijat-ja-ry%C3%B6mij%C3%A4t/).

<!-- eräs raapija ja ryömijä (ks. [esimerkki](https://github.com/jukkahuhtamaki/pcm-demo/blob/master/crawl-study-guide/crawl_courses.py), -->

<!-- Toiseen teknologiademoon pääsee [tästä]. -->

## Luento 5.3: Johdanto aihepiiriin ja suorittaminen

Avausluento tiistaina 5. maaliskuuta kello 10-12 SJ204.
Suorittamisen käytännöt.
Mitä on datatiede
([CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining),
[modern data scientist](https://www.schoolofdatascience.amsterdam/news/skills-need-become-modern-data-scientist/),
[datatieteen metrokartta](http://nirvacana.com/thoughts/2013/07/08/becoming-a-data-scientist/))?
[Up and runnign with Python](http://blog.kaggle.com/2012/07/02/up-and-running-with-python-my-first-kaggle-entry/)
Datatieteen työvälineet:
[Pandas](https://pandas.pydata.org/),
[scikit-learn](http://scikit-learn.org/),
[D3.js](https://d3js.org/),
[Jupyter](http://jupyter.org/).
Dataa koneeseen:
read_csv() & read_excel().

Ensimmäisen luennon esitysmateriaali [Jupyter-työkirjana](https://github.com/jodatut/2019/blob/master/luentokirjat/Lecture%201.ipynb)

Ensimmäisellä Koodiklinikalla käydään läpi pandasin perusteita sekä eri kehitysympäristöjä. Teknologiademoon pääsee [tästä](https://jodatut.github.io/2019/Datatiede-perusteet/). Echo360 - Exercise Session Video Recording: https://echo360.org.uk/section/6c32e7c7-bf87-4001-a2b2-0edee0232b0b/public
Liittykää myös kurssin [Slack-kanavalle](https://join.slack.com/t/tampere-university/shared_invite/enQtNTYxNjY2OTkwOTYyLWQ2M2EyODJkYWU5OWEwOGQzM2I5NDAwZDVhNWVhNzNlMjI5ZDgzNmQ4MTEyOWRlNTkzMWU2OTBkNWU4Y2UxMmU).
