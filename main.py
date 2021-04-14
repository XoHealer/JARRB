#Coded by https://github.com/XoHealer
import discord
import os
import time
import itertools
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
#version
version = "1.1"

# defines the bot as client for use of this code
client = commands.Bot(command_prefix='!R', help_command=None)
statuses = cycle([
    #List of statuses
    'You know the rules', 'and so do I.', '!Rhelp for help', 'Rick Rolling your parents', 'Never Gonna Give You Up'
])
#defines status change start and tells console bot has loaded correctly
@client.event
async def on_ready():
    change_status.start()
    print ("------------------------------------")
    print ("Bot Name: " + client.user.name)
    print ("Bot ID: " + str(client.user.id))
    print ("Discord Version: " + discord.__version__)
    print ("Bot Version " + version)
    print ("------------------------------------")

#tasks
@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(statuses)))

#error handler
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You are missing a person to rick roll!')
    else:
        pass

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Rick Doesn't understand this command yet!")
    else:
        pass

#heartbeat
@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! latency is {round(client.latency * 1000)}ms')
  print(f'pong! latency is {round(client.latency * 1000)}ms')

#manual rick roll
@client.command(aliases=['RR'])
async def rickroll(ctx, member : discord.Member):
    if member.id == 477589155468148736:
        await ctx.send(':no_entry_sign: You cannot out rick roll the JARRB Developer :no_entry_sign:')
    else:
        await ctx.send(f'https://www.youtube.com/watch?v=dQw4w9WgXcQ {member.mention}')

#help command
@client.command()
async def help(ctx):
    Help = discord.Embed(
        colour=discord.Colour.orange(),
        title="**Rick Bot**",
        description=f'\nHelp get rick rolled.\n'
    )
    Help.set_author(name="Rick Astley",
    icon_url="https://cdn.discordapp.com/avatars/831851789833863198/72d8f8b93562114a3f486cd828e5dfab.png?size=4096")
    Help.add_field(name=f'**Help**', value=f'*.help* \nShows the help window', inline=False)
    Help.add_field(name=f'**RickRoll**', value=f'*Rick Roll a mention / id', inline=False)
    Help.add_field(name=f'**Ping**', value=f'*.ping* \nTests latency', inline=False)
    Help.set_footer(text="Help - Rick Astley")

    await ctx.send(embed=Help)

#defines JARRB
@client.command(aliases = ['def'])
async def define(ctx):
    await ctx.send('Just Another Rick Roll Bot - https://www.youtube.com/watch?v=dQw4w9WgXcQ')

#keywords
keywords = ["nggyu", "never gonna give you up", "rick", "astley", "rick astley", "never gonna let you down"]

#on message check for keywords
@client.event
async def on_message(message):
    potrick = message.content.lower()
    for i in range(len(keywords)):
        isbot = message.author.bot
        if isbot:
            pass
        elif message.author.id == 477589155468148736:
            pass
        else:
            if keywords[i] in potrick:
                await message.channel.send(f'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                return
            else:
                pass
    #very important allowed for other commands to conintue to function 
    await client.process_commands(message)
    #client token required to tun the bot
    
client.run('TOKEN')
#Coded by https://github.com/XoHealer