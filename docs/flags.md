# Modifiers

This modifiers are for the file [`games.py`](https://github.com/MarkelFe/metacritic-crawler/blob/master/games.py) and must be introduced after the command `scrapy runspider games.py -o gm.jl`. 

|          Modifier         | Values |                     Determines the...                     | Default value |
|:-------------------------:|:------:|:---------------------------------------------------------:|:-------------:|
|       -a start_page=      | 0-161* | Page number in which the scrapers starts to get the games |       0       |
|         -a delay=         |   0-∞  |            Delay between the scraping of pages            |       3       |
|     -a items_per_page=    |  1-100 |     The number of games that will be scrapped per page    |      100      |
| -s CLOSESPIDER_PAGECOUNT= | 1-161* |              How many pages will be scrapped              |      161*     |

*Represents the last the page number - 1. You can check this number [here](https://www.metacritic.com/browse/games/score/metascore/all/all/filtered)
