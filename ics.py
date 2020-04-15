from plyer import notification
import requests
import bs4
import os

currDir = os.getcwd()
if 2 > 1:
    print('Works!')
    notification.notify(
        title='Charles is streaming!',
        message='https://www.twitch.tv/iamcharlesleclerc16',
        app_name='ics',
        app_icon=currDir + '/imgs/icon.ico'
    )
