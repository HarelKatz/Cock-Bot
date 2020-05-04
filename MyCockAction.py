from Action import *

class MyCockAction(Action):
    def __init__(self):
        super().__init__("my cock")

    def respond(self, message):
        return message.author.mention + " nice cock bro"
        