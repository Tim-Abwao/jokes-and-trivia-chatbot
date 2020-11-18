# Jokes, number & date trivia chatbot

A simple chatbot that's fun to talk to. Powered by [Rasa][1].

- Number and history facts courtesy of [Numbers API][2].
- Jokes courtesy of the [Official Jokes API][3].

## Prerequisites

- [Python][4], and some knowledge of *Rasa* (check out [Rasa Basics][5]).
- An internet connection to fetch content from the APIs.

## Getting started

- Download the files, and create a virtual environment:

    ```bash
    git clone https://github.com/Tim-Abwao/rasa-chatbot.git
    cd rasa-chatbot

    python3 -m venv venv
    source venv/bin/activate
    pip install -U pip
    pip install rasa Flask
    ```

- Train the chatbot, then run `run.sh` to launch it:

    ```bash
    cd trivia-chatbot && rasa train
    cd .. && bash run.sh
    ```

    The [Rasa Webchat][6] widget (by [Botfront][7]) provides a nice interface to the chatbot from websites. The `run.sh` script in the `rasa-chatbot` directory sets up a demo webpage using [flask][8], then starts the *Rasa action server* and the *Rasa* chatbot server.

    ![run script](screencasts/script-run.gif)

    Once you see the line *"Rasa server is up and running"*, head on to <localhost:5000> in your favourite browser:

    ![web widget](screencasts/web-chat.gif)

    When you're done, just close the demo webpage browser tab, and use `Ctrl + C` to terminate the *Rasa* processes running in the terminal.

    Next time you wish to start the chatbot, you'll just have to run the `run.sh` script.

    ```bash
    bash run.sh
    ```

## Deployment Options

Please see [Messaging & Voice Channels][9] for help on how to make the chatbot available on various platforms. Options include:

- Your own website *(as in the Webchat demo above)*
- Facebook Messenger
- Slack
- Telegram
- Twilio
- Microsoft Bot Framework
- Cisco Webex Teams
- RocketChat
- Mattermost
- Google Hangouts Chat
- Custom Connectors

[1]: https://rasa.com
[2]: http://numbersapi.com
[3]: https://official-joke-api.appspot.com/random_joke
[4]: https://www.python.org
[5]: https://rasa.com/docs/rasa/playground
[6]: https://github.com/botfront/rasa-webchat
[7]: https://botfront.io/
[8]: https://flask.palletsprojects.com/en/1.1.x/
[9]: https://rasa.com/docs/rasa/messaging-and-voice-channels/
