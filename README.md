# Metacritic Crawler
Tools for crawling data from metacritic.com (for educational purposes)

**IMPORTANT NOTE:**
As defined in the [Terms of Use](https://www.cbsinteractive.com/legal/cbsi/terms-of-use#Acceptable_Use) in point 11.13 is forbidden to *Engage in unauthorized spidering, “scraping,” data mining or harvesting of Content, or use any other unauthorized automated means to gather data from or about the Services*. So this repository is completely educational for people learn how to use Scrapy and by any means you have permission to use this repository for scraping metacritic or using as a reference or any kind of assist. You agree not to use this repository for any purpose that would violate [CBS Interactive's Terms of Use](https://www.cbsinteractive.com/legal/cbsi/terms-of-use). Please [contact with Metacritic](https://www.metacritic.com/contact-us) if you want to request permission for crawling their website. You bear all responsibility about the use of this program. Remember again that this program is designed for educational purposes (that the reason of so many commentaries).
PD.: If CBS Interactive contacts with me to retire this crawler I will definitely retire the repository.

## Description
These tools are designed for creating a SQLite file with [different kind of data](https://github.com/MarkelFe/metacritic-crawler/blob/master/README.md#example) that extracts from [Metacritic](https://www.metacritic.com). You won't find the result of the crawl, like a database, as this data is protected by copyright apart from that the content varies very frequently. For more information of how it works [check out this.](https://github.com/MarkelFe/metacritic-crawler/blob/master/README.md#method)

## Requisites
You can install all this packages with ```pip install -r requirements.txt``` or you can manually install them.
**[Python >=3.6](https://www.python.org/downloads/)** (preferably +3.7)  
**[Scrapy >=1.6.0](https://scrapy.org/)** ```pip install scrapy```  
**[Tqdm >= 4.31.1](https://github.com/tqdm/tqdm)** ```pip install tqdm```

## Usage
Scrapy has his own command line tool, you **shouldn't** use the default Python Shell.
0. Be sure that you have Python 3 installed.
1. [Download the repository](https://github.com/MarkelFe/metacritic-crawler/releases) and travel to the repository folder throught your OS Command Line Tool
2. Install all the requirements with ```pip install -r requirements.txt```
3. Run the following command ```scrapy runspider games.py -o gm.jl``` which will create a file called gm.jl. This file will include the links to all the Metacritic games, the process of completing this file will take around 40-80 minutes. You can [modify some parameters inline](https://github.com/MarkelFe/metacritic-crawler/blob/master/docs/flags.md)
4. Run the command ```scrapy runspider analyze.py``` which will create the database games.db. To complete this process, it will take around 2 hours.
5. Done! The file ```games.db```  includes all the information. Use your prefered SQLite reader.

## Method
The process consists on 2 files, the first, ```games.py```, runs through [this page](https://www.metacritic.com/browse/games/score/metascore/all/all/filtered) and collects all the data on a file called games.jl. After, ```analyze.py``` uses this list of games and goes to every single page and gets the details of all the games. These details are converted to a SQLite database, this process occurs while new pages are being scraped, so do not hesitate about stopping the script (note: for how scrapy works it may take a while to stop, as it waits until the loaded pages are scrapped).

## Example
This is an example of the result of running these scripts. The first line is the variable names of [analyze.py](https://github.com/MarkelFe/metacritic-crawler/blob/master/analyze.py). The second line includes the information from the game [Tetris DS](https://www.metacritic.com/game/ds/tetris-ds).

|   title   | platform |  company |    release   |          description          | metascore |         critics_desc        | critics_count | user_score |          user_desc          | user_count |  players  | rating |
|:---------:|:--------:|:--------:|:------------:|:-----------------------------:|:---------:|:---------------------------:|:-------------:|:----------:|:---------------------------:|:----------:|:---------:|:------:|
|     t     |     p    |     c    |       r      |               d               |     cs    |              cd             |       cn      |     us     |              ud             |     un     |     pl    |   rt   |
| Tetris DS |    DS    | Nintendo | Mar 20, 2006 | 10 DS players can battle(...) |     84    | Generally favorable reviews |       56      |     8.0    | Generally favorable reviews | 54 Ratings | 4  Online |    E   |

## Meta
Markel F. – [@Markel_f](https://twitter.com/Markel_f)
Distributed under the BSD license. See ``LICENSE`` for more information.  
[https://github.com/MarkelFe](https://github.com/MarkelFe)  
