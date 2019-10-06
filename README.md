# Rasa Chatbot with Custom Actions for  Number Facts, Date Facts & Jokes.

A simple chatbot that's fun to talk to. Powered by [Rasa](https://rasa.com). 

Number and history facts courtesy of [Numbers API](http://numbersapi.com).
Jokes courtesy of the [Official Jokes API](https://official-joke-api.appspot.com/random_joke).
Webchat widget courtesy of [Mr. Bot AI](https://github.com/mrbot-ai/rasa-webchat).

The **rasa** directory has the files needed to modify, re-train and run the chatbot. Please check out the [rasa docs](https://rasa.com/docs/), if you haven't yet.

The **flask-sample-page** directory has a flask app you can use to host the webchat widget. See [Messaging & Voice Channels](https://rasa.com/docs/rasa/user-guide/messaging-and-voice-channels/) for a list of interesting ways to deploy the chatbot.

## Prerequisites
- Basic knowledge of [Python](https://www.python.org/), particularly `pip` and `venv`.
- Familiarity with Rasa. Please see the [installation guide](https://rasa.com/docs/rasa/user-guide/installation/) for OS specific help to install it in a virtual environment.
- Familiarity with [Flask](https://palletsprojects.com/p/flask/) (optional)
- Internet connection - to fetch content from the joke/fact APIs.

### (a). Using Rasa Shell or Rasa X
1. Open a terminal/command line at the parent directory (i.e. **rasa-chatbot**), then run: 
```
#in case the virtual environment is not active
source venv/bin/activate
```
```
cd rasa
rasa run actions
```
2. Open another terminal at the parent directory, and activate the virtual environment.
```
source venv/bin/activate
```
* For the command line interface:
```
cd rasa
rasa shell 
```
* Or instead, for Rasa X:
```
cd rasa
rasa x
```

For additional arguements, please see [rasa command line interface](https://rasa.com/docs/rasa/user-guide/command-line-interface/).


### (b) Using the Webchat widget
1. Run the action server as in (a) 1 above. 
2. Open a second terminal at the parent directory, and run:
```
source venv/bin/activate
cd rasa
rasa run
```
3. Similarly, open a third terminal at the parent directory for the flask sample web-page:
```
source venv/bin/activate
cd flask-sample-page
python3 app.py
```
4. Head on to http://localhost:5000 to view the web-page. Click on the button at the bottom-right corner. 

That's all. Enjoy :simple_smile:
