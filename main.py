import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'i am ready {bot.user}')

@bot.command()
async def hallo(ctx):
    await ctx.send('hallo')
    

@bot.command(title="pong!", description="send asf pong!")
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
# extensions = [
#               "cogs.test"
# ]
# if __name__ == "__main__":
#   for extension in extensions:
#     try:
#       bot.load_extension(extension)
#     except Exception as e:
#       print(f"error loading {extension}", file=sys.stderr)
#       traceback.print_exc()

bot.run("Nzk3NDU1OTc1MTMyMTY4MjYz.GjUN1M.HS7HkLOXwSqNa_FFh9zuU6rdS0Ixmi0srzkho4")