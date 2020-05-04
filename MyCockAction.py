from Action import *


class MyCockAction(Action):
    def __init__(self):
        super().__init__("my cock")

    def do_action(self, message, client):
        return message.author.mention + " nice cock bro", True
