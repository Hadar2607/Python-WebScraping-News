# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:38:48 2021

@author: hadar
"""

from bs4 import BeautifulSoup
from news import news
from datetime import datetime


class mariv(news):
    
    def __init__(self):
          news.__init__(self,"https://www.maariv.co.il/breaking-news")
          self.quotes=[]  # a list to store quotes
   
    def appendData(self):
        continer = self.soup.findAll('div', attrs = {'class':'breaking-news-item'}) 
        timex =self.soup.findAll('div', attrs = {'class':'breaking-news-item-time'}) 
        count = 0;
        for x in continer:
            quote = {}
            quote['time'] = timex[count].text
            quote['title'] = x.span.text
            self.quotes.append(quote)
            count +=1
                 
    def getQuates(self):
        return self.quotes

   