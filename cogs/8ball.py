import random

import discord
from discord.ext import commands
color = 0x0A0045



class Magicball(commands.Cog):
    def __init__(self, client):
        self.client = client

    # The 8ball Command
    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                     "Yes.",
                     "No.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes, of course.",
                     "Absolutely",
                     "I don't think so.",
                     "As I can see it, yes!",
                     "Most likely.",
                     "Signs point to yes",
                     "Don't count on it.",
                     "I doubt it.",
                     "Impossible.",
                     "Simply, No.",
                     "Very doubtful.",
                     "My sources say no.",
                     "Ehhhh, no.",
                     "Probably"]

        embed0 = discord.Embed(
            description=f'**Q:** {question}\n**A:** {random.choice(responses)}',
            color=color)
        await ctx.send(embed=embed0)


def setup(client):
    client.add_cog(Magicball(client))
