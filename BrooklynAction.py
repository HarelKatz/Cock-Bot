from Action import *
import random

BROOKLYN_99_QUOTES = [
    'I\'m the human form of the 💯 emoji.',
    'Bingpot!',
    (
        'Cool. Cool cool cool cool cool cool cool, '
        'no doubt no doubt no doubt no doubt.'
    ),
]


class BrooklynAction(Action):
    def __init__(self):
        super().__init__("99!")

    def should_respond(self, message, client):
        return self._trigger == message.content.lower()

    def do_action(self, message, client):
        return random.choice(BROOKLYN_99_QUOTES), True
