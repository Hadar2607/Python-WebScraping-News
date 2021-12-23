# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:09:11 2021

@author: hadar
"""

from bs4 import BeautifulSoup
from news import news
from datetime import datetime

class ynet(news):
    
    def __init__(self):
          news.__init__(self,"https://www.ynet.co.il/news/category/184")
          self.quotes=[]  # a list to store quotes
   
    def appendData(self):
        continer = self.soup.findAll('div', attrs = {'class':'titleRow'}) 
        for x in continer:
            quote = {}
            quote['title'] = x.text
            t=x.div.span["data-wcmdate"].split('T')
            t[1]=t[1][0:6]
            quote['time'] = t[1]
            self.quotes.append(quote)
                  
    def getQuates(self):
        return self.quotes
              
        
