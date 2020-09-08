#!/bin/bash
source venv/bin/activate

# run flask server as background process
export FLASK_APP=flask-web-app/app
export FLASK_ENV=development
flask run &
web_server_pid=$!

# run rasa action server as background process
cd chatbot
rasa run actions &
action_server_pid=$!

# run rasa server
rasa run --cors "*"

# stop background processes on exit
kill $web_server_pid $action_server_pid;
