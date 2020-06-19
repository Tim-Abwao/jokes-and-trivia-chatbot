# Rasa chatbot with custom actions for number facts, date facts & Jokes

A simple chatbot that's fun to talk to. Powered by [Rasa](https://rasa.com).

> Number and history facts courtesy of [Numbers API](http://numbersapi.com).

> Jokes courtesy of the [Official Jokes API](https://official-joke-api.appspot.com/random_joke).

## Prerequisites

- Familiarity with **Rasa**. Please check out [rasa basics](https://rasa.com/docs/rasa/user-guide/rasa-tutorial/), if you haven't yet.
- An internet connection to fetch content from the joke and fact APIs.

The **rasa** folder has the files needed to modify, train and run the chatbot.

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

- First, activate the **action server**, to enable the *custom actions*. Open another terminal tab (<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>T</kbd>) or window (<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>N</kbd>) and run:

```bash
source ../venv/bin/activate
rasa run actions
```

![Rasa actions animation](/rasa/animations/rasa_actions.svg)<br>
<sub>Please note that the stopping (<kbd>ctrl</kbd>+<kbd>C</kbd>) and `exit` commands are used here just to make the animation brief. The action server has to be running for the custom actions to work.</sub>

- Afterwards, head back to the original terminal window(or tab) where you downloaded the files. You can re-train and run the chatbot using the commands:

```bash
cd rasa
rasa train
rasa shell
```

![Rasa shell animation](/rasa/animations/rasa_shell.svg)<br>
<sub>If you're curious about the warnings and errors that appear at the beginning, please have a look at [this question](https://stackoverflow.com/questions/60368298/could-not-load-dynamic-library-libnvinfer-so-6).</sub>

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
