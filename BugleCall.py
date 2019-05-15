#!/usr/bin/env python

##############################################################################
#                                                               /|
#                    XYX XYX XYX  ,-.                         .' |
#,-.__________________H___H___H__(___)_____________________,-'   |
#| ||__________________________________________ ___ `._____      |
#`-"   / /           | | | | | |               |   `. \    `-.   |
#     | |            | | _ | | |   ,-.         |    | |       `. |
#     | |    ________| ,"_)| | |__(___)________|_   | |         \|
#     ' \  .' ________).`-.|-| |_______________|_\_.' / |
#      \ `-`._________)|`-'|-| |____________________.'@/
#       `------------|_| |_| |_|-----------------'J `-'
#
# Author: Timothy Clark
# Version: 2.0
# Git:
############################################################################

import schedule
import subprocess
import time
import mysql.connector
import pandas as pd
from pandas import DataFrame as df

connection = mysql.connector.connect(host='PI/ipAddress',
                            user='*******',
                            passwd='*****',
                            db='*****',
                            charset='utf8',
                            use_unicode= True)
cursor = connection.cursor()
df = pd.read_sql("SELECT * FROM Schedule; ", con=connection )

def steele():
    subprocess.call(['C:/Users/Grant Clark/calls/steele1.mp3'], shell=True)
def fatigue():
    subprocess.call(['C:/Users/Grant Clark/calls/fatigue1.mp3'], shell=True)
def assembly():
    subprocess.call(['C:/Users/Grant Clark/calls/assembly1.mp3'], shell=True)

for (index, row) in df.iterrows():
    day = df.at[index,'Day'] # This is the tweet's id
    calltime = df.at[index,'Time'] # when the tweet posted
    call = df.at[index,'BugleCall'] # content of the tweet

    if day == 'monday':
        if call == 'steele':
            schedule.every().monday.at(calltime).do(steele)
        elif call == 'fatigue':
            schedule.every().monday.at(calltime).do(fatigue)
        elif call == 'assembly':
            schedule.every().monday.at(calltime).do(assembly)
    elif day == 'tuesday':
        if call == 'steele':
            schedule.every().tuesday.at(calltime).do(steele)
        elif call == 'fatigue':
            schedule.every().tuesday.at(calltime).do(fatigue)
        elif call == 'assembly':
            schedule.every().tuesday.at(calltime).do(assembly)

    elif day == 'wednesday':
        if call == 'steele':
            schedule.every().wednesday.at(calltime).do(steele)
        elif call == 'fatigue':
            schedule.every().wednesday.at(calltime).do(fatigue)
        elif call == 'assembly':
            schedule.every().wednesday.at(calltime).do(assembly)
    elif day == 'thursday':
        if call == 'steele':
            schedule.every().thursday.at(calltime).do(steele)
        elif call == 'fatigue':
            schedule.every().thursday.at(calltime).do(fatigue)
        elif call == 'assembly':
            schedule.every().thursday.at(calltime).do(assembly)
    elif day == 'friday':
        if call == 'steele':
            schedule.every().friday.at(calltime).do(steele)
        elif call == 'fatigue':
            schedule.every().friday.at(calltime).do(fatigue)
        elif call == 'assembly':
            schedule.every().friday.at(calltime).do(assembly)
    elif day == 'saturday':
        if call == 'steele':
            schedule.every().saturday.at(calltime).do(steele)
        elif call == 'fatigue':
            schedule.every().saturday.at(calltime).do(fatigue)
        elif call == 'assembly':
            schedule.every().saturday.at(calltime).do(assembly)
    elif day == 'sunday':
        if call == 'steele':
            schedule.every().sunday.at(calltime).do(steele)
        elif call == 'fatigue':
            schedule.every().sunday.at(calltime).do(fatigue)
        elif call == 'assembly':
            schedule.every().sunday.at(calltime).do(assembly)


while True:
    schedule.run_pending()
    time.sleep(1)
