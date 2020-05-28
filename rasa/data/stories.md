## happy path 1
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_ask_name
* say_name{"PERSON": "William"}
  - utter_game
* affirm
  - utter_happy
  - utter_game_types

## happy path 2
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_ask_name
* say_name{"PERSON": "Hellena"}
  - utter_game
* deny
  - utter_goodbye

## sad path game
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_ask_name
* say_name{"PERSON": "Dawson"}
  - utter_game
* affirm
  - utter_happy
  - utter_game_types

## sad path no game
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_ask_name
* say_name{"PERSON": "Holmes"}
  - utter_game
* deny
  - utter_goodbye

## math facts
* math_facts
  - get_math_fact
  - get_math_fact
  - utter_more
* continue
  - get_math_fact
  - get_math_fact
  - utter_more

## day facts
* day_facts
  - get_date_fact
  - get_date_fact
  - utter_more
* continue
  - get_date_fact
  - get_date_fact
  - utter_more

## get jokes
* jokes
  - get_joke
  - get_joke
  - utter_more
* continue
  - get_joke
  - get_joke
  - utter_more

## switch
* switch
  - utter_how_to_stop
  - utter_game_types

## say goodbye
* goodbye
  - utter_goodbye
