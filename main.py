#Imports the discord.py module itself, as well as importing possible commands from discord.ext.
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
#Let the bot operator know when the bot is online and ready to be used
@client.event
async def on_ready():
    print("The bot is ready to be used!")

#Hello command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello! My bot prefix is a period/dot!')

#Greet new members!
@client.event
async def on_join(member):
    channel = client.get_channel(809235994636976158)
    await channel.send("Hi! Welcome to our server!")

#Say goodbye to members when they leave
async def on_remove(member):
    channel = client.get_channel(809238210617933915)
    await channel.send("Goodbye! I hope you enjoyed your time in our server!")


#Define the bot token variable
TOKEN = 'ODA1NTcwOTM0MjA3MjgzMjEx.YBc0ZQ.ZNuuEBW2t0kUS9Ny9-SZLgr7abg'







client.run(TOKEN)
keep_alive.keep_alive()