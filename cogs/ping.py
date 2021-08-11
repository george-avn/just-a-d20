import discord
from discord.ext import commands

color = 0x0A0045


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(alias='Ping')
    async def ping(self, ctx):
        embed = discord.Embed(
            description=f'**Latency to discord servers : **`{round(self.client.latency* 100, 3) }`**ms**', color=color)
        embed.set_footer(text=f"Invoked by {ctx.message.author}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Ping(client))
