<h1 align="center">Spojování českých článků</h1>

<div align="center">
  
 My to zvládneme. Tak proč ne [newskit.](https://newskit.matsworld.io/)?
 
[![License](https://img.shields.io/github/license/nesati/czech-article-match)](https://github.com/nesati/czech-article-match/blob/master/LICENSE)
 ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/nesati/czech-article-match)
 [![GitHub last commit](https://img.shields.io/github/last-commit/nesati/czech-article-match)](https://github.com/nesati/czech-article-match/commits/master)
 [![GitHub forks](https://img.shields.io/github/forks/nesati/czech-article-match)](https://github.com/nesati/czech-article-match/network/members)
 [![GitHub stars](https://img.shields.io/github/stars/nesati/czech-article-match)](https://github.com/nesati/czech-article-match/stargazers)
 [![GitHub contributors](https://img.shields.io/github/contributors/nesati/czech-article-match)](https://github.com/nesati/czech-article-match/graphs/contributors)
 [![GitHub issues](https://img.shields.io/github/issues/nesati/czech-article-match)](https://github.com/nesati/czech-article-match/issues)
 ![Support <3](https://kokolem.github.io/LGBT-friendly-rainbow.svg)
 
</div>

## Jak to funguje?
Tento python program využívá morfologyckého analyzátoru [Majka](https://nlp.fi.muni.cz/czech-morphology-analyser/) a metody [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) k vyčíslení podobnosti mezi články načtenými přes RSS (seznam používaných kanálů lze upravit, načítá se ze souboru `zdroje.txt`). Je ale spíše ukázkou, že to vůbec jde, než použitelnou aplikací. **I proto jsou v něm od základu portály sputniknews a aeronet, rozhodně nejsou důvěryhodnými zdroji! Dobře ale slouží k demonstraci hledání souvislostí v textu.**

## Závislosti

### Nainstalovatelné přes PIP
Pomocí `pip -r requirements.txt` je lze nainstalovat automaticky. Druhou možností je to udělat ručně, jsou vypsané v `requirements.txt`.

### Majka
První je potřeba stáhnout si její spustitelný soubor. Tady [pro Linux](https://nlp.fi.muni.cz/czech-morphology-analyser/majka) (může být potřeba povolit spouštění souboru jako programu) nebo tady [pro Windows](https://nlp.fi.muni.cz/czech-morphology-analyser/majka.exe).

Dále je potřeba český slovník, ten lze stáhnout [odsud](https://nlp.fi.muni.cz/czech-morphology-analyser/majka.w-lt).

Oba soubory potom umístěte do stejného adresáře jako zbytek programu.

## Použití
Po instalaci závislostí je program možné spustit zavoláním `main.py`, ten vypíše titulky a zdroje článků a k nim adresy těch souvisejících, pokud budou nějaké nalezeny.
