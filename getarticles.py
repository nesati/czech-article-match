import re
import feedparser

"""
Získá články z RSS zdrojů ve zdroje.txt
"""

__author__ = "kokolem"
__version__ = "0.1.2"
__license__ = "GPLv3"


def getarticles():
    zdroje = [line.rstrip('\n') for line in open("zdroje.txt")]  # načtení zdrojů ze zdroje.txt
    rss_feedy = [feedparser.parse(zdroj) for zdroj in zdroje]  # stažení rss ze zdrojů

    clanky = []

    for feed in rss_feedy:
        for clanek in feed['items']:
            nadpis = clanek['title']
            text = re.sub(r'[<][^>]*[>]', '', clanek['title'] + " " + clanek['summary'])  # nadpis a tělo článku bez xml
            url = clanek['link']
            clanky.append({'nadpis': nadpis, 'text': text, 'url': url})

    return clanky


if __name__ == "__main__":
    getarticles()
