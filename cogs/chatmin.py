import discord
from discord.ext import commands
import os

class Chatmin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Cog \'{}\' loaded.'.format(os.path.basename(__file__)[:-3]))

    #delete last messges via !clear #
    @commands.command()
    @commands.has_permissions(manage_messages=True)

    async def clear(self, ctx, amount : int):
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f'Deleted {len(deleted)} messages.')

    #delete certain users last messges via !myclear #
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def count(self, ctx):
        #await ctx.send(ctx.message.author.id)
        msg1 = await ctx.channel.send('Calculating...')
        counter = 2
        msg2 = await ctx.channel.send(counter)

        async for entry in guild.audit_logs(limit=100):
            print('{0.user} did {0.action} to {0.target}'.format(entry))


def setup(bot):
    bot.add_cog(Chatmin(bot))
