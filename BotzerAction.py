from Action import *

BOTZER_REPEAT = 10


class BotzerAction(Action):
    def __init__(self):
        super().__init__("botzer")

    def respond(self, message, client):
        return message.author.mention + " BOTZER" * BOTZER_REPEAT, True
