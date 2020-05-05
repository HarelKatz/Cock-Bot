class Action:
    def __init__(self, trigger):
        self._trigger = trigger.lower()

    def should_respond(self, message, client):
        return self._trigger == message.content.lower()

    async def do_action(self, message, client, discord):
        return message, True
