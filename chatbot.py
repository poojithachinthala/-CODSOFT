import re
import random

class RuleBot:
    def __init__(self):
        self.rules = {
            r"(hi|hello|hey|hai)": "Hello! How can I assist you today?",
            r"how are you": "I'm doing great, thanks for asking!",
            r"(your name|who are you)": "I'm RuleBot, your friendly chatbot.",
            r"(what can you do|help)": "I can chat with you and answer simple questions!",
            r"(who made you|your creator)": "I was created by a Python developer like you!",
            r"(what are you doing)": "I'm just chatting with you right now!",
            r"(are you free|are you busy)": "I'm always available for you!",
            r"(tell me a joke|make me laugh)": "Why do Java developers wear glasses? Because they don’t C#! 😂",
            r"(bye|exit|quit)": "Goodbye! It was nice talking to you 😊"
        }

        self.default_responses = [
            "Hmm... I didn’t get that. Try asking something else?",
            "Can you ask that in another way?",
            "I'm still learning. Can you say it differently?",
            "That's interesting! Tell me more."
        ]

    def get_response(self, user_input):
        for pattern, response in self.rules.items():
            if re.search(pattern, user_input):
                return response
        return random.choice(self.default_responses)

    def start_chat(self):
        print("Hello! I'm RuleBot. Type 'bye' to exit.\n")

        while True:
            user_input = input("You: ").lower().strip()
            response = self.get_response(user_input)
            print("Bot:", response)

            if re.search(r"(bye|exit|quit)", user_input):
                break
if __name__ == "__main__":
    bot = RuleBot()
    bot.start_chat()



