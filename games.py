## This file creates an spider that gets the links of all the games
## For that it uses the best games page of Metacritic which has all the games (around 15K on December 2018)
## It usually takes between 40 and 80 minutes to make a complete run
## To run it use the command 'scrapy runspider games.py -o gm.jl'
## Remember that you MUST comply with the point 11.13 of the terms of use in Metacritic (https://www.cbsinteractive.com/legal/cbsi/terms-of-use), you need the permission of Cbs Interactive to run any kind of scraping (this is a scraping tool if you didn't know it btw)
## You bear all responsibility about the use of this program 

import scrapy
import win32api
from time import sleep

## ----------------------------CREATING THE SPIDER------------------------------

class ListSpider(scrapy.Spider):
    name = "list"
    start_urls = ['https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?page=0']

## ----------------------------GETTING GAMES URLs-------------------------------

    def parse(self, response):
        #Limit the range because it helps (be sure)
        x = 0
        for x in range(0, 100):
           yield {
             #Extracts the link of the game
             'f': response.css('.product_title a::attr(href)')[x].extract()
            }
           x = x + 1
#          print('Game number:', x) #Debug option

## ---------------------------FOLLOW TO THE NEXT PAGE-------------------------

        ## TIP: You can define the selector in a variable and later use it instead of the inline code, although it's not necessary
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        
        # Reducing the load in the Metacritic's servers (do you have permission to crawl?)
        print('Continuing to in 10 seconds:', next_page)
        sleep(10)

        # Travelling to the next page :D
        # Side note: When you reach the last page some bugs occur... 
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

# This message is for user that try to use the default Python Shell
print('Hey, are you using the correct tool? Spoiler: read README.md')
