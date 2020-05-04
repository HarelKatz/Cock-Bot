from Action import *

BOTZER_REPEAT = 10

class BotzerAction(Action):
    def __init__(self):
        super().__init__("botzer")

    def respond(self, message):
        return message.author.mention + " BOTZER" * BOTZER_REPEAT