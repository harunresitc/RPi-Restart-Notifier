#!/usr/bin python
# -*- coding: utf-8 -*-
'''
Written by Harun Reşit Çakaltarla
Version 1.0 Beta
http://hrc.karaliyor.com
'''

import os
import mySettings
import defs

intresult=defs.internet()
if(intresult==0):
    defs.logs("No Internet connection!")
    newip=0
else:
    oldip=defs.oldip()
    newip=defs.newip()
    
    if(newip==0):
        defs.logs("Could not get a valid IP")


if intresult!=0:
            
    if(mySettings.emailnot==1):
        mailreport = "Raspberry restarted! \nExternal IP: "+newip+"\n"
        mailsendreport=defs.send_email(mySettings.mailsubject,mailreport)
        if(mailsendreport==0):
            defs.logs("E-mailError: E-mail could not be send!")
    
    if(mySettings.pushbulletnot==1):
        pushbulletreport = "Raspberry restarted! \nExternal IP: "+newip+"\n"
        res=defs.pushbullet(pushbulletreport)
        if(res!=1):
            defs.logs("Pushbullet Error: "+res)
            print(res)
    
    wl="Raspberry restarted! External IP: "+newip
    defs.logs(wl)
    
    defs.chaoldip(newip)
