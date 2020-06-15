import discord
from discord.ext import commands
import os

class Embeded1(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Cog \'{}\' loaded.'.format(os.path.basename(__file__)[:-3]))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def emsay0(self, ctx):
        embedit0 = discord.Embed(title="title ~~(did you know you can have markdown here too?)~~",colour=discord.Colour(0x87a04a),url="https://discordapp.com",description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown.")
        embedit0.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embedit0.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embedit0.set_author(name = '<@{member.id}>', url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embedit0.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        await ctx.send(embed = embedit0)


def setup(bot):
    bot.add_cog(Embeded1(bot))
