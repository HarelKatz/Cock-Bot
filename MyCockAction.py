from Action import *


class MyCockAction(Action):
    def __init__(self):
        super().__init__("my cock")

    async def do_action(self, message, client, discord):
        return message.author.mention + " nice cock bro", True
