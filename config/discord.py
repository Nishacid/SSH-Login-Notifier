#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version : 3.X
# Author         : Nishacid

import requests
from config import *

def discord_bot_send(message):
    webhook_token = config["Discord_Webhook_Token"]
    url = f"https://discord.com/api/webhooks/{webhook_token}"
    data = {"content": message}
    
    try:
        req = requests.post(url, json=data)
        return req
    except requests.Timeout:
        print("Error, request time out.")
    except requests.ConnectionError:
        print("Error, couldn't connect to server")