import discord
from discord.ext import commands

color = 0x0A0045
text0 = """
A simple dnd bot made by NotCrisp#7974 as a side project.If you have any suggestions feel free to contact me.
"""
text1 = f"""

Rank icons made by [Dimitry Miroliubov](https://www.flaticon.com/authors/dimitry-miroliubov) from [Flaticon](https://www.flaticon.com/)
Bot profile made by [Freepik](https://www.freepik.com) from [Flaticon](https://www.flaticon.com/)
Chemistry Data from PubChem
"""


class About(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(alias='About')
    async def about(self, ctx):
        embed = discord.Embed(
            title='Just a D20',

            description='Made by Crisp#7974\n[Bot Invite](https://discord.com/oauth2/authorize?client_id=812736459617861642&scope=bot&permissions=314432)\n[Support Server](https://discord.gg/Cj8Xfrx3jN)',
            color=color)
        file = discord.File("src/dice.png", filename="dice.png")
        embed.set_thumbnail(url="attachment://dice.png")
        embed.add_field(name='About this Bot', value=text0, inline=False)
        embed.add_field(name='Credits', value=text1, inline=False)
        embed.set_footer(text=f"Invoked by {ctx.message.author}")
        await ctx.send(file=file, embed=embed)

    @commands.command(alias='Invite')
    async def invite(self, ctx):
        embed = discord.Embed(
            description='Here is your [invite](https://discord.com/oauth2/authorize?client_id=812736459617861642&scope=bot&permissions=314432)!',
            color=color)
        embed.set_footer(text=f"Invoked by {ctx.message.author}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(About(client))
