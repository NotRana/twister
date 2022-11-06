import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())

bot.remove_command('help')

@bot.event
async def on_ready():
  print(f"Bot is Ready {bot.user}")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Under Development."))
print("Presence has been set")

# @bot.command()
# async def hallo(ctx):
#     await ctx.send('hallo')
    

@bot.command(title="pong!", description="send asf pong!")
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")



# kick command

@bot.command(title="say", description="kick a membr from the server")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  if reason == None:
    reason = "***Reason not provided***"
    await ctx.guild.kick(member)
    await ctx.send(f"Successfully Kicked {member}REASON: {reason}")


@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please mention the member to kick")
    if isinstance(error, commands.MissingPermissions):
      await ctx.send("You dont have permission(s) to use this command")

# ban command

@bot.command(title="ban", description="ban a member from the server")
@commands.has_permissions(kick_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  if reason == None:
    reason = "Reason not provided"
  await ctx.guild.ban(member)
  await ctx.send(f"{member.mention}Successfully ban by {ctx.author.mention}REASON: ***{reason}***")


@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please mention the member to ban")
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You dont have permission(s) to use this command")

# purge command

@bot.command(title="purge", description="remove messages")
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f"{amount} Messages Were Deleted!")

@purge.error
async def purge_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please spacify the number of message to delete.")

  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You dont have permission(s) to use this command")

# warn command

@bot.command(title="warn", description="warn a member")
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member, reason=None):
  if reason == None:
    reason = "***No Reason Provided***"
  embed=discord.Embed(title="Warned!", description=f"{member.mention} has been warned for {reason}\n Moderator: {ctx.author.mention}\nWarned Member: {member.mention}", colour=discord.Colour.random())
  await ctx.send(embed=embed)

  embed=discord.Embed(title="Warned!", description=f"{member.mention} has been warned for {reason}\n Moderator: {ctx.author.mention}\nWarned Member: {member.mention}", colour=discord.Colour.blue())
  await member.send(embed=embed)

# mute command

@bot.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member, * , reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speek=False, send_messages=False, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason: {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter the username to unban.")

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have permission(s) to use this command")

      
# unmute command

      
@bot.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"You were unmuted in the server {guild.name}")
    await member.send(f"You were unmuted in the server {guild.name}")

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter the username to unban.")

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have permission(s) to use this command")
# slash commands for test

@bot.command()
async def say(ctx, message):
  em = discord.Embed(description=f"{message}", colour=discord.Color.random())
  await ctx.send(embed=em)
# help command

@bot.command()
async def help(ctx):
    em = discord.Embed(title="Help", description="Use /help for commands", colour=discord.Color.random())
    em.add_field(name = "Moderation", value = "> `kick`,`ban`,`unban`,`mute`,`unmute`,`warn`,`lock`,`unlock`,`giverole`")
    em.add_field(name="Fun", value="> `meme(comming soon)`")
    em.add_field(name="Utility", value="> `say`,`purge`,`ping`,`avatar`,`avatar`,`report`")
    em.set_footer(text="Made By Rana Asad.py#5925")
    await ctx.send(embed=em)


# avatar command

@bot.command()
async def avatar(ctx, *, member: discord.Member=None):
  if member == None:
    member = ctx.author
  userAvatarUrl = member.display_avatar
  em = discord.Embed(title="Download Link", url=f"{userAvatarUrl}", colour=discord.Color.random()) 
  em.set_image(url=f"{userAvatarUrl}")
  await ctx.send(embed=em)

# channel lock

@bot.command()
@commands.has_permissions(kick_members=True)
async def lock(ctx, channel: discord.TextChannel):
  await channel.set_permissions(ctx.guild.default_role,send_messages=False)
  await ctx.send(f"{channel.mention} channel has been locked")
  
# unloack command
  
@bot.command()
@commands.has_permissions(kick_members=True)
async def unlock(ctx, channel: discord.TextChannel):
  await channel.set_permissions(ctx.guild.default_role,send_messages=True)
  await ctx.send(f"{channel.mention} channel has been unlocked")

# role add

@bot.command()
@commands.has_permissions(kick_members=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"hey {ctx.author.mention}, {user.mention} has been giving a role called: {role.mention}")

# report command

@bot.command()
async def report(ctx, *, bug):
  channel = bot.get_channel(1037037515691016323)
  await ctx.send("Your bug has been submitted")
  em = discord.Embed(
    title='Bug!',
    description=f"Bug: {bug}\nFrom: {ctx.author.name}\nserver name: {ctx.guild.name}",
    colour = discord.Colour.random()
  )
  await channel.send(embed=em)









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