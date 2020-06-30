import os
import random
import asyncio
import datetime

import discord  # pip install discord
from dotenv import load_dotenv  # pip install python-dotenv

from Actions import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MAIN_CHANNEL_NAME = os.getenv('MAIN_CHANNEL_NAME')
MAIN_CHANNEL_ID = int(os.getenv('MAIN_CHANNEL_ID'))


client = discord.Client()

# when the bot is started
@client.event
async def on_ready():

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    for channel in guild.channels:
        print(channel, channel.id)

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# when someone send a message in chat
@client.event
async def on_message(message):

    # if the message is the bot's message or he recives a message in the DMs
    if message.author == client.user or message.guild == None:
        return

    guild = discord.utils.get(client.guilds, name=GUILD)
    main_channel = None
    for i in guild.channels:
        if i.name == MAIN_CHANNEL_NAME:
            main_channel = i
            break

    for action in all_actions:
        if action.should_respond(message, client):
            response, do = await action.do_action(message, client, discord)
            if do:
                await message.channel.send(response)
                sent_message(message.channel.name, response)
            break

# when someone joins a server
@client.event
async def on_member_join(member):

    if member == client.user:
        return

    response = member.mention + \
        " Nice to see you here, if you are a girl **GET OUT** if not nice, ding dong bro"

    main_channel = client.get_channel(MAIN_CHANNEL_ID)
    print(main_channel, main_channel.id)
    await main_channel.send(response)
    sent_message(main_channel.name, response)


def sent_message(channel_name, response):
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ": Sent message @ " + channel_name + ' that says "' + response + '"')


client.run(TOKEN)
