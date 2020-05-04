from Action import *


class WhatAction(Action):
    def __init__(self):
        super().__init__("")

    def should_respond(self, message, client):
        return client.user.mentioned_in(message) and message.content == "<@!" + str(client.user.id) + ">"

    def do_action(self, message, client):
        return message.author.mention + " what", True
