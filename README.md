# Rasa Chatbot with Custom Actions for  Number Facts, Date Facts & Jokes.

A simple chatbot that's fun to talk to. Powered by [Rasa](https://rasa.com). 

Number and history facts courtesy of [Numbers API](http://numbersapi.com).
Jokes courtesy of the [Official Jokes API](https://official-joke-api.appspot.com/random_joke).
Webchat widget courtesy of [Mr. Bot](https://github.com/mrbot-ai/rasa-webchat).

The **rasa** directory has the files needed to modify, re-train and run the chatbot. Please check out the [rasa docs](https://rasa.com/docs/), if you haven't yet.

The **flask-app** directory has a flask app you can use to host the webchat widget and talk to the bot. See [Messaging & Voice Channels](https://rasa.com/docs/rasa/user-guide/messaging-and-voice-channels/) for a list of interesting ways to deploy the chatbot.

## Prerequisites
- You'll need Python. It's considered good practice to whip up a virtual environment. 
- Familiarity with Rasa. Familiarity with [Flask](https://palletsprojects.com/p/flask/) too, but this is optional.
- Install Rasa. See [installation](https://rasa.com/docs/rasa/user-guide/installation/). This should install all necessary modules.
- You'll need the internet to fetch content from the APIs.

### Using the command line interface or Rasa X
If using the Rasa command line interface ( rasa shell ), or Rasa X, you'll need two terminals: one for the rasa action server and one for the rasa model server.

First, open a terminal for the action server. 
```
cd ../rasa-chatbot/rasa
rasa run actions
```
Then whip up a second terminal for either `rasa shell` or `rasa x` as follows:
- For the command line interface:
```
cd ../rasa-chatbot/rasa
rasa shell --endpoints endpoints.yml
```
- Or, for Rasa X:
```
cd ../rasa-chatbot/rasa
rasa x --endpoints endpoints.yml
```

For additional arguements, please see [rasa command line interface](https://rasa.com/docs/rasa/user-guide/command-line-interface/).


### Using the Webchat widget
First, run the action server as above. Then run the second terminal with:
```
cd ../rasa-chatbot/rasa
rasa run --endpoints endpoints.yml
```
Then open a third terminal for the flask app:
```
cd ../rasa-chatbot/flask-app
python app.py
```
Head on to http://localhost:5000 to view the webpage. Click on the button at the bottom-right corner. Enjoy :)
 
> Written with [StackEdit](https://stackedit.io/).
