import discord
from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @bot.slash_command(title="pong!", description="send asf pong!")
    async def ping(ctx):
      await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


def setup(bot):
    bot.add_cog(ping(bot))
    print("ping command is ready")