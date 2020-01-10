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
    print(zdroje)


if __name__ == "__main__":
    main()
