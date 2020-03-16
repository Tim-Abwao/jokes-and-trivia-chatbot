# Rasa chatbot with custom actions for number facts, date facts & Jokes.

A simple chatbot that's fun to talk to. Powered by [Rasa](https://rasa.com). 

Number and history facts courtesy of [Numbers API](http://numbersapi.com).

Jokes courtesy of the [Official Jokes API](https://official-joke-api.appspot.com/random_joke).

Webchat widget courtesy of [Botfront](https://github.com/botfront/rasa-webchat).

## Prerequisites
- Basic knowledge of **Python**, particularly `pip` and `venv`.
- Familiarity with **Rasa**.
- An internet connection to fetch fresh content from the joke/fact APIs.

The **rasa** folder has the files needed to modify, re-train and run the chatbot. Please check out the [rasa docs](https://rasa.com/docs/), if you haven't yet.

## Getting Started
Attempting to install the required modules from the `requirements.txt` file would reproduce the exact system state under which the chatbot ran. 
``` bash
git clone https://github.com/Tim-Abwao/rasa-chatbot.git
cd rasa-chatbot
python3 -m venv venv  #creating a virtual environment
source venv/bin/activate  #activating the virtual environment
pip install -U pip
pip install -r requirements.txt
```
However, some dependencies required for installation might interrupt this process. Please see the [installation guide](https://rasa.com/docs/rasa/user-guide/installation/) for OS - specific help.

**NOTE:** Since Rasa releases updates with major changes from time to time, future versions of Rasa might conflict with this project.


## Rasa Shell - The command line interface
1. After installation, you can train and run the chatbot using the commands:

``` bash
cd rasa
rasa train
rasa shell

```
2. For the custom actions to work, you'll need to activate the action server. Open another terminal tab (`ctrl+shift+t`) or window (`ctrl+shift+n`) and run:

``` bash
source ../venv/bin/activate
rasa run actions

```

Then head back to the terminal running the command line chatbot interface, and enter a greeting e.g. "Hi" or "Hello". Enter "/stop" to end the converstation.

## Deployment Options
Please see [Messaging & Voice Channels](https://rasa.com/docs/rasa/user-guide/messaging-and-voice-channels/) for help on how to make the chatbot available on various platforms. Options include:

- Your own website
- Facebook Messenger
- Slack
- Telegram
- Twilio
- Microsoft Bot Framework
- Cisco Webex Teams
- RocketChat
- Mattermost
- Custom Connectors

That's all. Enjoy.
