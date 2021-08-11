import os
import sys

import discord
from discord.ext import commands

color = 0x0A0045
from os import listdir
from os.path import isfile, join, abspath

sys.path.insert(1, abspath('modules'))
from modules import db_handler

cogs = ['8ball.py',
        'about.py',
        'admin.py',
        'botstats.py',
        'coin.py',
        'color.py',
        'dice.py',
        'elements.py',
        'help.py',
        'info.py',
        'ping.py',
        'profile.py']


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    async def load(self, ctx, module: str):
        if ctx.message.author.id == 522087338428596245:
            try:
                self.client.load_extension(f'cogs/{module}.py')
            except Exception as e:
                await self.bot.say('\N{PISTOL}')
                await self.bot.say('{}: {}'.format(type(e).__name__, e))
            else:
                await self.bot.say('\N{OK HAND SIGN}')

    @commands.command(hidden=True)
    async def unload(self, ctx, module: str):
        if ctx.message.author.id == 522087338428596245:
            try:
                self.client.reload_extension(f'cogs/{module}.py')
            except Exception as e:
                await ctx.send('\N{PISTOL}')
                await ctx.send('{}: {}'.format(type(e).__name__, e))
            else:
                await ctx.send('\N{OK HAND SIGN}')

    @commands.command(hidden=True)
    async def reload(self, ctx, module: str):
        if ctx.message.author.id == 522087338428596245:
            try:
                self.client.reload_extension(f'cogs/{module}.py')
            except Exception as e:
                await ctx.send('\N{PISTOL}')
                await ctx.send('{}: {}'.format(type(e).__name__, e))
            else:
                await ctx.send('\N{OK HAND SIGN}')

    @commands.command(hidden=True)
    async def reload_all(self, ctx):
        if ctx.message.author.id == 522087338428596245:
            for cog in os.listdir('cogs'):
                try:
                    if cog.endswith('.py'):
                        cog: str = cog[:-3]
                        self.client.reload_extension(f"cogs.{cog}")
                except Exception as e:
                    await ctx.send('\N{PISTOL}')
                    await ctx.send('{}: {}'.format(type(e).__name__, e))
                else:
                    await ctx.send(f':ok_hand:{cog}')


def setup(client):
    client.add_cog(Admin(client))
