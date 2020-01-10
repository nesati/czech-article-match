import subprocess
import re

# allowed characters - czech
regex = "[aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzž \n]+"


def tokenize(text, majkaPath="./majka", dictionaryPath="./majka.w-lt"):
    tokens = "".join(re.findall(regex, text.lower())).split()
    batcmd = "echo '" + "\n".join(tokens) + "' | " + majkaPath + " -p -f " + dictionaryPath
    results = subprocess.check_output(batcmd, shell=True).decode("utf-8").split("\n")[:-1]
    lemmas = []

    for line in results:
        output = line.split(":")
        lemmas.append(output[0] if len(output) == 1 else output[1])
    return lemmas
