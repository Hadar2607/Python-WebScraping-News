# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:35:36 2021

@author: hadar
"""

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

class news:
    
    def __init__(self,url):
      r = requests.get(url)
      self.soup = BeautifulSoup(r.content,"html5lib")
      
        
    def getSoup(self):
        return self.soup
        
    def writeToFile(self,filePath,dataContect,site):
        with open(filePath, 'a', newline='') as f:
            w = csv.DictWriter(f,['time','title',site])
            w.writeheader()
            for quote in dataContect:
                w.writerow(quote)
        
        
