import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="&", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'i am ready {bot.user}')

@bot.command()
async def hallo(ctx):
    await ctx.send('hallo')

bot.run("Nzk3NDU1OTc1MTMyMTY4MjYz.GjUN1M.HS7HkLOXwSqNa_FFh9zuU6rdS0Ixmi0srzkho4")