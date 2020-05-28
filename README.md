# Rasa chatbot with custom actions for number facts, date facts & Jokes

A simple chatbot that's fun to talk to. Powered by [Rasa](https://rasa.com).

Number and history facts courtesy of [Numbers API](http://numbersapi.com).

Jokes courtesy of the [Official Jokes API](https://official-joke-api.appspot.com/random_joke).

## Prerequisites

- Familiarity with **Rasa**. Please check out [rasa basics](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/), if you haven't yet.
- An internet connection to fetch content from the joke and fact APIs.

The **rasa** folder has the files needed to modify, re-train and run the chatbot.

## Getting Started

- Download the files, and create a virtual environment:

```bash
git clone https://github.com/Tim-Abwao/rasa-chatbot.git
cd rasa-chatbot
python3 -m venv venv  #creating a virtual environment
source venv/bin/activate  #activating the virtual environment
pip install -U pip
pip install -r requirements.txt
```

## Rasa Shell - The command line interface

- You can train and run the chatbot using the commands:

```bash
cd rasa
rasa train
rasa shell
```

- For the *custom actions* to work, you'll need to activate the **action server**. Open another terminal tab (<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>T</kbd>) or window (<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>N</kbd>) and run:

```bash
source ../venv/bin/activate
rasa run actions
```

Then head back to the initial terminal with the command line chatbot interface active, and enter a greeting e.g. "Hi" or "Hello". Enter "/stop" to end the converstation.

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
