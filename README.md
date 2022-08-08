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

2. Use `run.sh` to launch the chatbot:

    ```bash
    bash run.sh
    ```

    The script:

    - activates a virtual environment with dependencies
    - starts the *rasa action server*
    - opens the demo web-page
    - starts the *rasa server* (might take a while).

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
