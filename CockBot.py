# bot.py
import os
import random
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MAIN_CHANNEL_NAME = os.getenv('MAIN_CHANNEL_NAME')


client = discord.Client()


@client.event
async def on_ready():

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    guild = discord.utils.get(client.guilds, name=GUILD)
    main_channel = None
    for i in guild.channels:
        if i.name == MAIN_CHANNEL_NAME:
            main_channel = i
            break

    if message.content == '99!':

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
        sent_message(message.channel.name, response)

    if 'my cock' in message.content.lower():

        response = message.author.mention + " Nice cock bro"
        await message.channel.send(response)
        sent_message(message.channel.name, response)

    if all(word in message.content.lower() for word in ["your", "dick", "small"]):

        response = message.author.mention + " dick is small"
        await message.channel.send(response)
        sent_message(message.channel.name, response)

        response = message.author.mention + " Yes, your dick is small"
        await message.channel.send(response)
        sent_message(message.channel.name, response)

    if client.user.mentioned_in(message) and "gay" in message.content.lower():

        response = message.author.mention + " lol bye"
        await message.channel.send(response)
        sent_message(message.channel.name, response)
        await asyncio.sleep(5)

        try:

            await message.author.create_dm()
            await message.author.dm_channel.send("you are stupid")
            await message.author.dm_channel.send("you should be sent a new link to the server, if not just search for another link or ask some one to dend you a link")
            link = await main_channel.create_invite(max_age=300, max_uses=1, reason="kicked him for the lolz")
            await message.author.dm_channel.send("Here is a 1 time use invite link: " + link.url)
            await message.author.kick()
            print("kicking " + message.author.name + " for the lolz")

        except:
            pass


def sent_message(channel_name, response):
    print("Sent message @ " + channel_name + ' that says "' + response + '"')


client.run(TOKEN)
