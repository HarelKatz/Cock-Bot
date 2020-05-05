from Action import *
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
MAIN_CHANNEL_ID = int(os.getenv('MAIN_CHANNEL_ID'))


class GayKickAction(Action):
    def __init__(self):
        super().__init__("")

    def __sent_message(self, channel_name, response):
        print("Sent message @ " + channel_name +
              ' that says "' + response + '"')

    def should_respond(self, message, client):
        return client.user.mentioned_in(message) and "gay" in message.content.lower()

    async def do_action(self, message, client, discord):

        response = message.author.mention + " lol bye"
        await message.channel.send(response)
        self.__sent_message(message.channel.name, response)
        await asyncio.sleep(5)

        # try:

        main_channel = client.get_channel(MAIN_CHANNEL_ID)
        await message.author.create_dm()
        await message.author.dm_channel.send("you are stupid")
        await message.author.dm_channel.send("you should be sent a new link to the server, if not just search for another link or ask some one to dend you a link")
        link = await main_channel.create_invite(max_age=300, max_uses=1, reason="kicked him for the lolz")
        await message.author.dm_channel.send("Here is a 1 time use invite link: " + link.url)
        await message.author.kick()
        print("kicking " + message.author.name + " for the lolz")

        # except:
        # pass

        return message.content, False
