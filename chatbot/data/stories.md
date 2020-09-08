## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_ask_name

## sad path
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_ask_name

## introduction 1
* say_name{"PERSON": "William"}
  - utter_pitch_trivia
* affirm
  - utter_happy
  - utter_trivia_options

## introduction 2
* say_name{"PERSON": "Hellena"}
  - utter_pitch_trivia
* deny
  - utter_goodbye

## math facts
* math_facts
  - get_math_fact
  - get_math_fact
  - utter_ask_add_more

## day facts
* day_facts
  - get_date_fact
  - get_date_fact
  - utter_ask_add_more

## get jokes
* jokes
  - get_joke
  - get_joke
  - utter_ask_add_more

## say goodbye
* goodbye
  - utter_goodbye
