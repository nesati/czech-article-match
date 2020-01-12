#!/usr/bin/env python3
from getarticles import getarticles
from preprocessor import Preprocessor
from gensim import corpora, models, similarities

"""
Vrací boolean podle toho, jestli dva články pojednávají o tom samém
"""

__author__ = "kokolem"
__version__ = "0.1.0"
__license__ = "GPLv3"


class Predictor:
    def __init__(self):
        self.clanky = getarticles()  # načtení článků z RSS

        # předpříprava (tokenizace, otagování a normalizace) textů
        preprocessor = Preprocessor()
        for clanek in self.clanky:
            preprocessor.add_article(clanek['text'])
        korpus = preprocessor.preprocess()

        if len(korpus) != len(self.clanky):
            print("Chyba! Jeden nebo více článků obsahuje znak ‽, který je vnitřně používaný k jejich oddělení.")
            exit(1)

        # zpětné přiřazení tokenů k jejich článkům
        cislo_clanku = 0
        for clanek in self.clanky:
            clanek['tokeny'] = korpus[cislo_clanku]
            cislo_clanku += 1

        self.slovnik = corpora.Dictionary(korpus)
        bow_korpus = [self.slovnik.doc2bow(zpracovany_clanek) for zpracovany_clanek in korpus]
        self.tfidf = models.TfidfModel(bow_korpus, smartirs="nfu")
        self.index = similarities.SparseMatrixSimilarity(self.tfidf[bow_korpus], num_features=len(self.slovnik))

    def predict(self, url1, url2, threshold=0.3):
        clanek1 = {}
        for clanek in self.clanky:
            if clanek['url'] == url1:
                clanek1 = clanek

        for podobnost in list(enumerate(self.index[self.slovnik.doc2bow(clanek1['tokeny'])])):
            if self.clanky[podobnost[0]]['url'] == url2:
                return podobnost[1] > threshold


if __name__ == "__main__":
    predictor = Predictor()
    print(predictor.predict(
        "https://zpravy.aktualne.cz/domaci/zeman-si-vazi-rozhodnuti-valkove-nekandidovat-ombudsmankou-b/r~7f7c4448352411ea84260cc47ab5f122/?utm_source=mediafed&utm_medium=rss&utm_campaign=mediafed",
        "https://www.idnes.cz/zpravy/domaci/milos-zeman-helena-valkova-s-prezidentem-v-lanech.A200112_103851_domaci_knn#utm_source=rss&utm_medium=feed&utm_campaign=zpravodaj&utm_content=main"
    ))
