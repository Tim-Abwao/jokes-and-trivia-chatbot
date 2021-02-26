from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from datetime import date


class ActionGetMathFact(Action):

    def name(self) -> Text:
        return "get_math_fact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        math_fact = requests.get('http://numbersapi.com/random/trivia')
        dispatcher.utter_message(math_fact.text)
        return []


class ActionGetDateFact(Action):

    def name(self) -> Text:
        return "get_date_fact"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # get current day and month
        day = date.strftime(date.today(), '%m/%d')

        day_fact = requests.get('http://numbersapi.com/' + day + '/date')
        dispatcher.utter_message(day_fact.text)
        return []


class ActionGetJoke(Action):

    def name(self) -> Text:
        return "get_joke"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        joke_content = requests.get(
            'https://official-joke-api.appspot.com/random_joke'
        ).json()
        joke = f"{joke_content['setup']}...   {joke_content['punchline']}"
        dispatcher.utter_message(joke)
        return []
