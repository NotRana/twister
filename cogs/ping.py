import discord
from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(title="pong!", description="send asf pong!")
    async def ping(ctx: discord.ApplicationContext, self):
      await ctx.respond(f"Pong! {round(self.bot.latency * 1000)}ms")


def setup(bot):
    bot.add_cog(ping(bot))
    print("ping command is ready")