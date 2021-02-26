#!/usr/bin/env bash

# Activate the Python virtual environment
if [ -d venv ]
    then
        source venv/bin/activate
fi

cd trivia-chatbot

# Train the chatbot if no model is present
if [ ! -d models ]
    then rasa train
fi

# Start the action server & Rasa X
rasa run actions &
rasa x
