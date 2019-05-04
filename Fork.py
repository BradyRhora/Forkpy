import discord
from discord.ext import commands
from xml.etree import ElementTree as ET
import Constants as CON
import Variables as VAR
import requests
import urllib.request
from bs4 import BeautifulSoup as BS
#  import logging

#  logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix=';', description='Forkbot\'s GF')


@bot.event
async def on_ready():
    print('Initialized {0}!'.format(bot.user.name))


@bot.event
async def on_message(message):
    if message.author.id == CON.FORKPY_ID:
        return
    if f'<@{CON.FORKPY_ID}>' in message.content or f'<@!{CON.FORKPY_ID}>' in message.content:
        msg = message.content.replace(f'<@{CON.FORKPY_ID}>', '').replace(f'<@!{CON.FORKPY_ID}>', '')

        link = f'https://www.botlibre.com/rest/api/form-chat?&application={CON.BOT_APP}&instance={CON.BOT_INST}&conversation={VAR.conversation}&message={msg}'
        response = requests.get(link)
        if response.text != "Profanity, offensive or sexual language is not permitted.":
            tree = ET.fromstring(response.text)
            VAR.conversation = tree.get('conversation')
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

@bot.command()
async def dnd(ctx, param):
    if param == 'party':
        urllib.urlopen(f'https://www.dndbeyond.com/campaigns/{CON.CAMPAIGN_ID}')
        pass


token = open('token', 'r')
bot.run(token.read().strip())
