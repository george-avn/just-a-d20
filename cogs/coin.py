import discord
from discord.ext import commands
import random
color = 0x0A0045

def flip(iteration=1):
    if iteration > 10000 or (not isinstance(iteration, int)):
        return False

    if iteration == 1:
        i = random.randint(0, 1)
        if i == 0:
            return "Heads", 0, 0
        if i == 1:
            return "Tails", 0, 0
    else:
        heads0 = 0
        tails1 = 0
        for i in range(0, iteration):
            q = random.randint(0, 1)
            if q == 0:
                heads0 = heads0 + 1
            if q == 1:
                tails1 = tails1 + 1
        if heads0 > tails1:
            return "Heads Win", heads0, tails1
        if heads0 < tails1:
            return "Tails Win", heads0, tails1
        if heads0 == tails1:
            return "Draw", heads0, tails1


class Coin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['coinflip', 'Coinflip'])
    async def _coin(self, ctx, arg: int = 1):
        if arg < 10000:
            result, heads, tails = flip(arg)
            if (heads or tails) == 0:
                embed = discord.Embed(
                    description=f"{result}", color=color)
                embed.set_footer(text=f"Invoked by {ctx.message.author}")
                await ctx.send(embed=embed)

            if (heads or tails) > 0:
                text = f'**From {arg} flips**:\n Heads: `{heads}`\nTails: `{tails}`\n\n**{result}!**'
                embed = discord.Embed(description=text,
                                      color=color)
                embed.set_footer(text=f"Invoked by {ctx.message.author}")
                await ctx.send(embed=embed)
        if arg > 10000:
            await ctx.send('**Warning** : `The Limit is 10000 to avoid hangups.`')


def setup(client):
    client.add_cog(Coin(client))