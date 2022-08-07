#!/usr/bin/env bash
MAIN_DIR=$(pwd)
CHATBOT_DIR="${MAIN_DIR}/trivia-chatbot"

train_model () {
    cd "$CHATBOT_DIR" && rasa train
    cd "$MAIN_DIR"
}

run_rasa_server () {
    cd "$CHATBOT_DIR"
    rasa run actions &  # Start Rasa action server in the background
    python -m webbrowser "../demo-webpage.html"  # Open demo page in browser
    rasa run --cors="*"  # Start the rasa server
}

# Activate virtual environment
if [ -d venv ]
    then
        source venv/bin/activate
    else
        echo -e "Creating a virtual environment and installing dependencies...\n"
        python3.9 -m venv venv  # Current latest supported version.
        source venv/bin/activate
        pip install -U pip
        pip install -r requirements.txt
fi

# Ensure a trained model is available
if [ ! -d "${CHATBOT_DIR}/models" ]; then
    train_model
fi

run_rasa_server
