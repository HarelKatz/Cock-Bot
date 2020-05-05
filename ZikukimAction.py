from Action import *
import asyncio


class ZikukimAction(Action):
    def __init__(self):
        super().__init__("זיקוקים")

    async def do_action(self, message, client, discord):

        voice = await message.author.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio(
            '.\\Misc\\Moshe Perez - Zikukim.mp3'))
        print("Started playing Zikukim @ " + message.author.voice.channel.name)
        counter = 0
        duration = 21   # In seconds
        while not counter >= duration:
            await asyncio.sleep(1)
            counter = counter + 1
        await voice.disconnect()
        return "", False
