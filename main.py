#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version : 3.X
# Author         : Nishacid

import re
import subprocess
import json
import sys
from datetime import datetime
import socket
import requests
sys.path.insert(1, '/opt/SSH-Login/config/') # Change it
from telegram import telegram_bot_send
from discord import discord_bot_send
from config import *

def is_login():
    
    # Infos
    ip_pattern = re.compile("Accepted password for [a-zA-Z]* from (.*?) port")
    login_pattern = re.compile("_unix\((.*?)ened for")
    user_pattern = re.compile("Accepted password for ([a-zA-Z]*) from")
    hostname = socket.gethostname()
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    # Get Logs
    out = subprocess.Popen(['tail', '-10', '/var/log/auth.log'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = out.communicate()
    result = stdout.decode('ascii')
    
    if login_pattern.search(result):
        ip_search = ip_pattern.search(result)
        if ip_search:
            ip = ip_search.group(1)
            user_search = user_pattern.search(result)
            if user_search:
                user = user_search.group(1)
                message = f"New SSH login on server {hostname} with {user} at {date} with IP : {ip}\n{abuseipdb(ip)}"
                plateform = config["Plateform"]
                if plateform == "telegram":
                    telegram_bot_send(message)
                elif plateform == "discord":
                    discord_bot_send(message)
                else:
                    print("There is a problem with the plateform, check the conf.py file")
def abuseipdb(ip):
     
    # Defining the api-endpoint
    api_url = 'https://api.abuseipdb.com/api/v2/check'
    api_key = config["Abuse_API_Key"]

    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    try:
        response = requests.get(url=api_url, headers=headers, params=querystring)
        # Formatted output
        decodedResponse = json.loads(response.text)

       # print(json.dumps(decodedResponse, sort_keys=True, indent=4)) # get all datas from API
        abuseScore = decodedResponse["data"]["abuseConfidenceScore"]
        country = decodedResponse["data"]["countryCode"]
        reports = decodedResponse["data"]["totalReports"]

        abuse_message = f"The IP come from {country} and she has a abuse score of {abuseScore}/100, which is reported {reports} times on abuseipdb.com \nMore information here : https://abuseipdb.com/check/{ip}"
        return abuse_message
    
    except requests.ConnectionError:
        print("Error, couldn't connect to server")
        sys.exit()
    except requests.Timeout:
        print("Error, request time out.")
        sys.exit()
    
if __name__ == "__main__":
    is_login()