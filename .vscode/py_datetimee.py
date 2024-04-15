import datetime
import time
import pygame
alarmHour = int(input('Enter Hour: '))
alarmMin = int(input('Enter Minutes: '))
alarmAm = input('am/pm: ')

if alarmAm == 'pm':
    alarmHour += 12

file = (r'C:\Users\okanl\OneDrive\Documents\Python\Kizz-Daniel-My-G-(JustNaija.com).mp3')

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        print('Playing...')
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(10)
        break
