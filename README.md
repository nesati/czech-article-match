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
Tento python program využívá morfologyckého taggeru [MorphoDiTa](http://ufal.mff.cuni.cz/morphodita) a knihovny [gensim](https://radimrehurek.com/gensim/index.html) k vyčíslení podobnosti mezi články načtenými přes RSS (seznam používaných kanálů lze upravit, načítá se ze souboru `zdroje.txt`). Je ale spíše ukázkou, že to vůbec jde, než použitelnou aplikací.
**I proto jsou v něm od základu portály sputniknews a aeronet, které rozhodně nejsou důvěryhodnými zdroji! Dobře ale slouží k demonstraci hledání souvislostí v textu.**

## Závislosti

### Nainstalovatelné přes PIP
Pomocí `pip -r requirements.txt` je lze nainstalovat automaticky. Druhou možností je to udělat ručně, jsou vypsané v `requirements.txt`.

### MorphoDiTa
První jsou potřeba spustitelné soubory. Z [GitHubu](https://github.com/ufal/morphodita/releases) si stáhněte nejnovější verzi (například `mordphodita-1.9.2-bin.zip`) a extrahujte ji. Ze složky `bin-[váš operační systém][vaše architektura]` zkopírujte do stejného adresáře, ve kterém se nachází zbytek programu, soubor `run_tagger`.  

Dále jsou potřeba české modely, jejich nejnovější verzi lze stáhnout [odsud](http://ufal.mff.cuni.cz/morphodita/users-manual#czech-morfflex-pdt_download). Archiv opět extrahujte a najděte v něm soubor `czech-morfflex-pdt-[verze modelů].tagger`. Ten zkopírujte do složky se zbytkem programu a přejmenujte ho na `czech-morfflex.tagger`

#### Poznámka
`preprocessor.py` využívá k práci s MorphoDiTa volání unixového příkazu. Ačkoliv MorphoDiTa sama o sobě má spustitelné soubory i pro Windows, tento příkaz v něm nebude fungovat a `czech-article-match` je tedy bez úpravy preprocessoru pod Windows nepoužitelný. 

## Použití
Po instalaci závislostí je program možné spustit zavoláním `main.py`, ten vypíše titulky a zdroje článků a k nim adresy těch souvisejících, pokud budou nějaké nalezeny.
