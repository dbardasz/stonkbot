import os
import discord
from discord.ext import commands
from data_function import get_data

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        tkr = message.content[1:5]
        data = get_data(tkr)
        await message.channel.send(data)


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
client.run("MTEyNDUyODY4MjMzNDE3NTMyMw.GDCPXg.WXuq0sK98Q3UgesILjRzZ0g2-m8b3POL4J72zM")
