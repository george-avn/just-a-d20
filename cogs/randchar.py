import os
import sys

import discord
from discord.ext import commands

color = 0x0A0045

sys.path.insert(1, os.path.abspath('modules'))
from modules import db_handler, dice_roller, exp_handler


class RandomCharacter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Randchar', 'randomcharacter', 'Randomcharacter', 'rc'])
    async def randchar(self, ctx):
        rolls, total, sides = [], [], []
        uid = ctx.author.id
        db_handler.check_user(uid)
        for i in range(0, 6):
            #bold_rolls(rolls=rolls, sides=sides), sum(rolls), repeats, sides
            temp_rolls,temp_total,temp_repeat, temp_sides = dice_roller.roll(user_input=str('4d6h3'))
            rolls.append(temp_rolls)
            total.append(temp_total)
            sides.append(temp_sides)
            db_handler.update_user_dice(id=uid, side='d6', rolls=len(temp_rolls))
        db_handler.update_user_exp(id=uid)
        stats = exp_handler.calculate_rank(id=uid)
        text = ''
        for j in range(0, 6):
            text += f'{rolls[j]} **=** `{total[j]}`\n'
        text += f'\nTotal **=** `{sum(total)}`'
        embed = discord.Embed(title=f"{stats[1]}",
                              description=text,
                              color=color)
        embed.set_footer(text=f"Invoked by {ctx.message.author}\nLevel : {stats[0]}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(RandomCharacter(client))
