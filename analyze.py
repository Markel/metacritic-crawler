# This file gets the information of the games you have collected previously on games.py
# The program runs using 'scrapy runspider analyze.py'
# This file should take around 2 hours to completed
# This file is NOT a final build, expect MANY bugs, especially skipping games crawl.
# Remember that you MUST comply with the point 11.13 of the terms of use in Metacritic (https://www.cbsinteractive.com/legal/cbsi/terms-of-use), you need the permission of Cbs Interactive to run any kind of scraping (this is a scraping tool if you didn't know it btw)
# You bear all responsibility about the use of this program

import scrapy
from time import sleep
import sqlite3
from sqlite3 import Error
import re

## ---------------------------OPEN GAME LINKS FILE------------------------------

def parse_url(route):
    return 'https://www.metacritic.com' + re.findall(r'\"(.+?)\"', route)[1]

with open ("gm.jl", "r") as myfile:
    games_list = [parse_url(line) for line in myfile]
    
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

def extract_value(res, text_path):
    value = res.css(text_path).get()
    return value if value is None else value.strip()

class DetailsSpider(scrapy.Spider):
    name = "Details"
    start_urls = games_list

## ----------------------------------CRAWL-------------------------------------    
    def parse(self, response):
        t = extract_value(response, '.product_title a.hover_none h1 ::text')
        ## Platform
        p = extract_value(response, '.product_title span.platform ::text')
        ## Company
        c = extract_value(response, 'div.product_data ul.summary_details li.publisher span.data a ::text')
        ## Release Date
        r = extract_value(response, 'div.product_data ul.summary_details li.release_data span.data  ::text')
        ## Game description
        d = extract_value(response, 'div.product_details div.main_details ul.summary_details li.summary_detail span.data span.inline_collapsed span.blurb_expanded ::text')
        ## Metascore
        cs = extract_value(response, '.metascore_w span ::text')
        ## Critics Description
        cd = extract_value(response, 'div.summary p span.desc ::text')
        ## Critics Count
        cn = extract_value(response, 'div.summary p span.count a span ::text')
        ## User Score
        us = extract_value(response, 'div.userscore_wrap a.metascore_anchor div.user ::text')
        ## User Description
        ud = extract_value(response, 'div.userscore_wrap div.summary p span.desc ::text')
        ## User Count
        un = extract_value(response, 'div.userscore_wrap div.summary p span.count a ::text')
        ## Number of players
        pl = extract_value(response, 'div.product_details div.side_details ul.summary_details li.product_players span.data ::text')
        ## Rating (ESRB)
        rt = extract_value(response, 'div.product_details div.side_details ul.summary_details li.product_rating span.data ::text')
        
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
