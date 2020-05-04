from Action import *


class SmallDickAction(Action):
    def __init__(self):
        super().__init__("")
        self.triggers = ["your", "dick", "small"]

    def should_respond(self, message, client):
        return all(word in message.content.lower() for word in self.triggers)

    async def do_action(self, message, client):
        return message.author.mention + " dick's is small", True
