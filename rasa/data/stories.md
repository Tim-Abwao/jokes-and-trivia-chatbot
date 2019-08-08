## happy path 1
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_ask_name
* say_name
  - action_get_name
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
* say_name
  - action_get_name
  - utter_game
* deny
  - utter_goodbye

## sad path game
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_ask_name
* say_name
  - action_get_name
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
* say_name
  - action_get_name
  - utter_game
* deny
  - utter_goodbye

## math facts
* get_math_facts
  - action_get_math_fact
  - action_get_math_fact
  - utter_more
* continue
  - action_get_math_fact
  - action_get_math_fact
  - utter_more

## day facts
* get_day_facts
  - action_get_date_fact
  - action_get_date_fact
  - utter_more
* continue
  - action_get_date_fact
  - action_get_date_fact
  - utter_more

## get jokes
* get_jokes
  - action_get_joke
  - action_get_joke
  - utter_more
* continue
  - action_get_joke
  - action_get_joke
  - utter_more

## switch
* switch
  - utter_how_to_stop
  - utter_game_types


## say goodbye
* goodbye
  - utter_goodbye
