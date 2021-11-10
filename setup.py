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

import os
import sys

if os.path.exists("config.json") == False:
    print("No config file found. Starting setup run.")
    import json
    f = open("config.json", "w+")

    yourname = input("How should ProCTRL call you? ")
    prefix = input("What should the bot prefix be? ")
    status = input("Do you want to change the bot's activity (y/N)? ")
    if status == "y":
        cstatus = input("What should be the status? ")
    else:
        cstatus = f"{prefix}help | ProCTRL"
        print("Skipping custom activity step.")
    guild = input("What is the ID of the guild you'll be using the bot on? ")
    client_id = input("What is the bot's client ID? ")
    token = input("What is the bot's token? ")
    dashport = input("What would be the port we use for the panel [80]? ")
    if dashport == None:
        dashport = 80
    print("")
    print("Thanks for filling our form! We are now setting you up.")
    c = {
        "username": yourname,
        "prefix": prefix,
        "status": cstatus,
        "guild": guild,
        "token": token,
        "client_id": client_id,
        "dashport": dashport
    }

    cdump = json.dumps(c)
    json.dump(c, f)
    f.close()

else:
    print("Config file found. Skipping config setup.")
    sys.exit(0)

module = "pypresence"
try:
    exec(f"from {module} import *")
except ImportError as e:
    try:
        os.system(f"pip3 install {module}")
    except Exception as e:
        print("Uh oh! Something has broken :(")
        sys.exit(1)

module = "discord"
try:
    exec(f"from {module} import *")
except ImportError as e:
    try:
        os.system(f"pip3 install {module}")
    except Exception as e:
        print("Uh oh! Something has broken :(")
        sys.exit(1)

module = "discord-py-slash-command"
try:
    exec(f"from discord_slash import *")
except ImportError as e:
    try:
        os.system(f"pip3 install {module}")
    except Exception as e:
        print("Uh oh! Something has broken :(")
        sys.exit(1)
    
module = "psutil"
try:
    exec(f"from {module} import *")
except ImportError as e:
    try:
        os.system(f"pip3 install {module}")
    except Exception as e:
        print("Uh oh! Something has broken :(")
        sys.exit(1)
    
module = "flask"
try:
    exec(f"from {module} import *")
except ImportError as e:
    try:
        os.system(f"pip3 install {module}")
    except Exception as e:
        print("Uh oh! Something has broken :(")
        sys.exit(1)

print("Done!")
