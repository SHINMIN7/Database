# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []
      
from typing import Text, Dict, Any, List
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionAcknowledgeLanePreference(Action):
    def name(self) -> Text:
        return "action_acknowledge_lane_preference"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the value of 'lane' slot from the tracker
        lane = tracker.get_slot('lane')

        # Acknowledge the user's lane preference
        dispatcher.utter_message(text=f"Great choice! I see you want to play in the {lane} lane.")
        
        # Return an event to set the 'lane_acknowledged' slot to 'true'
        return [SlotSet("lane_acknowledged", "true")]

class ActionAcknowledgeRolePreference(Action):
    def name(self) -> Text:
        return "action_acknowledge_role_preference"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the value of 'role' slot from the tracker
        role = tracker.get_slot('role')

        # Acknowledge the user's role preference
        dispatcher.utter_message(text=f"Got it! You prefer the {role} role.")

        # Return an event to set the 'role_acknowledged' slot to 'true'
        return [SlotSet("role_acknowledged", "true")]      
      
