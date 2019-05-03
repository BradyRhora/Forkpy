import discord
from discord.ext import commands
from xml.etree import ElementTree as ET
import requests
#  import logging

#  logging.basicConfig(level=logging.INFO)

FORKPY_ID = 573047938306146304
chatbot_convo = 0

bot = commands.Bot(command_prefix=';', description='Forkbot\'s GF')


@bot.event
async def on_ready():
    print('Initialized {0}!'.format(bot.user.name))


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    if f'<@{FORKPY_ID}>' in message.content or f'<@!{FORKPY_ID}>' in message.content:
        msg = message.content.replace(f'<@{FORKPY_ID}>', '').replace(f'<@!{FORKPY_ID}>', '')
        global chatbot_convo
        link = f'https://www.botlibre.com/rest/api/form-chat?&application=7362540682895337949&instance=26768886&conversation={chatbot_convo}&message={msg}'
        response = requests.get(link)
        if response.text != "Profanity, offensive or sexual language is not permitted.":
            tree = ET.fromstring(response.text)
            chatbot_convo = tree.get('conversation')
            await message.channel.send(message.author.mention + ' ' + tree.find('message').text)
        else:
            await message.channel.send(message.author.mention + ' ' + "I don't want to talk about that.")
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command()
async def start(ctx):
    await ctx.send('<@377913570912108544> Hi')


token = open('token', 'r')
bot.run(token.read())