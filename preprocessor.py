import subprocess
import re

"""
 Přidané články na pole slov v základním tvaru
"""

__author__ = "kokolem"
__version__ = "0.1.0"
__license__ = "GPLv3"

# zajímají nás pouze česká písmena
regex = re.compile(r'[aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž]+')


class Preprocessor:
    def __init__(self):
        self.clanky = ""

    def add_article(self, article):
        if self.clanky == "":
            self.clanky = article
        else:
            self.clanky += " ‽ " + article  # ‽ slouží k oddělení článků, je to symbol, který se v nich (snad) neobjeví

    def preprocess(self):
        # uložení všech článků do souboru
        cache_clanku = open("clanky", "w")
        cache_clanku.write(self.clanky)

        # unix příkaz k použití taggeru na články v souboru
        command = "./run_tagger czech-morfflex.tagger clanky" \
                  " --output vertical --convert_tagset strip_lemma_id" \
                  " | awk '{print $2}'"

        # načtení článků
        clanky = subprocess.check_output(command, shell=True).decode("utf-8").split("‽")

        # rozdělení na tokeny a vyhození všeho, co nejsou slova
        tokeny = []
        for clanek in clanky:
            tokeny_clanku = list(filter(regex.search, clanek.split("\n")))  # \n odděluje tokeny
            tokeny.append(tokeny_clanku)

        return tokeny
