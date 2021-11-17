# SSH Login Notifier

SSH-Login-Notifier is a script for ensure you'r server monitoring with notify you when a SSH login is estabilshed.

It can be used on any type of server, like a personal server, a honeypot, a professional server or other.

This script use the [Abuseipdb](https://abuseipdb.com) API. \
AbuseIPDB is a project dedicated to helping combat the spread of hackers, spammers, and abusive activity on the internet. 

AbuseIPDB will help you to know how an IP is malicious or not with her `Confidence Abuse score`. 
Higher is the score, more the IP is reported as malicious.


## 🛠️ Installation

```bash
# Of course you can change the path-name, but you need to edit the main.py file
git clone https://github.com/Nishacid/SSH-Login-Notifier.git /opt/SSH-Login
cd /opt/SSH-Login
python3 -m pip install -r requirements.txt
```

## ⚙️ Configuration 

### 1. Config.py

Once you have cloned the repository, you need to setup a [Telegram Bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot) or a [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks). Next set the Token on the config file. 

Then you need to create an account on [abuseipdb.com](https://abuseipdb.com/) (it's free) and add you'r API Key on the `config.py` file.

Finally, you must choose the platform on which the message will be sent.

Note: for the moment you can't use Discord and Telegram at the same time, choose only one platform.


### 2. Server setup

After, edit the `~/.bashrc` file on the `home` directory of the user who want to monitoring and add the following line :

```bash
if [[ -n $SSH_CONNECTION ]] ; then
    python3 /opt/SSH-Login/main.py # or your custom path
fi
```

This will execute the script when an SSH connection is established.

## 📨 Exemple 

Example of a message received from the bot :

### Telegram 

![Telegram](https://i.imgur.com/eFblcFs.png)

### Discord 

![Discord](https://i.imgur.com/ul2HPds.png)
