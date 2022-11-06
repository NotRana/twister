import discord
from discord.ext import commands


class Test(commands.Cog):
	def __init__(self, client):
		self.bot = bot


    @bot.slash_command(title="pong!", description="send pong!")
    async def ping(ctx, self):
        await ctx.respond(f"Pong! {round(bot.latency * 1000)}ms")

  


def setup(bot):
	bot.add_cog(Test(bot))