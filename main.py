## CONFIG
import json
import os
print("Loading user config.")
if os.path.exists("config.json") == False:
    print("No config file found, ending.")
    import sys
    sys.exit(0)
with open("config.json") as json_file:
    data = json.load(json_file)
    you = data["username"]
    prefix = data["prefix"]
    token = data["token"]
    status = data["status"]
    guild_id = data["guild"]
    print(f"Username: {you}\nBot prefix: {prefix}\nBot token: {token}\nGuild ID: {guild_id}")
    json_file.close()

# pip install discord asyncio aiohttp psutil discord-py-slash-command

print('Importing modules.')
print('Importing Discord 0/100%')
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
print('Importing Discord 1000/100%')
print('Importing random 0/100%')
import random
print('Importing random 100/100%')
print('Importing extras 0/100%')
import asyncio
import aiohttp
import psutil
print('Importing extras 100/100%')
print(f'Setting prefix to {prefix}, making "client" definition, making slash definition. 0/100%')
client = commands.Bot(command_prefix=str(prefix))#, intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
print(f'Setting prefix to {prefix}, making "client" definition, making slash definition. 100/100%')

def mathop(num1, operation, num2):
    if operation == "mult":
        return(int(num1)*int(num2))
    if operation == "div":
        return(int(num1)/int(num2))
    if operation == "rest":
        return(int(num1)-int(num2))
    if operation == "add":
        return(int(num1)+int(num2))
        
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
    print('Launching BOT 100/100%')
@client.event
async def on_command_error(ctx, error):
    embedVar = discord.Embed(title="Failure", description="", color=0x5865F2)
    embedVar.add_field(name=f"Failed to execute action", value=f"Error: `{error}`")
    await ctx.reply(embed=embedVar, mention_author=True)

## SLASH - TEST
@slash.slash(
    name="stats",
    description=f"Information about {you}'s computer.",
    guild_ids=[int(guild_id)]
)
async def _test(ctx:SlashContext):
    embedVar = discord.Embed(title="PC stats", description=f"Information about {you}'s PC.", color=0x5865F2)

    cpu = psutil.cpu_percent()

    memory_using = psutil.virtual_memory().percent

    embedVar.add_field(name="CPU Usage", value=f"{cpu}%", inline=False)
    embedVar.add_field(name="Memory usage", value=f"{memory_using}%", inline=False)
    embedVar.add_field(name="Internet Latency", value=f"{client.latency*1000}ms", inline=False)
    #embedVar.add_field(name="Servers", value=f"{str(len(client.guilds))} servers", inline=False)
    await ctx.send(embed=embedVar)

@client.command()
async def stats(ctx):
    """Information about your computer"""
    embedVar = discord.Embed(title="PC stats", description=f"Information about {you}'s PC.", color=0x5865F2)

    cpu = psutil.cpu_percent()

    memory_using = psutil.virtual_memory().percent

    embedVar.add_field(name="CPU Usage", value=f"{cpu}%", inline=False)
    embedVar.add_field(name="Memory usage", value=f"{memory_using}%", inline=False)
    embedVar.add_field(name="Internet Latency", value=f"{client.latency*1000}ms", inline=False)
    #embedVar.add_field(name="Servers", value=f"{str(len(client.guilds))} servers", inline=False)
    await ctx.reply(embed=embedVar, mention_author=True)

print('Launching BOT 0/100%')
client.run(token)
