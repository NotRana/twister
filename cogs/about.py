import discord
from discord.ext import commands


class About(commands.Cog):
    def __init__(bot , self):
        self.bot = bot



    @commands.slash_command(name="about", description="About Me")
    async def about(self,ctx: discord.ApplicationContext):
        await ctx.respond("This is my about")


def setup(bot):
    bot.add_cog(About(bot))