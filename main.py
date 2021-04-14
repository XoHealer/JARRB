import discord
import os
import time
import itertools
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
# defines the bot as client for use of this code
client = commands.Bot(command_prefix='R', help_command=None)
statuses = cycle([
    #List of statuses
    'You know the rules', 'and so do I.', 'Rhelp for help', 'Rick Rolling your parents', 'Never Gonna Give You Up'
])
#defines status change start and tells console bot has loaded correctly
@client.event
async def on_ready():
    change_status.start()
    print('Bot has loaded and is online')

#tasks
@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(statuses)))

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! latency is {round(client.latency * 1000)}ms')
  print(f'pong! latency is {round(client.latency * 1000)}ms')

@client.command()
async def help(ctx):
    Help = discord.Embed(
        colour=discord.Colour.orange(),
        title="**Rick Bot**",
        description=f'\nHelp get rick rolled.\n'
    )
    Help.set_author(name="Rick Astley",
    icon_url="https://cdn.pixabay.com/photo/2017/08/31/04/01/d20-2699387_640.png")
    Help.add_field(name=f'**Help**', value=f'*.help* \nShows the help window', inline=False)
    Help.add_field(name=f'**RickRoll**', value=f'*Rick Roll a mention / id', inline=False)
    Help.add_field(name=f'**Ping**', value=f'*.ping* \nTests latency', inline=False)
    Help.set_footer(text="Help - Rick Astley")

    await ctx.send(embed=Help)
#keywords
keywords = ["nggyu"]
#on message check for keywords
@client.event
async def on_message(message):
    
    for i in range(len(keywords)):
        isbot = message.author.bot
        if isbot:
            pass
        else:
            if keywords[i] in message.content:
                await message.channel.send(f'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            else:
                pass
    await client.process_commands(message)
client.run('ODMxODUxNzg5ODMzODYzMTk4.YHbQWQ.zH4PxVcu_ilx2u1g77XooChjTx4')