class Action:
    def __init__(self, trigger):
        self._trigger = trigger.lower()

    def should_respond(self, message):
        return self._trigger in message.content.lower()

    @property
    def trigger(self):
        return self._trigger

    def respond(self, message):
        return message