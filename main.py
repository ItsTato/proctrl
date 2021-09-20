## CONFIG
import json
import os
print("Loading user config.")
if os.path.exists("config.json") == False:
    print("No config file found, ending.")
    import sys
    sys.exit(0)
if os.path.exists("rpc.json") == False:
    print("RPC Config couldn't be found, ending.")
    import sys
    sys.exit(0)
with open("config.json") as json_file:
    data = json.load(json_file)
    you = data["username"]
    prefix = data["prefix"]
    token = data["token"]
    status = data["status"]
    guild_id = data["guild"]
    client_id = data["client_id"]
    json_file.close()
with open("rpc.json") as json_file:
    data = json.load(json_file)
    details = data["details"]
    state = data["state"]
    large_image = data["large_image"]
    small_image = data["small_image"]
    large_text = data["large_text"]
    small_text = data["small_text"]
    button_text = data["button_text"]
    button_link = data["button_link"]

# pip install discord asyncio aiohttp psutil discord-py-slash-command

print('Importing modules.')
print('Importing Discord 0/100%')
from pypresence import Presence
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
print('Importing Discord 1000/100%')
print('Importing extras 0/100%')
import asyncio
import random
import time
import aiohttp
import psutil
print('Importing extras 100/100%')
print(f'Setting prefix to {prefix}, making "client" definition, making slash definition. 0/100%')
client = commands.Bot(command_prefix=str(prefix))#, intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
print(f'Setting prefix to {prefix}, making "client" definition, making slash definition. 100/100%')

RPC = Presence(client_id)
RPC.connect()
RPC.update(details=details, state=state, large_image=large_image, small_image=small_image, large_text=large_text, small_text=small_text, buttons=[{"label": button_text, "url": button_link}])
        
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
    print('Launching BOT 100/100%')
@client.event
async def on_command_error(ctx, error):
    embedVar = discord.Embed(title="Failure", description="", color=0x5865F2)
    embedVar.add_field(name=f"Failed to execute action", value=f"Error: `{error}`")
    await ctx.reply(embed=embedVar, mention_author=True)

## SLASH - STATS
@slash.slash(
    name="stats",
    description=f"Information about {you}'s computer.",
    guild_ids=[int(guild_id)]
)
async def _test(ctx:SlashContext):
    cpu = psutil.cpu_percent()

    memory_using = psutil.virtual_memory().percent

    await ctx.send(f"```CPU USAGE: {cpu}%\nMEMORY USAGE: {memory_using}%\nINTERNET LATENCY: {client.latency*1000}ms```")

## SLASH - RPC
@slash.slash(
    name="edit-rpc",
    description="Edit your Discord RPC.",
    options=[
        create_option(
            name="details",
            description="RPC: Details",
            required=True,
            option_type=3
            )
        ],
    guild_ids=[int(guild_id)]
)
async def _editrpc(ctx:SlashContext, details:str):
    await ctx.send("d")


print('Launching BOT 0/100%')
client.run(token)
