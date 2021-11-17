#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version : 3.X
# Author         : Nishacid

import requests
from config import *

def telegram_bot_send(message):
    bot_token = config["Telegram_Bot_Token"]
    bot_chatID = config["Telegram_Bot_ChatID"]
    
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&text={message}'
    
    try:
        req = requests.get(url)
        return req
    except requests.Timeout:
        print("Error, request time out.")
    except requests.ConnectionError:
        print("Error, couldn't connect to server")