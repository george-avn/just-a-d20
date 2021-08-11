import discord
from discord.ext import commands
import psutil
import time

cpu = '<:CPU:812730062880768033>'
ram = '<:RAM:812730122469244929>'
color = 0x0A0045


def min_elapsed():
    return int((time.time() - psutil.boot_time()) // 60)


class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["uptime", 'Uptime'])
    async def _uptime(self, ctx):
        embed = discord.Embed(title=f'Uptime : {min_elapsed()} minutes.',
                              description=f'{cpu} **:** {str(psutil.cpu_percent())}**%**\n{ram} **:** {str(psutil.virtual_memory()[2])}**%**\n☁️ **:** `{round(self.client.latency * 100, 3)}`**ms**',
                              color=color)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Stats(client))
