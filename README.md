# Metacritic Crawler [![Python version](https://img.shields.io/badge/python-%E2%89%A53.6-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/) [![Travis (.com)](https://img.shields.io/travis/com/MarkelFe/metacritic-crawler/main.svg?logo=travis-ci&logoColor=white&style=flat-square)](https://travis-ci.com/MarkelFe/metacritic-crawler)
Tools for crawling data from metacritic.com (for educational purposes)

**IMPORTANT NOTE:**
1. Is under your responsibility that you respect the [Terms of Use of Metacritic](https://www.cbsinteractive.com/legal/cbsi/terms-of-use#Acceptable_Use), especially the point 11.13
2. This script uses some outdated packages (check #34).

## Description
These tools are designed for creating a SQLite file with [different kind of data](#example) that extracts from [Metacritic](https://www.metacritic.com). You won't find the result of the crawl, like a database, as this data is protected by copyright apart from that the content varies very frequently. For more information of how it works [check out this.](#method)

## Requisites
You can install all this packages with ```pip install -r requirements.txt``` or you can manually install them.
**[Python ≥3.6](https://www.python.org/downloads/)** (preferably ≥3.7)  
**[Scrapy 1.8.0](https://scrapy.org/)** ```pip install Scrapy==1.8.0```  
**[Tqdm ≥4.31.1](https://github.com/tqdm/tqdm)** ```pip install tqdm```

## Usage
Scrapy has his own command line tool, you **shouldn't** use the default Python Shell.
0. Be sure that you have Python 3 installed.
1. [Download the repository](https://github.com/MarkelFe/metacritic-crawler/releases) and travel to the repository folder through your OS Command Line Tool
2. Install all the requirements with ```pip install -r requirements.txt```
3. Run the following command ```scrapy runspider games.py -o gm.jl``` which will create a file called gm.jl. This file will include the links to all the Metacritic games, the process of completing this file will take around 40-80 minutes. You can [modify some parameters inline](#modifiers)
4. Run the command ```scrapy runspider analyze.py``` which will create the database games.db. To complete this process, it will take around 2 hours.
5. Done! The file ```games.db```  includes all the information. Use your preferred SQLite reader.

## Modifiers
These modifiers are for [`games.py`](https://github.com/MarkelFe/metacritic-crawler/blob/main/games.py) and should be placed after the command `scrapy runspider games.py -o gm.jl`. 

|          Options         | Values |        Description             | Default value |
|:-------------------------:|:------:|:---------------------------------------------------------:|:-------------:|
|       -a start_page=      | 0-161* | Page number to begin scrape |       0       |
|         -a delay=         |   0-∞  |            Delay between page scrapes            |       3       |
|     -a items_per_page=    |  1-100 |     Number of games to scrape per page    |      100      |
| -s CLOSESPIDER_PAGECOUNT= | 1-161* |              Number of pages to scrape              |      161*     |

*Represents the last game page. Verify the latest page number [here](https://www.metacritic.com/browse/games/score/metascore/all/all/filtered).

## Method
The process consists of 2 files, the first, ```games.py```, runs through [this page](https://www.metacritic.com/browse/games/score/metascore/all/all/filtered) and collects all the data on a file called games.jl. After, ```analyze.py``` uses this list of games and goes to every single page and gets the details of all the games. These details are converted to a SQLite database, this process occurs while new pages are being scraped, so do not hesitate about stopping the script (note: for how scrapy works it may take a while to stop, as it waits until the loaded pages are scrapped).

## Example
This is an example of the result of running these scripts. The first line is the variable names of [analyze.py](https://github.com/MarkelFe/metacritic-crawler/blob/main/analyze.py). The second line includes the information from the game [Tetris DS](https://www.metacritic.com/game/ds/tetris-ds).

|   title   | platform |  company |    release   |          description          | metascore |         critics_desc        | critics_count | user_score |          user_desc          | user_count |  players  | rating |
|:---------:|:--------:|:--------:|:------------:|:-----------------------------:|:---------:|:---------------------------:|:-------------:|:----------:|:---------------------------:|:----------:|:---------:|:------:|
|     t     |     p    |     c    |       r      |               d               |     cs    |              cd             |       cn      |     us     |              ud             |     un     |     pl    |   rt   |
| Tetris DS |    DS    | Nintendo | Mar 20, 2006 | 10 DS players can battle(...) |     84    | Generally favorable reviews |       56      |     8.0    | Generally favorable reviews | 54 Ratings | 4  Online |    E   |

## Meta
Markel F. – [@Markel_f](https://twitter.com/Markel_f)
Distributed under the BSD license. See ``LICENSE`` for more information.  
[https://github.com/MarkelFe](https://github.com/MarkelFe)  
