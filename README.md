# Metacritic Crawler
Tools for crawling data from metacritic.com (for educational purposes)

**IMPORTANT NOTE:**
As defined in the [Terms of Use](https://www.cbsinteractive.com/legal/cbsi/terms-of-use#Acceptable_Use) in point 11.13 is forbidden to *Engage in unauthorized spidering, “scraping,” data mining or harvesting of Content, or use any other unauthorized automated means to gather data from or about the Services*. So this repository is completely educational for people learn how to use Scrapy and by any means you have permission to use this repository for scraping metacritic or using as a reference or any kind of assist. You agree not to use this repository for any purpose that would violate [CBS Interactive's Terms of Use](https://www.cbsinteractive.com/legal/cbsi/terms-of-use). Please [contact with Metacritic](https://www.metacritic.com/contact-us) if you want to request permission for crawling their website. You bear all responsibility about the use of this program. Remember again that this program is designed for educational purposes (that the reason of so many commentaries).
PD.: If CBS Interactive contacts with me to retire this crawler I will definitely retire the repository.

## Description
These tools are designed for creating a SQLite file with different kind of data that you can extract from [Metacritic](https://www.metacritic.com). You won't find the result of the crawl, like a databse, as this data is protected by copyright apart from that we don't have the permission from CBS to crawl their website.

## Requisites
**[Python 3.X](https://www.python.org/downloads/)** (preferably +3.7)  
**[Scrapy:](https://scrapy.org/)**
```$ pip install scrapy```  
**Win32api:**
```$ pip install pypiwin32```

## Usage
[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)  
**This is a alpha release so expect having to do some manual job for getting result (apart from several bugs).**
Scrapy has his own command line tool, you **shouldn't** use the default Python Shell.
1. Download the repository and travel to the repository folder throught your OS Command Line Tool
2. Run the following command ```scrapy runspider games.py -o gm.jl``` which will create a file called gm.jl. This file will include the links to all the Metacritic games, the process of completing this file will take between 40 and 80 minutes.
3. You must replace all the ```{"f": "``` for ```https://www.metacritic.com``` and also you must remove all the ```"}``` (The final file should have an standard URL per line). We recommend using a text editor tool that would allow to do all these changes at the say time.
4. Run the command ```scrapy runspider analyze.py``` which will create the database games.db. To complete this process is calculated that it will take around 2 hours.

## Meta
Markel F- – [@Markel_f](https://twitter.com/Markel_f) – markelf@protonmail.com (Please include ```Github - Metacritic Crawler``` on the subject of the email)  
Distributed under the BSD license. See ``LICENSE`` for more information.  
[https://github.com/MarkelFe](https://github.com/MarkelFe)  
