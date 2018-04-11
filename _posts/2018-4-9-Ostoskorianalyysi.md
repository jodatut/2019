---
layout: post
title: Ryvästäminen ja ostoskorianalyysi
---

# Teknologiademo 5 #

Motivaationa [uutisartikkeli](https://www.nytimes.com/2004/11/14/business/yourmoney/what-walmart-knows-about-customers-habits.html) jo vuodelta 2004, jossa Wal-Mart ennusti ostokäyttäytymistä hurrikaanien varalle.

Teknologiademossa tutustutaan ryvästämiseen (clustering) ostoskorianalyysin keinoin. Ostoskorianalyysistä kertoo [johdantoartikkeli](https://towardsdatascience.com/a-gentle-introduction-on-market-basket-analysis-association-rules-fa4b986a40ce), jossa puhutaan mm. support- ja confidence-arvoista. Lukekaa myös artikkelit [assosiaatiosäännöistä](https://www.kaggle.com/datatheque/association-rules-mining-market-basket-analysis) sekä [Apriori-algoritmista](https://www3.cs.stonybrook.edu/~cse634/lecture_notes/07apriori.pdf) (suomeksi Apriori-algoritmista [täällä](https://www.cs.helsinki.fi/u/htoivone/teaching/seminaariK08/tuomas.pdf)), joka on hyvin käytetty algoritmi ostoskorianalyysissa.

## Esimerkki 1 ##

Ostoskorianalyyissä käytetään Apriori-algoritmiin [mlxtend-kirjastoa](http://rasbt.github.io/mlxtend/). Kirjaston voi ladata Anaconda Promptissa komennolla

     conda install -c conda-forge mlxtend

Esimerkissä käytetyn datan voi ladata [täältä](https://drive.google.com/file/d/0BzygIwXb3aZJZ1c0Ri1hZ0VOWkk/view).

Koodi löytyy [täältä](https://github.com/jodatut/2018/blob/master/koodiesimerkit/apriori_notebook.py).

## Esimerkki 2 ##

Toisessa esimerkissä käytetyn datan voi ladata [täältä](https://www.datascience.com/blog/k-means-clustering).

Koodi löytyy [täältä](https://github.com/jodatut/2018/blob/master/koodiesimerkit/clustering_notebook.py).
