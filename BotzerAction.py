from Action import *

BOTZER_REPEAT = 10


class BotzerAction(Action):
    def __init__(self):
        super().__init__("botzer")

    async def do_action(self, message, client, discord):
        return message.author.mention + " BOTZER" * BOTZER_REPEAT, True
