# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 09:17:38 2021

@author: hadar
"""

from bs4 import BeautifulSoup
from news import news
from datetime import datetime



class mako(news):
    
    def __init__(self):
          news.__init__(self,"https://www.mako.co.il/news-news-flash")
          self.quotes=[]  # a list to store quotes
   
    def appendData(self):
        continer = self.soup.findAll('h3', attrs = {'class':"title"}) 
        splinter=""
        for x in continer:
            quote = {}
            splinter = x.text.split("|")
            quote['title'] = splinter[1]
            quote['time'] = splinter[0]
            self.quotes.append(quote)          
        d = datetime.now().strftime("%Y_%m_%d");
        filename= r'C:\Users\hadar\Desktop\check\news-'+d +".csv"
        
            
    def getQuates(self):
        return self.quotes

