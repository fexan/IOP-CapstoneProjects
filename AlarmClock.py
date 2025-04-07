'''
Author: Ifeoluwa Oyelowo-Paul
Date: April 7, 2025


Alarm Clock - 
A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
'''

import datetime
from datetime import time
from datetime import datetime
from datetime import timedelta # this class for datetime math operations
import re #regex lib
import calendar
from time import sleep
from playsound import playsound #module for playing mp3


# Get number of mins/secs from user or a particular time
user_selection = ''
while not(user_selection == 'm' or user_selection =='s' or user_selection=='t'):
    user_selection = input("When will you like the sound to be played? minutes(m), seconds(s) or a particular time(t): ")

current_datetime = datetime.now()
print(f"This is the current time: {current_datetime}")

# if else for different scenarios
if user_selection =='m':
    mins = input("Enter the number of minutes you will like the sound to be played (integer): ")
    while not mins.isdigit():
        mins = input("Enter the number of minutes you will like the sound to be played (integer): ")
    
    mins = int(mins)
    mins_delta = timedelta(minutes=mins)
    play_datetime = current_datetime + mins_delta
    print(f'Sound will be played at {play_datetime}')
elif user_selection =='s':
    secs = input("Enter the number of seconds you will like the sound to be played (integer): ")
    while not secs.isdigit(): #intentional so we can use .isdigit()
        secs = input("Enter the number of seconds you will like the sound to be played (integer): ")
    
    secs = int(secs)    
    secs_delta = timedelta(seconds=secs)
    play_datetime = current_datetime + secs_delta
    print(f'Sound will be played at {play_datetime}')
elif user_selection == 't':

    #Create regex for yyyy-mm-dd hh:mm:ss values
    #yyyy must be btw 2025 and 2999
    yyyy = r"(20[2-9][5-9]|2[1-9][0-9][0-9])"
    #mm must be btw 1 and 12
    mm = r"(1[0-2]|0?[1-9])"
    #dd must be btw 1 and 31 -- 30 day months will be accounted for later based on the user's input
    dd = r"(3[0-1]|[1-2][0-9]|0?[1-9])"
    #hh must be btw 0 and 23
    hh = r"([0-1]?[0-9]|2[0-3])"
    #mm must be btw 0 and 59
    t_mm = r"([0-9]|[0-5]?[0-9])" #to enforce 2 digits, Remove ?. ie ([0-9]|[0-5][0-9])
    #ss must be btw 0 and 59
    ss = r"([0-9]|[0-5][0-9])"

    #date_regex = '-'.join((yyyy,mm,dd)) #.join requires a list, tuple etc of strings
    #date_regex = "^(" + date_regex + ")$" # full string should match regex not partial
    time_regex = ':'.join((hh,t_mm,ss))
    time_regex = "^("+time_regex+")$" # full string should match regex not partial

    user_date_yyyy = input("Enter the exact year you'll like the sound to be played (yyyy): ")
    while re.search("^(" + yyyy + ")$", user_date_yyyy) == None: # If no match found, continue asking for a valid year 
        user_date_yyyy = input("Enter the exact year you'll like the sound to be played (yyyy): ")

    print("\n")

    user_date_mm = input("Enter the exact month you'll like the sound to be played (mm): ")
    while re.search("^(" + mm + ")$", user_date_mm) == None: # If no match found, continue asking for a valid month 
        user_date_mm = input("Enter the exact month you'll like the sound to be played (mm): ")

    # adjust regex for mm depending on user's input
    # 30 days for 04, 06, 09, 11
    # 28 days for Feb, unless it's a leap year
    if user_date_mm == ('04' or '06' or '09' or '11'):
        dd = r"(30|[1-2][0-9]|0?[1-9])"
    elif user_date_mm == '02':
        if calendar.isleap(int(user_date_yyyy)): #leap year has 29 days in feb
            dd = r"([1-2][0-9]|0?[1-9])"
        else:
            dd = r"(2[0-8]|1[0-9]|0?[1-9])" #non-leap year goes up till 28 days in feb
    
    print("\n")

    user_date_dd = input("Enter the exact day you'll like the sound to be played (dd): ")
    while re.search("^(" + dd + ")$", user_date_dd) == None: # If no match found, continue asking for a valid day 
        user_date_dd = input("Enter the exact day you'll like the sound to be played (dd): ")

    user_date = '-'.join((user_date_yyyy,user_date_mm,user_date_dd))
    play_date = user_date.split('-')

    print("\n")

    


    user_time = input("Enter the exact time you'll like the sound to be played (hh:mm:ss): ")
    while re.search(time_regex, user_time) == None: # If no match found, continue asking for a valid time 
        user_time = input("Enter the exact time you'll like the sound to be played (hh:mm:ss): ")

    print(f"The sound will be played on {user_date} at {user_time}")

    
    play_time = user_time.split(':')
    play_datetime = datetime(year=int(play_date[0]),month=int(play_date[1]),day=int(play_date[2]),hour=int(play_time[0]),minute=int(play_time[1]),second=int(play_time[2]))
    print(play_datetime)

else:
    #something went wrong
    print("Ending session.")

wait_secs = (play_datetime - datetime.now()).total_seconds()
print(wait_secs)
sleep(wait_secs) #sleep until it's time to play audio
# Now that we have play_datetime, play the sound at the specified time
if (datetime.now() - play_datetime).total_seconds() <= 10: #account for precision differences
    playsound("/Users/iop/Development/PythonProjects/CapstoneProjects/roar-sounds.mp3") #use full file path if file was in a different dir to .py script