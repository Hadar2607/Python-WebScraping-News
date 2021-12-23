# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:51:58 2021

@author: hadar
"""

from bs4 import BeautifulSoup
from news import news
from datetime import datetime

class walla(news):
    
    def __init__(self):
          news.__init__(self,"https://news.walla.co.il/breaking")
          self.quotes=[]  # a list to store quotes
   
    def appendData(self):
        textHeader = self.soup.findAll('div', attrs = {'class':'body'}) 
        tim=self.soup.select(".time")
        counter = 0;
        for x in textHeader:
            quote = {}
            quote['title'] = x.h2.text
            quote['time'] = tim[counter].getText()
            self.quotes.append(quote)
            counter+=1
        d = datetime.now().strftime("%Y_%m_%d");
        filename= r'C:\Users\hadar\Desktop\check\news-'+d +".csv"
        
            
    def getQuates(self):
        return self.quotes
   
