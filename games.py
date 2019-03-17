## This file creates an spider that gets the links of all the games
## For that it uses the best games page of Metacritic which has all the games (around 16K on March 2019)
## It usually takes between 40 and 80 minutes to make a complete run
## To run it use the command 'scrapy runspider games.py -o gm.jl'
## You bear all responsibility about the use of this program 

import scrapy
from time import sleep
from tqdm import tqdm

## ----------------------------CREATING THE SPIDER------------------------------

class ListSpider(scrapy.Spider):
    name = "list"
    custom_settings = {
        'LOG_LEVEL': 'ERROR',
    }

## ----------------------------DEFINING THE SPIDER------------------------------ 

    # We define the arguments, more information in PR #16
    def __init__(self, start_page=0, delay=3, items_per_page=100, **kwargs):
        self.start_urls = [f'https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?page={start_page}']
        # We declare delay and "i_p_p" generally outside the variable as we will need it later
        self.delay = int(delay)
        self.items_per_page = int(items_per_page)
        self.start_page = int(start_page)
        super().__init__(**kwargs)

## ----------------------------GETTING GAMES URLs-------------------------------  

    def parse(self, response):
        ## Creating the loading bar!
        # We need the last number for ETA
        last_page_num = int(response.css('.last_page a ::text').get())
        # We check the page in which we are for as we only need to summon the loading bar in the first page
        current_page = int(response.css('.active_page span ::text').get()) - 1
        if current_page == self.start_page:
            self.pbar = tqdm(total=last_page_num - self.start_page, desc="Listing games", ascii=True, unit="page")

        ## The scrapping  
        # System for items_per_page to work
        num_of_games_on_page = len(response.css('.product_wrap > .product_title a::attr(href)').getall())
        end = num_of_games_on_page if num_of_games_on_page <= self.items_per_page else self.items_per_page

        for x in range(0, end):
            yield {
             #Extracts the link of the game and stores it
             'f': response.css('.product_wrap > .product_title a::attr(href)')[x].get()
            }

## ---------------------------FOLLOW TO THE NEXT PAGE-------------------------

        ## TIP: You can define the selector in a variable and later use it instead of the inline code, although it's not necessary
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).get()
        ## Increase the completed value
        self.pbar.update(1)
        
        # Travelling to the next page :D
        if next_page:
            sleep(self.delay)
            yield scrapy.Request(response.urljoin(next_page))