# bot.py
import os
import random
import asyncio

import discord
from dotenv import load_dotenv

from Actions import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MAIN_CHANNEL_NAME = os.getenv('MAIN_CHANNEL_NAME')
MAIN_CHANNEL_ID = int(os.getenv('MAIN_CHANNEL_ID'))


client = discord.Client()


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


@client.event
async def on_message(message):

    if message.author == client.user or message.guild == None:
        return

    guild = discord.utils.get(client.guilds, name=GUILD)
    main_channel = None
    for i in guild.channels:
        if i.name == MAIN_CHANNEL_NAME:
            main_channel = i
            break

    for action in all_actions:
        if action.should_respond(message):
            response = action.respond(message)
            await message.channel.send(response)
            send_message(message.channel.name, response)
            break
   
    """
    elif client.user.mentioned_in(message) and "gay" in message.content.lower():

        response = message.author.mention + " lol bye"
        await message.channel.send(response)
        send_message(message.channel.name, response)
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

    elif client.user.mentioned_in(message) and message.content == "<@!" + str(client.user.id) + ">":
        response = message.author.mention + " what"
        await message.channel.send(response)
        send_message(message.channel.name, response)

    elif client.user.mentioned_in(message) and (message.content.replace(" ", "").replace("<@!" + str(client.user.id) + ">", '') == "wow"):
        response = '''וווואווווווווו😱😱😱😱😱
אתם לא מאמינים זה אשכרה עובד!!! אם תגידו את המשפט שכתוב פה למטה שלוש פעמים ותשתפו לחמש קבוצות אתם לא תאמינו מה קורה!!!!!!!!!!!!!!!! האייקון של הדיסקורד יהפוך לאדום‼️‼️‼️‼️

אַשְהַדֻ אַן לַא אִלָהַ אִלַּא אללָּה וַאַן מֻחַמַּדַ(ן) רַסוּלֻ אללָּה.

כדאי לכם ממממשששש לנסות לי זה עבד וזה ממש מגניבב🤭🤭🤭'''
        await message.channel.send(response)
        send_message(message.channel.name, response)
        """


@client.event
async def on_member_join(member):

    if member == client.user:
        return

    response = member.mention + \
        " Nice to see you here, if you are a girl **GET OUT** if not nice, ding dong bro"

    main_channel = client.get_channel(MAIN_CHANNEL_ID)
    print(main_channel, main_channel.id)
    await main_channel.send(response)
    send_message(main_channel.name, response)


def send_message(channel_name, response):
    print("Sent message @ " + channel_name + ' that says "' + response + '"')


client.run(TOKEN)
