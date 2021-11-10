# MIT License
# 
# Copyright (c) 2021 ItsTato
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
    client_id = data["client_id"]
    PanelPort = data["dashport"]
    json_file.close()

print('Importing modules 0/100%')
from pypresence import Presence
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option, update_single_command_permissions
import psutil
import sys
import threading
import time
import socket
from flask import *
print('Importing modules 100/100%')
print(f'Setting prefix to {prefix}, making "client" definition, making "slash" definition, making "socketio" definition, making "app" definition. 0/100%')
client = commands.Bot(command_prefix=str(prefix))#, intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
RPC = Presence(client_id)
app = Flask(__name__)
app.config["SECRET_KEY"] = "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"
print(f'Setting prefix to {prefix}, making "client" definition, making "slash" definition, making "socketio" definition, making "app" definition. 100/100%')

built_using = "Built Using Modules (Marked with * are from Pypi): pypresence*, discord*, discord-py-slash-command*, psutil*, flask*, flask-socketio*, threading, json, os, sys, socket"

def restart():
    os.system("shutdown /r /t  1")

def shutdown():
    os.system("shutdown /s /t  1")

# Web Panel
@app.route('/panel', methods=['GET'])
def panelSite():
    return render_template(f"panel.html",sysName=you,shutDownSite="/panel/control_actions/shutdown",reStartSite="/panel/control_actions/restart",cpu_usage=psutil.cpu_percent(),mem_usage=psutil.virtual_memory().percent,mem_total_mb=round(round(psutil.virtual_memory().total/1024)/1024),active_python_threads=threading.active_count(),latency=round(client.latency*1000),built=built_using)

@app.route('/panel', methods=['POST'])
def panelSite_post():
    try:
        if(not request.form["commandVal"]==None):
            os.system(str(request.form["commandVal"]))
            return redirect('/panel')
    except:
        if(not request.form["evalpythonVal"]==None):
            try:
                exec(str(request.form["evalpythonVal"]))
            except:
                print("Oopsie UwU")
            return redirect('/panel')

@app.route('/panel/control_actions/shutdown')
def shutdownSite():
    shutdown()
    return redirect('/panel',302)

@app.route('/panel/control_actions/restart')
def restartSite():
    restart()
    return redirect('/panel',302)

def flaskThread():
    global panelStatus
    panelStatus = True
    app.run(host="0.0.0.0",port=PanelPort,debug=False)

# Discord Bot
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
    print('Launching BOT 100/100%')

@client.event
async def on_command_error(ctx, error):
    embedVar = discord.Embed(title="Failure", description="", color=0x2F3136)
    embedVar.add_field(name=f"Failed to execute action", value=f"Error: `{error}`")
    await ctx.reply(embed=embedVar, mention_author=True)

## SLASH - STATS
@slash.slash(
    name="stats",
    description=f"Information about {you}'s computer.",
    guild_ids=[int(guild_id)]
)
async def _stats(ctx:SlashContext):
    cpu = psutil.cpu_percent()

    memory_using = psutil.virtual_memory().percent

    embedVar = discord.Embed(title="ProCTRL", description=" ", color=0x2F3136)
    embedVar.add_field(name=f"System", value=f"```CPU Usage: {psutil.cpu_percent()}%\nMemory Usage: {psutil.virtual_memory().percent}% (Of {round(round(round(psutil.virtual_memory().total/1024)/1024)/1024)}GB)```",inline=True)
    embedVar.add_field(name=f"Python", value=f"```Active Python Threads: {threading.active_count()}\n{built_using}```",inline=True)
    embedVar.add_field(name=f"Discord Bot", value=f"```Internet -> Discord API latency: {round(client.latency*1000)}ms```",inline=True)
    embedVar.add_field(name=f"Web Panel", value=f"```Panel Online: {panelStatus}\nLocal IP Address: {str(socket.gethostbyname(str(socket.gethostname())))}\nPort: {str(PanelPort)}```",inline=True)
    await ctx.send(embed=embedVar)

@client.command(aliases=['runBash'])
async def bash(ctx,*,cmd):
    await ctx.send(content=os.system(cmd))

@client.command()
async def eval(ctx,*,cmd):
    exec(cmd)
    await ctx.send(content=f"Ran code: ```{cmd}```")

@client.command(aliases=["information","botinfo","botinformation", "sysinfo", "systeminfo", "systeminformation", "sysinformation"])
async def info(ctx):
    embedVar = discord.Embed(title="ProCTRL", description=" ", color=0x2F3136)
    embedVar.add_field(name=f"System", value=f"```CPU Usage: {psutil.cpu_percent()}%\nMemory Usage: {psutil.virtual_memory().percent}% (Of {round(round(round(psutil.virtual_memory().total/1024)/1024)/1024)}GB)```",inline=True)
    embedVar.add_field(name=f"Python", value=f"```Active Python Threads: {threading.active_count()}\n{built_using}```",inline=True)
    embedVar.add_field(name=f"Discord Bot", value=f"```Internet -> Discord API latency: {round(client.latency*1000)}ms```",inline=True)
    embedVar.add_field(name=f"Web Panel", value=f"```Panel Online: {panelStatus}\nLocal IP Address: {str(socket.gethostbyname(str(socket.gethostname())))}\nPort: {str(PanelPort)}```",inline=True)
    await ctx.reply(embed=embedVar, mention_author=True)

print('Launching BOT 0/100%')

threading.Thread(target=flaskThread).start()
client.run(token)
