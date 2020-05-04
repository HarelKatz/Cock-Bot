class Action:
    def __init__(self, trigger):
        self._trigger = trigger

    def should_respond(self, message, client):
        return self._trigger in message.content.lower()

    def do_action(self, message, client):
        return message, True
