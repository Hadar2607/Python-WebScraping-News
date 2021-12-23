# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 11:46:33 2021

@author: hadar
"""
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from datetime import datetime

class sendData:
    
    def __init__(self,emailfrom,emailto,fileToSend):
          self.emailfrom = emailfrom
          self.emailto = emailto
          self.fileToSend = fileToSend


    def msgContent(self):        
        d = datetime.now().strftime("%Y_%m_%d");
        msg = MIMEMultipart()
        msg["From"] = self.emailfrom
        msg["To"] = self.emailto
        msg["Subject"] = "news: "+d
        msg.preamble = ""
        return msg;

            
    def readFile(self,msg):
        ctype, encoding = mimetypes.guess_type(self.fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1) 
        fp = open(self.fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=self.fileToSend)
        msg.attach(attachment)
        return msg;
        
    def connection(self,msg,username,password):
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username,password)
        server.sendmail(self.emailfrom, self.emailto, msg.as_string())
        server.quit()