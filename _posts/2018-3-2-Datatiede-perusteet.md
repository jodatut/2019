---
layout: post
title: Johdanto datatieteeseen
---

# Teknologiademo 1 #

Ennen ensimmäistä teknologiademoa opiskelijalta odotetaan:
- Python-osaamista ja kehitysympäristö omalla koneella
- Ymmärrystä paketinhallintajärjestelmistä

Asennettuna tulisi olla:
- [Python](https://www.python.org/downloads/) (mieluiten v3.6.x)
- [Anaconda](https://www.anaconda.com/download/) (v5.1)
  - Anaconda ei ole pakollinen, mikäli esimerkiksi kovalevytilaa ei ole tarpeeksi, mutta erittäin hyödyllinen. Pycharm ajaa myös asiansa.

sekä seuraavat kirjastot:

- [Pandas](https://pandas.pydata.org/)
- [Numpy](http://www.numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Scikit-learn](http://scikit-learn.org/stable/)

Huom! Mikäli käytät Anacondaa, käytä myös Anacondan paketinhallintajärjestelmää eli _conda_:a esim. `conda install numpy`.

Lopuksi liittykää opintojakson Slack-kanavalle [täältä](https://join.slack.com/t/jodatut/shared_invite/enQtMzIyOTk4NjI5OTM2LTU2NDUwM2I0ZmRhZmI4Y2E5OWM1NGE1MTA5NDQ5NGRhMDI3NWI0MjUxZDA5MjIxMjhmNmFlYmI5YzRjZTdmOWU).

## Ensimmäinen esimerkki ##

Tehdään ohjelma, joka siivoaa likaista dataa käyttäen pandas-kirjastoa. Tutustutaan pandasin DataFrameihin ja siihen, miten niitä voidaan käsitellä. Jos aikaa riittää, tutustutaan myös matplotlib-kirjastoon ja kuvioiden piirtämiseen DataFrameista.

__Ensimmäisen demon lähdekoodi löytyy [tästä](./koodiesimerkit/data_cleaning3.py).__
