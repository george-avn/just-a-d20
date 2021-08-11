import discord
from discord.ext import commands
import random

dot = '<:dot:812387602874761288>'
mail = ''
responses = ['<:blobwizard:812728655221358632> 📬 DM Incoming! 📬 <:blobwitch:812728589048479764>',
             '<:blobwitch:812728589048479764> 📬 Check your DMs! 📬 <:blobwizard:812728655221358632>',
             '<:blobwitch:812728589048479764> 📬 I got you homie, DMed! 📬 <:blobwizard:812728655221358632>']
color = 0x0A0045
main_commands = f"""
{dot}`./roll` - Roll20 syntax dice roller. *
{dot}`./coinflip` - Coin flipper. *
{dot}`./randchar` - Random character ability scores. *
"""
other_commands = f"""
{dot}`./element` - Search the periodic table.
{dot}`./color` - Random color with hex & rgb codes.
{dot}`./8ball` - Standard 8ball command.
"""
info_commands = f"""
{dot}`./profile` - Dice rolling statistics.
{dot}`./delprofile` - Delete your dice rolling profile.
{dot}`./about` - Information about the bot,credits and its developer.
{dot}`./ping` - Check the bot's latency to Discord servers.
{dot}`./invite` - Invite the bot to your server.
"""

dice_arguments = """
`h` **-** Highest Rolls\nExample : `5d20h3` returns the 3 highest rolls from the five d20 that were rolled.\n
`l` **-** Lowest Rolls\nExample : `5d20l3` returns the 3 lowest rolls from the five d20 that were rolled.\n
`+` **-** Adds to sum\nExample : `5d20+3` adds 3 to the sum of the five d20 that were rolled, always returns a single integer.\n
`-` **-** Subtracts from sum\nExample : `5d20-3` subtracts 3 from the sum of the five d20 that were rolled, always returns a single integer.\n
`.-` **-** Subtracts from each individual roll\nExample : `5d20.-3` subtracts 3 from each of the five d20 that were rolled.\n
`.+` **-** Adds to each individual roll\nExample : `5d20.+3` adds 3 to each of the five d20 that were rolled.\n
`e` **-** "Exploding dice\nExample : `5d20e` if any of the five rolls goes critical, it gets re-rolled and added to the individual roll.\n 
"""
dice_adv = """
`adv` **-** Rolling with Advantage\nExample : `5d20 adv` will roll with advantage, compatible will all arguments from above, `5d20e adv` or `5d20.+3 adv`.\n\n
`dis` **-** Rolling with Disadvantage\nExample : `5d20 dis` will roll with disadvantage, compatible will all arguments from above, `5d20e dis` or `5d20.+3 dis`.
"""
coinflip = """
`./coinflip` **-** This will do 1 coinflip.

`./coinflip 100` **-** This will do 100 coinflips and aggregate them for the result.
"""
randchar = """
Rolls four(4) d6 dice and keeps the highest 3, represented as `4d6h3`.It does this 6 times.Useful when creating new D&D characters.
"""
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(alias='Help')
    async def help(self, ctx, *, arg0: str = False):
        if arg0 is False:
            embed = discord.Embed(
                description=f'Commands of `{self.client.user}`\n\nUse ./help [command] for usage information on a command\n Example -> ./help roll\nCommands with * support this help function.\n\n',
                color=color)
            embed.add_field(name='DnD Commands', value=main_commands, inline=False)
            embed.add_field(name='Misc Commands', value=other_commands, inline=False)
            embed.add_field(name='Utility Commands', value=info_commands, inline=False)
            embed.set_footer(text=f"Invoked by {ctx.message.author}")
            await ctx.author.send(embed=embed)
            if not isinstance(ctx.channel, discord.channel.DMChannel):
                embed0 = discord.Embed(
                    description=random.choice(responses),
                    color=color)
                await ctx.send(embed=embed0)

        elif arg0 == 'roll':
            embed = discord.Embed(
                title='`./roll` or `./r` or `./Roll`',
                description='This command has 2 input arguments,the first '
                            'is always the rolling argument and is mandatory,the second is optional and is the '
                            'advantage/disadvantage argument.\nMax allowed roll is 500d1000.\n\nEach time you roll you gain exp to level up, each level is 250 exp and each rank is 10 levels, when you reach level 200 you will prestige and reset to 0.',
                color=color)

            embed.add_field(name='Dice Arguments', value=dice_arguments, inline=False)
            embed.add_field(name='Advantage/Disadvantage', value=dice_adv, inline=False)
            await ctx.author.send(embed=embed)
            if not isinstance(ctx.channel, discord.channel.DMChannel):
                embed0 = discord.Embed(
                    description=random.choice(responses),
                    color=color)
                await ctx.send(embed=embed0)
        elif arg0 == 'coinflip':
            embed = discord.Embed(
                title='`./coinflip`',
                description='This command has 1 input argument ,which is optional.\nMax allowed flips are 10000.',
                color=color)

            embed.add_field(name='Usage', value=coinflip, inline=False)
            await ctx.author.send(embed=embed)
            if not isinstance(ctx.channel, discord.channel.DMChannel):
                embed0 = discord.Embed(
                    description=random.choice(responses),
                    color=color)
                await ctx.send(embed=embed0)
        elif arg0 == 'randchar':
            embed = discord.Embed(
                title='`./randchar` or `./rc`',
                description='This command has 0 input argument.',
                color=color)

            embed.add_field(name='Usage', value=randchar, inline=False)
            await ctx.author.send(embed=embed)
            if not isinstance(ctx.channel, discord.channel.DMChannel):
                embed0 = discord.Embed(
                    description=random.choice(responses),
                    color=color)
                await ctx.send(embed=embed0)

def setup(client):
    client.add_cog(Help(client))
