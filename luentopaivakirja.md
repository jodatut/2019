---
layout: default
title: Luentopäiväkirja / JODA 2018
year: 2018
---

Tämä on Johdanto datatieteeseen -opintojakson kevään 2018 toteutuskerran luentopäiväkirja.
<!-- Vastaisen varalle:
Toteutus noudattelee [vuoden 2018 toteutuskertaa](https://jodatut.github.io/2018/luentopaivakirja).
Alan dynaamisuudesta johtuen sisältöjä ja toteutustapaa kuitenkin kehitetään jatkuvasti.
-->
Toteutuskerta etenee karkean
[luentosuunnitelman](https://docs.google.com/document/d/1drHb2HtmFy_Nu5iVuCtqZV6C9OjsoGMQqDrvDhV7fIc/edit?usp=sharing)
mukaisesti.

Totetutuskerran käytössä on
[Slack-kanava](https://join.slack.com/t/jodatut/shared_invite/enQtMzIyOTk4NjI5OTM2LTU2NDUwM2I0ZmRhZmI4Y2E5OWM1NGE1MTA5NDQ5NGRhMDI3NWI0MjUxZDA5MjIxMjhmNmFlYmI5YzRjZTdmOWU).
Osa luennoista tallennetaan [Echo360-järjestelmällä](https://echo360.org.uk/section/c9dd83a0-b703-47e7-82fe-545ff4644e75/public).

# Luentopäiväkirja

## Luentoviikko 4.4: Harjoitustyöhön tutustuminen

Lue ennen luentoa: [Predicting Airbnb Listing Prices with Scikit-Learn and Apache Spark](https://mapr.com/blog/predicting-airbnb-listing-prices-scikit-learn-and-apache-spark/)

Johdanto datatieteeseen -harjoitustyössä käydään läpi datatiedeprojektin keskeiset vaiheet.
Voit valita aiheen ja datalähteen vapaasti.
Saat pisteitä julkaisemalla Slackissa kuvauksen [harjoitustyön eri vaiheiden](https://jodatut.github.io/2018/harjoitustyo/) toteutuksesta.
Eräs vaihtoehto on Airbnb-aineiston analysointi.
Voit vaikkapa toteuttaa hintaennustimen [esimerkkianalyysiä](https://mapr.com/blog/predicting-airbnb-listing-prices-scikit-learn-and-apache-spark/) soveltamalla.

Koodiklinikalla [syvennytään lineaariregressioon](https://jodatut.github.io/2018/Kategoriset-muuttujat-ja-puuttuva-data).

## Luentoviikko 4.3: Koneoppimisen periaatteet

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

## Luentoviikko 4.2: Datan kerääminen ja jalostaminen

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

## Luentoviikko 4.1: Johdanto aihepiiriin ja suorittaminen

Avausluento maanantaina 5. maaliskuuta kello 14-16 Konetalon salissa K1320.
Suorittamisen käytännöt.
Mitä on datatiede
([CRISP-DM](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining),
[modern data scientist](https://www.schoolofdatascience.amsterdam/news/skills-need-become-modern-data-scientist/),
[datatieteen metrokartta](http://nirvacana.com/thoughts/2013/07/08/becoming-a-data-scientist/))?
Datatieteen työvälineet:
[Pandas](https://pandas.pydata.org/),
[scikit-learn](http://scikit-learn.org/),
[D3.js](https://d3js.org/),
[Jupyter](http://jupyter.org/).
Dataa koneeseen:
read_csv() & read_excel().

Ensimmäisellä Koodiklinikalla käydään läpi pandasin perusteita sekä eri kehitysympäristöjä. Teknologiademoon pääsee [tästä](https://jodatut.github.io/2018/Datatiede-perusteet/). Liittykää myös kurssin [Slack-kanavalle](https://join.slack.com/t/jodatut/shared_invite/enQtMzIyOTk4NjI5OTM2LTU2NDUwM2I0ZmRhZmI4Y2E5OWM1NGE1MTA5NDQ5NGRhMDI3NWI0MjUxZDA5MjIxMjhmNmFlYmI5YzRjZTdmOWU).
