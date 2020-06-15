import discord
from discord.ext import commands
import os
from datetime import datetime

class Welcomebye(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Cog \'{}\' loaded.'.format(os.path.basename(__file__)[:-3]))

    #@commands.Cog.listener()
    #async def on_member_join(self, member):
    #    print(f'{member} has joined the server.')
    #    channel = member.guild.text_channels[0]
    #    await channel.send(f'Welcome, **<@{member.id}>**! {member.avatar_url}')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')
        channel = member.guild.text_channels[0]
        await channel.send(f'Au revoir, adiós, arrivederci and good bye, **<@{member.id}>**!')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.text_channels[0]
        #embedit0 = discord.Embed(title = "Welcome to " + member.guild.name, colour=discord.Colour(0x87a04a), url="https://google.com",description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown.")
        embedit0 = discord.Embed(title = "Welcome to " + member.guild.name, colour=discord.Colour(0x87a04a), url="",description="The main language here is english. If you are in contact with an Arena member who is not already with us, please invite. :pray:\n\nMay we add your Arena payout time (GMT) to the list at <#712293077670166528> ?")

        embedit0.set_image(url = member.avatar_url)
        embedit0.set_thumbnail(url = member.guild.icon_url)
        embedit0.set_author(name = member.name, url="", icon_url = member.avatar_url)
        #embedit0.set_footer(text = "You joined us " + datetime.now().strftime('%d-%m-%Y %H:%M:%S') , icon_url = member.guild.icon_url)
        embedit0.set_footer(text = "Joined us " + datetime.now().strftime('%d-%m-%Y %H:%M:%S') , icon_url = "https://discord.com/assets/28174a34e77bb5e5310ced9f95cb480b.png")

        await channel.send(embed = embedit0)

def setup(bot):
    bot.add_cog(Welcomebye(bot))

#The main language here is english.\n If you are in contact with an Arena member who is not already with us, please invite. :pray:\n May we add your Arena payout time (GMT) to the list at #info ?
