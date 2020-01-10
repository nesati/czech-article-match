#!/usr/bin/env python3

import feedparser

"""
Získá články z RSS zdrojů ve zdroje.txt
"""

__author__ = "kokolem"
__version__ = "0.1.1"
__license__ = "GPLv3"


def main():
    zdroje = [line.rstrip('\n') for line in open("zdroje.txt")]
    rss_feedy = [feedparser.parse(zdroj) for zdroj in zdroje]

    clanky = []
    for feed in rss_feedy:
        clanky.append([clanek['title'] + " " + clanek['summary'] for clanek in feed['items']])
    clanky = [item for sublist in clanky for item in sublist]
    for clanek in clanky:
        print(clanek)
        print("--------------------------------------")


if __name__ == "__main__":
    main()
