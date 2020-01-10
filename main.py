#!/usr/bin/env python3
import getarticles
import tfidf
import tokenize

"""
Hlavní část programu, vypíše odkazy na články seskupené podle témat
"""

__author__ = "kokolem"
__version__ = "0.1.0"
__license__ = "GPLv3"

THRASH_HOLD = 0.09


def main():
    clanky = getarticles.get()
    table = tfidf.TfIdf()
    for clanek in clanky:
        tokeny = tokenize.tokenize(clanek['text'])
        clanek['tokeny'] = tokeny
        table.add_document(clanek['url'], tokeny)

    pocet_souvislosti = 0

    for clanek in clanky:
        print("------------------")
        print(clanek['nadpis'])
        print("zdroj: " + clanek['url'])
        for podobnost in table.similarities(clanek['tokeny']):
            if podobnost[1] > THRASH_HOLD and podobnost[0] != clanek['url']:
                print("Souvisí: " + podobnost[0])
                pocet_souvislosti += 1
    print("------------------")
    print("nalezeno souvislostí: ", pocet_souvislosti)


if __name__ == "__main__":
    main()
