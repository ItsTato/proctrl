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
