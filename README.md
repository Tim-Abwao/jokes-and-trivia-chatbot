# Jokes & Trivia Chatbot

A simple chatbot that's fun to talk to. Powered by [Rasa][rasa].

- Number and history facts courtesy of [Numbers API][num-api].
- Jokes courtesy of <https://joke.deno.dev/>.

![screencast of the chatbot](screencast.gif)

## Getting started

1. Download the necessary files:

    ```bash
    git clone https://github.com/Tim-Abwao/jokes-and-trivia-chatbot.git
    cd jokes-and-trivia-chatbot
    ```

2. Create a virtual environment, and install the required packages:

    >**NOTE:** *Rasa* only supports python3.7 to python3.9 at time of writing.

    ```bash
    python3.9 -m venv venv
    source venv/bin/activate
    pip install -U pip
    pip install rasa
    ```

3. Use `run.sh` to launch the chatbot:

    ```bash
    bash run.sh
    ```

    The script:

    - Starts the *rasa action server*
    - Opens the demo web-page
    - Starts the *rasa server* (might take a while).

## Deployment Options

Please see [Messaging & Voice Channels][channels] for help on how to make the chatbot available on various platforms. Options include:

- Your own website
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

[rasa]: https://rasa.com
[num-api]: http://numbersapi.com
[channels]: https://rasa.com/docs/rasa/messaging-and-voice-channels/
