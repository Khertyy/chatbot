from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted

class ActionRestartChatbot(Action):
    def name(self) -> str:
        return "action_restart_chatbot"

    async def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
        return [Restarted()]
