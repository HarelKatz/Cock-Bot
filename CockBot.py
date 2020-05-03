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

    '''for member in guild.members:
        if member.name == 'Gilbert with no brim':
            while 1:
                try:
                    await member.create_dm()
                    await member.dm_channel.send("you are stupid")
                except:
                    pass'''

    for i in guild.channels:
        print(i.name, type(i.name))


@client.event
async def on_message(message):

    guild = discord.utils.get(client.guilds, name=GUILD)
    main_channel = None
    for i in guild.channels:
        if i.name == MAIN_CHANNEL_NAME:
            main_channel = i
            break

    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':

        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
        print("Sent message @ " + message.channel.name +
              ' that says "' + response + '"')

    if 'my cock' in message.content.lower():

        response = message.author.mention + " Nice cock bro"
        await message.channel.send(response)
        print("Sent message @ " + message.channel.name +
              ' that says "' + response + '"')

    if 'your dick' in message.content.lower():

        response = message.author.mention + " dick is small"
        await message.channel.send(response)
        print("Sent message @ " + message.channel.name +
              ' that says "' + response + '"')

        '''og_message = message.content
        await message.edit("My dick is very small")
        print("Edited " + message.author + " message from " +
              og_message + ' to "My dick is very small')'''

        response = message.author.mention + " Yes, your dick is small"
        await message.channel.send(response)
        print("Sent message @ " + message.channel.name +
              ' that says "' + response + '"')

    if client.user.mentioned_in(message) and "gay" in message.content.lower():

        response = message.author.mention + " lol bye"
        await message.channel.send(response)
        print("Sent message @ " + message.channel.name +
              ' that says "' + response + '"')
        await asyncio.sleep(5)
        try:
            await message.author.kick()
            print("kicking " + message.author.name + " for the lolz")
            await message.author.create_dm()
            await message.author.dm_channel.send("you are stupid")
            await message.author.dm_channel.send("you should be sent a new link to the server, if not just search for another link or ask some one to dend you a link")
            link = await main_channel.create_invite(max_age=300, max_uses=1, reason="kicked him for the lolz")
            await message.author.dm_channel.send("Here is a 1 time use invite link: " + link.url)

        except:
            pass

client.run(TOKEN)
