import discord
from discord.ext import commands


class Test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


  @bot.slash_command(title="pong!", description="send pong!")
  async def ping(ctx, self):
    await ctx.respond(f"Pong! {round(bot.latency * 1000)}ms")

  


async def setup(bot):
    await bot.add_cog(Test(bot))
  print('test cog is ready')