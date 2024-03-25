import datetime as dt
# dt- give it an alias

# current = dt.datetime.now()
# print(current)
# print(current.date()) #prints only date
# print(current.time()) #prints only time
# print(current.weekday()) 
# print(current.isoweekday()) 
# print(current.day) #prints only day
# print(current.year) #prints only year
# print(current.month) #prints only month
# print(current.hour)
# print(current.strftime('%H')) #- string format time function
# print(current.strftime('%S')) #- string format time function
# print(current.strftime('%H:%M:%S')) #- string format time function
# print(current.strftime('%d:%m:%y')) #- string format time function

# set_datetime = dt.datetime(2025,12,23,3,45,55,34)
# print(set_datetime)


# %a	Weekday, short version	Wed	

# %A	Weekday, full version	Wednesday	

# %w	Weekday as a number 0-6, 0 is Sunday	3	

# %d	Day of month 01-31	31	

# %b	Month name, short version	Dec	

# %B	Month name, full version	December	

# %m	Month as a number 01-12	12	

# %y	Year, short version, without century	18	

# %Y	Year, full version	2018	

# %H	Hour 00-23	17	

# %I	Hour 00-12	05	

# %p	AM/PM	PM	

# %M	Minute 00-59	41	

# %S	Second 00-59	08	

# %f	Microsecond 000000-999999	548513	

# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	

# %U	Week number of year, Sunday as the first day of week, 00-53	52	

# %W	Week number of year, Monday as the first day of week, 00-53	52	

# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	

# %C	Century	20	

# %x	Local version of date	12/31/18	

# %X	Local version of time	17:41:00	
# # %%	A % character	%	

# %G	ISO 8601 year	2018	

# %u	ISO 8601 weekday (1-7)	1	

# %V	ISO 8601 weeknumber (01-53)	01	


import time
import pygame
file = (r'C:\Users\okanl\OneDrive\Documents\Python\Kizz-Daniel-My-G-(JustNaija.com).mp3')

# pygame.init()
# pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer.music.stop



while True:
    tm = dt.datetime.now()
    # remind = tm.strftime(input('Enter time as hour(1-12), minute(0-59), seconds(0-59), AM/PM: '))
    hour = input('Enter time as hour(1-12): ')
    minute = input('Enter time as minute(0-59): ')
    second = input('Enter time as seconds(0-59): ')
    format = input('Enter AM/PM: ')
    if hour == dt.datetime.now() and minute == dt.datetime.now() and second == dt.datetime.now() and format == dt.datetime.now():
        print('time')
        # print("Its time to play.")
        # pygame.init()
        # pygame.mixer.music.load(file)

        # pygame.mixer.music.play()

        # time.sleep(10)
        # break

    # Stop the music
        # pygame.mixer.music.stop()

    # Quit pygame
        # pygame.quit()

    # if tm.strftime("%I") == remind and tm.strftime("%M") == "44" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
    # print("Its time to play.")

    # pygame.init()
    # pygame.mixer.music.load(file)

    # pygame.mixer.music.play()

    # time.sleep(10)

    # # Stop the music
    # pygame.mixer.music.stop()

    # # Quit pygame
    # pygame.quit()
