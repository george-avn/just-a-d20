import json
import discord
import os
from discord.ext import commands, tasks

# Loading the Setting json
path = os.path.abspath("settings/settings.json")
with open(path, "r") as read_file:
    loaded_settings = json.load(read_file)

# Setting the prefix and removing the default help command
client = commands.Bot(command_prefix=loaded_settings['prefix'], pm_help=True)
client.remove_command("help")


# On Ready Routine
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print(f"{client.user}: Online")
    change_presence.start()
    print(f'In {str(len(client.guilds))} server')


# The Presence Loop
@tasks.loop(seconds=6000)
async def change_presence():
    status = discord.Activity(type=discord.ActivityType.watching,
                              name=f"for {loaded_settings['prefix']}help")
    await client.change_presence(activity=status)


# --------------

def cog_init():
    for cog in os.listdir('cogs'):
        if cog.endswith('.py'):
            cog: str = cog[:-3]
            client.load_extension(f"cogs.{cog}")


# Main Cog Loading
if __name__ == "__main__":
    cog_init()
    client.run(loaded_settings['bot_token'])
