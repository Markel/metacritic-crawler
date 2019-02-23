# This file gets the information of the games you have collected previously on games.py
# The file is not prepared and needs formatting before starting this script
# You must replace all the '{"f": "' for 'https://www.metacritic.com' and also you must remove all the '"}' (The final file should have an standard URL per line)
# Once this is ready you can run the program using 'scrapy runspider analyze.py'
# This file should take around 2 hours to completed
# This file is NOT a final build, expect MANY bugs, especially skipping games crawl.
## Remember that you MUST comply with the point 11.13 of the terms of use in Metacritic (https://www.cbsinteractive.com/legal/cbsi/terms-of-use), you need the permission of Cbs Interactive to run any kind of scraping (this is a scraping tool if you didn't know it btw)
## You bear all responsibility about the use of this program

import scrapy
import win32api
from time import sleep
import sqlite3
from sqlite3 import Error

## ---------------------------OPEN GAME LINKS FILE------------------------------

with open ("gm.jl", "r") as myfile:
    games_list=myfile.readlines()
    
## -------------------------------SQLITE STUFF----------------------------------

## Special thanks to hypertaboo for his code: https://gist.github.com/hypertaboo/4464096

# It creates a SQLite database (take care that it doesn't already exist)
cnn = sqlite3.connect('games.db')
mycursor = cnn.cursor()

# Create the games table (named data)
sql_new_table = '''create table data
(title text, platform text, company text, release text, description text, metascore integer, critics_desc text, critics_count integer, user_score real, user_desc text, user_count integer, players text, rating text)'''
mycursor.execute(sql_new_table)

cnn.commit()


## ----------------------------DEFINING THE SPIDER------------------------------

class DetailsSpider(scrapy.Spider):
    name = "Details"
    start_urls = games_list

## ----------------------------------CRAWL-------------------------------------    

    def parse(self, response):
        ## Title
        t = response.css('.product_title a.hover_none h1 ::text').extract_first()
        ## Platform
        p = response.css('.product_title span.platform ::text').extract_first().strip()
        ## Company
        c = response.css('div.product_data ul.summary_details li.publisher span.data a ::text').extract_first().strip()
        ## Release Date
        r = response.css('div.product_data ul.summary_details li.release_data span.data  ::text').extract_first()
        ## Game description
        d = response.css('div.product_details div.main_details ul.summary_details li.summary_detail span.data span.inline_collapsed span.blurb_expanded ::text').extract_first() 
        ## Metascore
        cs = response.css('.metascore_w span ::text').extract_first()
        ## Critics Description
        cd = response.css('div.summary p span.desc ::text').extract_first().strip()
        ## Critics Count
        cn = response.css('div.summary p span.count a span ::text').extract_first()
        ## User Score
        us = response.css('div.userscore_wrap a.metascore_anchor div.user ::text').extract_first()
        ## User Description
        ud = response.css('div.userscore_wrap div.summary p span.desc ::text').extract_first()
        ## User Count
        un = response.css('div.userscore_wrap div.summary p span.count a ::text').extract_first()
        ## Number of players
        pl = response.css('div.product_details div.side_details ul.summary_details li.product_players span.data ::text').extract_first()
        ## Rating (ESRB)
        rt = response.css('div.product_details div.side_details ul.summary_details li.product_rating span.data ::text').extract_first() 
        
## --------------------------INSERT DATA INTO THE SQL----------------------------        

        # Establishing all the variable in one single variable
        game_d = [(t, p, c, r, d, cs, cd, cn, us, ud, un, pl, rt)]

        # Inserting the data on the SQL database
        mycursor.executemany('''insert into data values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', game_d)
        cnn.commit()

##------- DEBUGGING OPTIONS ------ ##
##        print(game_d)
##        print(t)
##        print(p)
##        print(c)
##        print(r)
##        print(d)
##        print(cs)
##        print(cd)
##        print(cn)
##        print(us)
##        print(ud)
##        print(un)
##        print(pl)
##        print(rt)
