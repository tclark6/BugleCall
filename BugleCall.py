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
# Version: 1.0
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

# Friday Schedule
schedule.every().friday.at('18:02').do(steele)
# Saturday Schedule

#Sunday Schedule

while True:
    schedule.run_pending()
    time.sleep(1)
