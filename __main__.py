# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:31:36 2021

@author: hadar
"""


from sendData import sendData
from news import news
from ynet import ynet
from mariv import mariv
from walla import walla
from mako import mako
from datetime import datetime


def main():  
    
    nameFile = datetime.now().strftime("%Y_%m_%d");
    path = r'C:\Users\hadar\Desktop\check\news-'+nameFile +".csv"
    
    ynetObj = ynet()
    ynetSoup = ynetObj.getSoup()
    ynetObj.appendData()
    arrData = ynetObj.getQuates() 
    ynetObj.writeToFile(path,arrData,"ynet")

    marivObj = mariv()
    marivSoup = marivObj.getSoup()
    marivObj.appendData()
    arrData = marivObj.getQuates()
    marivObj.writeToFile(path,arrData,"mariv")

    wallaObj = walla()
    wallaSoup = wallaObj.getSoup()
    wallaObj.appendData()
    arrData = wallaObj.getQuates()
    wallaObj.writeToFile(path,arrData,"walla")
    
    makoObj = mako()
    makoSoup = makoObj.getSoup()
    makoObj.appendData()
    arrData = makoObj.getQuates()
    makoObj.writeToFile(path,arrData,"mako")
    sendFile(path)
    
    
def sendFile(path):  
      fromEmail = input("your email:")
      toEmail = input ("destination email:")
      send = sendData(fromEmail,toEmail,path)
      msg = send.msgContent()
      a = send.readFile(msg)
      user = input("write your user name: ")
      password = input("write your pass: ")
      send.connection(a,user,password)
   
  

   
if __name__ == "__main__": 
    main()
    
  