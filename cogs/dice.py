import os
import sys

import discord
from discord.ext import commands

sys.path.insert(1, os.path.abspath('modules'))
from modules import db_handler, dice_roller, exp_handler


def database_roll_entry(uid: int, sides: int, rolls: int):
    if int(sides) == 4:
        db_handler.update_user_dice(id=uid, side='d4', rolls=rolls)
    if int(sides) == 6:
        db_handler.update_user_dice(id=uid, side='d6', rolls=rolls)
    if int(sides) == 8:
        db_handler.update_user_dice(id=uid, side='d8', rolls=rolls)
    if int(sides) == 10:
        db_handler.update_user_dice(id=uid, side='d10', rolls=rolls)
    if int(sides) == 12:
        db_handler.update_user_dice(id=uid, side='d12', rolls=rolls)
    if int(sides) == 20:
        db_handler.update_user_dice(id=uid, side='d20', rolls=rolls)


rejected = '<:rejected:812383819327078430>'
accepted = '<:accepted:812383844136517642>'
color = 0x0A0045


class Dice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["roll", 'Roll', 'r'])
    async def _dice(self, ctx, arg: str, adv: str = False):
        uid = ctx.author.id
        rolls, total, repeats, sides = dice_roller.roll(user_input=str(arg))
        db_handler.check_user(uid)
        db_handler.update_user_exp(id=uid)
        database_roll_entry(uid=uid, sides=sides, rolls=repeats)
        stats = exp_handler.calculate_rank(id=uid)
        if len(str(rolls)) > 2000:
            rolls = rolls[0:50]
            embed = discord.Embed(title=stats[1], description=f'\n{rolls}\n', color=color)
            embed.set_footer(text=f"Invoked by {ctx.message.author}\nLevel : {stats[0]}")
            await ctx.send(
                f"{ctx.author.mention} this exceeds the 2000 character limit by discord.",
                embed=embed)
        else:

            if adv is False:
                text = f"{rolls} **=** `{total}`\n"
                embed = discord.Embed(title=f'{stats[1]}', description=f'{text}\n', color=color)
                embed.set_footer(text=f"Invoked by {ctx.message.author}\nLevel : {stats[0]}")
                await ctx.send(embed=embed)
            elif adv == 'adv':
                second_rolls, second_total,second_repeats, second_sides = dice_roller.roll(user_input=str(arg))
                sum1 = total
                sum2 = second_total
                if sum1 > sum2:
                    text = f'{accepted}{rolls} **=** `{sum1}`\n||{rejected} {second_rolls} **=** `{sum2}`||'
                    embed = discord.Embed(title=stats[1], description=text, color=color)
                    embed.set_footer(text=f"Invoked by {ctx.message.author}\nLevel : {stats[0]}")
                    await ctx.send(embed=embed)
                else:
                    text = f'{accepted}{second_rolls} **=** `{sum2}`\n||{rejected}{rolls} **=** `{sum1}`||'
                    embed = discord.Embed(title=stats[1], description=text, color=color)
                    embed.set_footer(text=f"Invoked by {ctx.message.author}\nLevel : {stats[0]}")
                    await ctx.send(embed=embed)
            elif adv == 'dis':
                second_rolls, second_total, second_repeats,second_sides = dice_roller.roll(user_input=str(arg))
                sum1 = total
                sum2 = second_total
                if sum1 > sum2:
                    text = f'{accepted}{second_rolls} **=** `{sum2}`\n||{rejected}{rolls} **=** `{sum1}`||'
                    embed = discord.Embed(title=stats[1], description=text, color=color)
                    embed.set_footer(text=f"Invoked by {ctx.message.author}\nLevel : {stats[0]}")
                    await ctx.send(embed=embed)
                else:
                    text = f'{accepted}{rolls} **=** `{sum1}`\n||{rejected}{second_rolls} **=** `{sum2}`||'
                    embed = discord.Embed(title=stats[1], description=text, color=color)
                    embed.set_footer(text=f"Invoked by {ctx.message.author}\nLevel : {stats[0]}")
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=stats[1], description='`You provided invalid argument`', color=color)
                embed.set_footer(text=f"Invoked by {ctx.message.author}\nLevel : {stats[0]}")
                await ctx.send(embed=embed)

    @_dice.error
    async def dice_error(self, ctx, error):
        if isinstance(error, ValueError):
            await ctx.send('Invalid entry')


def setup(client):
    client.add_cog(Dice(client))
