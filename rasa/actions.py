from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from urllib.request import urlopen
from datetime import date
from ast import literal_eval


class ActionGetMathFact(Action):

    def name(self) -> Text:
        return "get_math_fact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # get message from numbersapi
        fact = urlopen('http://numbersapi.com/random/trivia').read()
        # send fact as message
        dispatcher.utter_message(fact.decode('utf-8'))
        return []


class ActionGetDateFact(Action):

    def name(self) -> Text:
        return "get_date_fact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # get day and month
        day = date.strftime(date.today(), '%m/%d')
        # get message from numbersapi
        day_fact = urlopen('http://numbersapi.com/' + day + '/date').read()
        # send fact as message
        dispatcher.utter_message(day_fact.decode('utf-8'))
        return []


class ActionGetJoke(Action):

    def name(self) -> Text:
        return "get_joke"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # get joke from the jokes api
        joke = urlopen('https://official-joke-api.appspot.com/random_joke')
        # convert 'string dict' to dict using ast
        joke = literal_eval(joke.read().decode('utf-8'))
        joke = ' ..... '.join([joke['setup'], joke['punchline']])
        dispatcher.utter_message(joke)
        return []
