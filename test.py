import discord
from discord.ext import commands


class Test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


  @commands.slash_command()  # Not passing in guild_ids creates a global slash command.
  async def hi(self, ctx: discord.ApplicationContext):
    await ctx.respond("Hi, this is a global slash command from a cog!")

  


adef setup(bot):
  await bot.add_cog(Test(bot))
  print('test cog is ready')