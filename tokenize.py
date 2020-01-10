import subprocess
import re

"""
Vstupní text převede na pole slov v základním tvaru
"""

__author__ = "nesati"
__version__ = "0.1.0"
__license__ = "GPLv3"

# zajímají nás pouze česká písmena
regex = "[aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzž \n]+"


def tokenize(text, majkaPath="./majka", dictionaryPath="./majka.w-lt"):
    tokens = "".join(re.findall(regex, text.lower())).split()  # regex a malá písmena
    majka_command = "echo '" + "\n".join(tokens) + "' | " + majkaPath + " -p -f " + dictionaryPath  # příkaz pro Majku
    results = subprocess.check_output(majka_command, shell=True).decode("utf-8").split("\n")[:-1]  # výsledek z Majky
    lemmas = []  # tokeny - základní tvary slov

    for line in results:
        output = line.split(":")
        lemmas.append(output[0] if len(output) == 1 else output[1])  # někdy Majka vrátí slovo tak, jak ho dostala
    return lemmas
