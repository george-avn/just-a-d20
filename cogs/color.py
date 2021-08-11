import random
import discord
from PIL import Image
from discord.ext import commands


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb2hex(r, g, b):
    return f'#{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}'




class Color(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['color', 'colour', 'Color', 'Colour'])
    async def _color(self, ctx):
        r = (random.randint(0, 255))
        g = (random.randint(0, 255))
        b = (random.randint(0, 255))

        img = Image.new('RGB', (30, 80), color=(r, g, b))
        img.save('src/img.png')
        file = discord.File('src/img.png', filename='img.png')
        embed = discord.Embed(title=f"`Hex : {rgb2hex(r, g, b)}`",
                              description=f'**Red** : `{r}`\n**Green** : `{g}`\n**Blue**: `{b}`',
                              color=discord.Color.from_rgb(r, g, b))
        embed.set_thumbnail(url="attachment://img.png")
        embed.set_footer(text=f"Invoked by {ctx.message.author}")
        await ctx.send(file=file, embed=embed)


def setup(client):
    client.add_cog(Color(client))
