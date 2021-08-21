import random

import aiofiles

import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

activity = discord.Game(name="d!help list")

bot = commands.Bot(command_prefix="d!", intents=intents, activity=activity, status=discord.Status.online,
                   help_command=None,
                   allowed_mentions=discord.AllowedMentions(
                       users=True,  # Whether to ping individual user @mentions
                       everyone=True,  # Whether to ping @everyone or @here mentions
                       roles=False,  # Whether to ping role @mentions
                       replied_user=False,  # Whether to ping on replies to messages
                   ),
                   )
bot.reaction_roles = []


# Lowercase function
def lower(message):
    return f'{message}'.lower()


@bot.event
async def on_ready():
    async with aiofiles.open("reaction_roles.txt", mode="a") as temp:
        pass

    async with aiofiles.open("reaction_roles.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            bot.reaction_roles.append((int(data[0]), int(data[1]), data[2].strip("\n")))

    print(f'{bot.user} has connected to Discord!')

'''
@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    """A global error handler cog."""
    if isinstance(error, commands.CommandNotFound):
        message = f"This command is not listed in {bot.user} dictionary. Please try again."
        embed = discord.Embed(title=f"Woah, woah!", description=message, colour=0xd80000)
        await ctx.send(embed=embed, delete_after=5)
        # return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        embed = discord.Embed(title=f"Woah, woah!", description=message, colour=0xd80000)
        await ctx.send(embed=embed, delete_after=5)
    elif isinstance(error, commands.MissingPermissions):
        message = "You are missing the required permissions to run this command!"
        embed = discord.Embed(title=f"Woah, woah!", description=message, colour=0xd80000)
        await ctx.send(embed=embed, delete_after=5)
    elif isinstance(error, commands.NoPrivateMessage):
        message = "Private messages only. How cute."
        embed = discord.Embed(title=f"Woah, woah!", description=message, colour=0xd80000)
        await ctx.send(embed=embed, delete_after=5)
    elif isinstance(error, commands.MissingRequiredArgument):
        message = "Command is missing an argument. Try again."
        embed = discord.Embed(title=f"Woah, woah!", description=message, colour=0xd80000)
        await ctx.send(embed=embed, delete_after=5)
    elif isinstance(error, commands.CheckFailure):
        message = "You do not have the permissions to do this."
        embed = discord.Embed(title=f"Woah, woah!", description=message, colour=0xd80000)
        await ctx.send(embed=embed, delete_after=5)
    elif isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        message = "You don't have any role to run this command."
        embed = discord.Embed(title=f"Woah, woah!", description=message, colour=0xd80000)
        await ctx.send(embed=embed, delete_after=5)
    else:
        message = "Oh no! Something went wrong while running the command!"
        embed = discord.Embed(title=f"Woah, woah!", description=message, colour=0xd80000)
        await ctx.send(embed=embed, delete_after=5)
'''

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    # Text on txt
    with open('respon_and_answer/bad_word.txt', encoding="utf8") as file:
        bad_word = file.read().split(",")
    with open('respon_and_answer/praise_word.txt', encoding="utf8") as file2:
        praise_word = file2.read().split(",")

    if message.author != bot.user and not message.attachments and not message.embeds:
        if all(word == lower(message.content) for word in bad_word):
            emb = discord.Embed(colour=0xd80000,
                                description=random.choice(
                                    open('respon_and_answer/bad_answer.txt', encoding="utf8").readlines())
                                )
            await message.channel.send(embed=emb)

        elif all(word == lower(message.content) for word in praise_word):
            emb = discord.Embed(colour=0xd80000,
                                description=random.choice(
                                    open('respon_and_answer/praise_answer.txt', encoding="utf8").readlines())
                                )
            await message.channel.send(embed=emb)

    if message.author == bot.user or message.attachments or message.embeds:
        return
      
    if bot.user.mentioned_in(message) and 'Hi' in message.content:
        await message.channel.send(':hand_splayed: Yo, what\'s up?')

    if "tau aku" in lower(message.content):
        await message.channel.send("TaU aKu")
    elif "apasih lol" in lower(message.content):
        await message.channel.send("ApAsIh LoL")

    else:
        return


@bot.event
async def on_raw_reaction_add(payload):
    for role_id, msg_id, emoji in bot.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            await payload.member.add_roles(bot.get_guild(payload.guild_id).get_role(role_id))
            return


@bot.event
async def on_raw_reaction_remove(payload):
    for role_id, msg_id, emoji in bot.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            guild = bot.get_guild(payload.guild_id)
            await guild.get_member(payload.user_id).remove_roles(guild.get_role(role_id))
            return


bot.load_extension("bot_command_all.bot_commands_list_admin")
bot.load_extension("bot_command_all.bot_commands_list")
bot.load_extension("bot_command_all.bot_commands_help")
bot.load_extension("misc.api_blogspot")
bot.load_extension("misc.api_anilist")
bot.load_extension("simple_werewolf.simple_werewolf")
bot.run(TOKEN)
