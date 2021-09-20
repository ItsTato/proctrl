import os
import sys

if os.path.exists("config.json") == False:
    print("No config file found. Starting setup run.")
    import json
    f = open("config.json", "w+")

    yourname = input("How should ProCTRL call you? ")
    prefix = input("What should the bot prefix be? ")
    status = input("Do you want to change the bot's activity (y/n)? ")
    if status == "y":
        cstatus = input("What should be the status? ")
    else:
        cstatus = f"{prefix}help | ProCTRL"
        print("Skipping custom activity step.")
    guild = input("What is the ID of the guild you'll be using the bot on? ")
    client_id = input("What is the bot's client ID? ")
    token = input("What is the bot's token? ")
    print("")
    print("Thanks for filling our form! We are now setting you up.")
    c = {
        "username": yourname,
        "prefix": prefix,
        "status": cstatus,
        "guild": guild,
        "token": token,
        "client_id": client_id
    }

    cdump = json.dumps(c)
    json.dump(c, f)
    print(f"Wrote to json file the following:\n{c}")
    f.close()
else:
    print("Config file found, not doing anything.")
    sys.exit(0)
