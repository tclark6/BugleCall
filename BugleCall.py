
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
# Version: 1.1
# Git:https://github.com/tclark6/BugleCall
############################################################################

import schedule
import subprocess
import time

# call MP3s
def steele():
    subprocess.call(['C:/Users/Grant Clark/calls/steele1.mp3'], shell=True)
def fatigue():
    subprocess.call(['C:/Users/Grant Clark/calls/fatigue1.mp3'], shell=True)
def assembly():
    subprocess.call(['C:/Users/Grant Clark/calls/assembly1.mp3'], shell=True)
# Wednesday Schedule
schedule.every().wednesday.at('14:55').do(fatigue)
schedule.every().wednesday.at('15:00').do(assembly)
schedule.every().wednesday.at('15:50').do(steele)
schedule.every().wednesday.at('16:00').do(steele)
schedule.every().wednesday.at('16:50').do(steele)
schedule.every().wednesday.at('17:00').do(steele)
schedule.every().wednesday.at('17:50').do(steele)
# Friday Schedule
schedule.every().friday.at('18:55').do(fatigue)
schedule.every().friday.at('19:00').do(assembly)
schedule.every().friday.at('19:50').do(steele)
schedule.every().friday.at('20:00').do(steele)
schedule.every().friday.at('20:50').do(steele)
schedule.every().friday.at('21:00').do(steele)
schedule.every().friday.at('21:50').do(steele)
# Saturday Schedule
schedule.every().saturday.at('13:55').do(fatigue)
schedule.every().saturday.at('14:00').do(assembly)
schedule.every().saturday.at('14:50').do(steele)
schedule.every().saturday.at('15:00').do(steele)
schedule.every().saturday.at('15:50').do(steele)
schedule.every().saturday.at('16:00').do(steele)
schedule.every().saturday.at('16:50').do(steele)

schedule.every().saturday.at('19:55').do(fatigue)
schedule.every().saturday.at('20:00').do(assembly)
schedule.every().saturday.at('20:50').do(steele)
schedule.every().saturday.at('21:00').do(steele)
schedule.every().saturday.at('21:50').do(steele)
#Sunday Schedule
schedule.every().sunday.at('13:55').do(fatigue)
schedule.every().sunday.at('14:00').do(assembly)
schedule.every().sunday.at('14:50').do(steele)
schedule.every().sunday.at('15:00').do(steele)
schedule.every().sunday.at('15:50').do(steele)
schedule.every().sunday.at('16:00').do(steele)
schedule.every().sunday.at('16:50').do(steele)
schedule.every().sunday.at('17:00').do(steele)
schedule.every().sunday.at('17:50').do(steele)

while True:
    schedule.run_pending()
    time.sleep(1)
