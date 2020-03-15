# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from urllib.request import urlopen
from datetime import date
from ast import literal_eval


# extra words usually said along with names 
name_extras=['my','name','is',"i'm",'i','am','called','nameis',"name's",'names','im','they','call','me']

class ActionGetName(Action):
    def name(self) -> Text:
        return "action_get_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          # get latest message in lower case text
        text=tracker.latest_message['text'].lower()
          # turn text into a list of words and remove extra text to get unique name
        text=text.split()
        for word in name_extras:
            if word in text:
                text.remove(word)

        full_name =' '.join([a.title() for a in text]) # combine names
        first_name=full_name.split()[0] # get first word in full_name
          # save first name and full name to slots
        return [SlotSet("name", full_name), SlotSet("fname", first_name)]


class ActionGetMathFact(Action):

    def name(self) -> Text:
        return "action_get_math_fact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          # get message from numbersapi
        fact=urlopen('http://numbersapi.com/random/trivia').read().decode('utf-8')
          # send fact as message
        dispatcher.utter_message(fact)
        return []

class ActionGetDateFact(Action):

    def name(self) -> Text:
        return "action_get_date_fact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          # get day and month
        todays_date=date.today()
        month=todays_date.month
        day=todays_date.day
          # get message from numbersapi
        day_fact=urlopen('http://numbersapi.com/'+str(month)+'/'+str(day)+'/date').read().decode('utf-8')
          # send fact as message
        dispatcher.utter_message(day_fact)
        return []

class ActionGetJoke(Action):

    def name(self) -> Text:
        return "action_get_joke"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          # get joke from the jokes api
        joke=urlopen('https://official-joke-api.appspot.com/random_joke').read().decode('utf-8')
          #convert 'string dict' to dict using ast
        joke=literal_eval(joke)
        joke_setup=joke['setup']
        joke_punchline=joke['punchline']
        joke_text=joke_setup+' ..... '+joke_punchline
          # send joke as message
        dispatcher.utter_message(joke_text)
        return []
