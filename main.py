#!/usr/bin/env python3
from getarticles import getarticles
from preprocessor import Preprocessor
from gensim import corpora, models, similarities

"""
Hlavní část programu, vypíše titulky, zdroje a související články
"""

__author__ = "kokolem"
__version__ = "0.1.0"
__license__ = "GPLv3"

THRESHOLD = 0.35  # jak moc nepodobné články se budou řadit k sobě


def main():
    clanky = getarticles()  # načtení článků z RSS

    # předpříprava (tokenizace, otagování a normalizace) textů
    preprocessor = Preprocessor()
    for clanek in clanky:
        preprocessor.add_article(clanek['text'])
    korpus = preprocessor.preprocess()

    if len(korpus) != len(clanky):
        print("Chyba! Jeden nebo více článků obsahuje znak ‽, který je vnitřně používaný k jejich oddělení.")
        exit(1)

    # zpětné přiřazení tokenů k jejich článkům
    cislo_clanku = 0
    for clanek in clanky:
        clanek['tokeny'] = korpus[cislo_clanku]
        cislo_clanku += 1

    slovnik = corpora.Dictionary(korpus)
    bow_korpus = [slovnik.doc2bow(zpracovany_clanek) for zpracovany_clanek in korpus]
    tfidf = models.TfidfModel(bow_korpus, smartirs="nfu")
    index = similarities.SparseMatrixSimilarity(tfidf[bow_korpus], num_features=len(slovnik))

    celkem_souvislosti = 0

    for clanek in clanky:
        print("---------------")
        print(clanek['nadpis'])
        print("zdroj: ", clanek['url'])
        for podobnost in list(enumerate(index[slovnik.doc2bow(clanek['tokeny'])])):
            if podobnost[1] > THRESHOLD and clanky[podobnost[0]]['url'] != clanek['url']:
                print("souvisí: ", clanky[podobnost[0]]['url'])
                celkem_souvislosti += 1

    print("---------------")
    print("celkem souvislostí: ", celkem_souvislosti)


if __name__ == "__main__":
    main()
