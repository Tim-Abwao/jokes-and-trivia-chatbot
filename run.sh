#!/usr/bin/env bash

# Activate the virtual environment, if present
if [ -d venv ]
    then
        source venv/bin/activate
fi

cd trivia-chatbot

# Train the chatbot if no model is present
if [ ! -d models ]
    then rasa train
fi

# Start the action server in the background
rasa run actions &

# Open the demo web-page in a browser
python -m webbrowser "../demo-webpage.html"

# Start the rasa server
rasa run --cors="*"

# Return to chatbot home "jokes-and-trivia-chatbot"
cd ..
