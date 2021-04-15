#Coded by https://github.com/XoHealer
#Imports and Intents ------------------------------------------------------------
import discord
import os
import time
import itertools
import json
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
#--------------------------------------------------------------------------------

#Version
version = "1.2"

#Imports Json file containing keywords that trigger a rickroll
with open("rollwords.json", "r") as f:
    keylist = json.load(f)

#Defines the bot as client, removes the default help command and defines intents
client = commands.Bot(command_prefix='!R', help_command=None, intents=intents)

#List of Statuses to be cycled
statuses = cycle([

    'You know the rules', 'and so do I.', '!Rhelp for help', 'Rick Rolling your parents', 'Never Gonna Give You Up'
])

#Task that cycles Statuses
@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(statuses)))

#defines status change start and tells console bot has loaded correctly and prints the bot info
@client.event
async def on_ready():
    change_status.start()
    print ("------------------------------------")
    print ("Bot Name: " + client.user.name)
    print ("Bot ID: " + str(client.user.id))
    print ("Discord Version: " + discord.__version__)
    print ("Author: XoHealer")
    print ("Bot Version " + version)
    print ("------------------------------------")

#Sends joining members a Rick Roll
@client.event
async def on_member_join(member):
    print(f'{member} has Joined the server and has been rickrolled succesfully.')
    await member.send(f'Hi {member.mention} https://www.youtube.com/watch?v=dQw4w9WgXcQ')

#error handler and completion --------------------------------------------------------------------
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

@client.event
async def on_command_completion(ctx):
    print("Command: " + ctx.command.name + " was invoked Succesfully")

#-------------------------------------------------------------------------------------------------

#Commands-----------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------------------


#Main Rick Roll Events, Waits for a message then checks its content for the keywords list
@client.event
async def on_message(message):
    #identifies message as lower (makes it all lowercase and assigns it variable potential rick roll.)
    msg = message.content.lower() 
    for item in keylist:
        isbot = message.author.bot
        if isbot:
            pass
        elif message.author.id == 477589155468148736:
            pass
        else:
            if item in msg:
                
                await message.channel.send(f'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                print(f'{message.author} was Rick Rolled Succesfully')
                return
            else:
                pass
        #very important allowed for other commands to conintue to function 
    await client.process_commands(message)
        
#Application - Bots Client Token
   
client.run('TOKEN')
#Coded by https://github.com/XoHealer
