class ChatContext:
    def __init__(self):
        self.history = []

    def add(self, user_input, bot_response):
        self.history.append({"user": user_input, "bot": bot_response})

    def get_prompt(self):
        context = ""
        for turn in self.history[-5:]:
            context += f"User: {turn['user']}\nBot: {turn['bot']}\n"
        return context
