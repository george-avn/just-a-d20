import sys

import discord
from discord.ext import commands
import os
from discord.ext.commands import CommandOnCooldown

sys.path.insert(1, os.path.abspath('modules'))
from modules import db_handler, plotter,exp_handler

color = 0x0A0045


class Profile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 120, commands.BucketType.user)
    @commands.command(aliases=['profile', 'Profile', 'p'])
    async def _profile(self, ctx, *, name: discord.User = False):
        try:
            uid = name.id
        except:
            uid = ctx.author.id
            name = ctx.author

        if db_handler.check_user(id=uid):
            data = db_handler.fetch_user(id=uid)
            exp_data = exp_handler.calculate_rank(id=uid)
            embed = discord.Embed(
                description=f"Statistics of user : `{name}`\nTotal EXP : `{data['exp']}`⠀⠀Prestige Rank : `{data['prestige']}`\nLevel : `{exp_data[0]}`⠀⠀Badges : {exp_data[1]}",
                color=color)
            embed.add_field(name='D4', value=f"`{data['rolls']['d4']}`")
            embed.add_field(name='D6', value=f"`{data['rolls']['d6']}`")
            embed.add_field(name='D8', value=f"`{data['rolls']['d8']}`")
            embed.add_field(name='D10', value=f"`{data['rolls']['d10']}`")
            embed.add_field(name='D12', value=f"`{data['rolls']['d12']}`")
            embed.add_field(name='D20', value=f"`{data['rolls']['d20']}`")
            embed.set_thumbnail(url=name.avatar_url)
            plotter.plot(data=data)
            file = discord.File("bar.png", filename="bar.png")
            embed.set_image(url="attachment://bar.png")
            embed.set_footer(text=f"Invoked by {ctx.message.author}")
            await ctx.send(embed=embed, file=file)

    @_profile.error
    async def profile_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            await ctx.send(
                f'You are on cooldown to preserve server resources, this command will be available to you in {str(round(error.retry_after / 60))} minute(s)')

    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(aliases=['delprofile', 'Delprofile'])
    async def _delete_profile(self, ctx):
        uid = ctx.author.id
        mention = ctx.author.mention
        if db_handler.check_user(id=uid):
            await ctx.send(
                f'{mention} your profile has been cleared, it will be recreated once you use the ./dice command')
            db_handler.drop_user(id=uid)
        else:
            await ctx.send('User does not exist in database yet.')


def setup(client):
    client.add_cog(Profile(client))
