#!/usr/bin/env python3
import getarticles
import tfidf
import tokenize

"""
Hlavní část programu, vypíše titulky, zdroje a související články
"""

__author__ = "kokolem"
__version__ = "0.1.0"
__license__ = "GPLv3"

THRASH_HOLD = 0.11  # jak moc nepodobné články se budou řadit k sobě


def main():
    clanky = getarticles.getarticles()  # načtení článků z RSS
    table = tfidf.TfIdf()  # inicializace TfIdf
    for clanek in clanky:
        tokeny = tokenize.tokenize(clanek['text'])  # tokeny jsou základní tvary slov
        clanek['tokeny'] = tokeny
        table.add_document(clanek['url'], tokeny)  # přidání článku do tfidf ke zpracování

    pocet_souvislosti = 0  # celkový počet nalezených souvislostí, hodí se k hraní si s trash holdem

    for clanek in clanky:
        print("------------------")
        print(clanek['nadpis'])
        print("zdroj: " + clanek['url'])
        for podobnost in table.similarities(clanek['tokeny']):  # podobnost[0] je url článku, podobnost[1] samotné číslo
            if podobnost[1] > THRASH_HOLD and podobnost[0] != clanek['url']:  # nejpodobnější je článek sám sobě
                print("souvisí: " + podobnost[0])
                pocet_souvislosti += 1
    print("------------------")
    print("nalezeno souvislostí: ", pocet_souvislosti)


if __name__ == "__main__":
    main()
