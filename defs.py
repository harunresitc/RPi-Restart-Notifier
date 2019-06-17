#!/usr/bin python
# -*- coding: utf-8 -*-

import os
import sys
import mySettings
import smtplib
import requests
import json

if sys.version_info > (3,):
    from urllib.request import urlopen, Request
    from urllib.error import URLError
else:
  from urllib2 import urlopen, Request
  from urllib2 import URLError

import datetime

def internet():
    try:
        urlopen('https://www.google.com', timeout=2)
        return 1
    except URLError: 
        return 0

def oldip():
    f = open(mySettings.SCRIPT_PATH+'/oldip.txt')
    return f.read()
    f.close()
    
def newip():
    #url = urllib.request
    site = urlopen('http://ipecho.net/plain')
    ip = site.read()
    ip = str(ip)
    ip = ip.strip("b")
    ip = ip.replace("'", "")

    ips = ip.split('.')
    if len(ips)!=4 or not ips[0].isdigit() or not ips[1].isdigit() or not ips[2].isdigit() or not ips[3].isdigit() or int(ips[0])>255 or int(ips[1])>255 or int(ips[2])>255 or int(ips[3])>255:
        return 0
    else:
        return ip

def logs(log):
    tm = datetime.datetime.now()
    time = datetime.datetime.strftime(tm, '%d.%m.%Y-%H.%M')
    log= time+" -> "+log+"\n"
    f=open(mySettings.SCRIPT_PATH+"/LOGS.txt","a")
    f.write(log)
    f.close()

def chaoldip(ip):
    f=open(mySettings.SCRIPT_PATH+"/oldip.txt","w")
    f.write(ip)
    f.close()

def send_email(subject,msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(mySettings.senderaddress, mySettings.senderpassword)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(mySettings.senderaddress, mySettings.recaddress, message)
        server.quit()
        return 1
    except:
        return 0


'''
Pushbullet Function
Edit from: https://simply-python.com/tag/pushbullet/
'''
if sys.version_info > (3,):
    from urllib.request import urlopen, Request
    from urllib.error import URLError, HTTPError
else:
    from urllib2 import urlopen, Request
    from urllib2 import URLError, HTTPError

pbACCESS_TOKEN="o.ggr8aMEH60dGk8Brjr2PSra8Exz3tfMx"
pbMsgTitle="Raspberry Warning"

def pushbullet(msg):

    data_send = {"type": "note", "title": pbMsgTitle, "body": msg}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + pbACCESS_TOKEN, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        
        e=resp.status_code
        
        if e==400:
            msg="{} Bad Request - Usually this results from missing a required parameter.".format(e)
            return msg
        elif e==401:
            msg="{} Unauthorized - No valid access token provided.".format(e)
            return msg
        elif e==403:
            msg="{} Forbidden - The access token is not valid for that request.".format(e)
            return msg
        elif e==404:
            msg="{} Not Found - The requested item doesn't exist.".format(e)
            return msg
        elif e==429:
            msg="{} Too Many Requests - You have been ratelimited for making too many requests to the server.".format(e)
            return msg
        else:
            msg="Cause of error: {} For more details: https://docs.pushbullet.com/#http-status-codes".format(e)
            return msg

    else:
        return 1
