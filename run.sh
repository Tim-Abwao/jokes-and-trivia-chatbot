#!/usr/bin/env bash

# activate Python virtual environment
source venv/bin/activate

# Flask web app
export FLASK_APP=flask-web-app/app
export FLASK_ENV=development
flask run &
flask_server_pid=$!

# Action server & Rasa server
cd chatbot
rasa run actions &
rasa run --cors "*"

# stop flask web app
kill $flask_server_pid;
