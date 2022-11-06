import discord
from discord.ext import commands


class Test(commands.Cog):
	def __init__(self, client):
		self.bot = bot


    @commands.command()
    async def ping(ctx, self):
        await ctx.send('pong!') 

  


def setup(bot):
	bot.add_cog(Test(bot))