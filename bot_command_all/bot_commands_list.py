import random
import time
from os import getenv

import discord
from discord.ext import commands

from dotenv import load_dotenv
import giphy_client
from giphy_client.rest import ApiException

load_dotenv()


class SomeCommands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # ## Command yang bisa digunakan oleh Umum

    """Bagian yang digunakan untuk umum"""

    @commands.command(aliases=['HELLO', 'h'])
    @commands.cooldown(rate=1, per=10)
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Hello, {ctx.message.author.mention}!")

    @commands.command(aliases=['PING'])
    @commands.cooldown(rate=1, per=10)
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket and API latency."""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(
            content=f"Your ping right now is {round(self.bot.latency * 1000)}ms\n"
                    f"API's ping right now is {round((end_time - start_time) * 1000)}ms")

    @commands.command(aliases=['SAY'])
    async def say(self, ctx: commands.Context, *, arg):
        await ctx.message.delete()
        await ctx.send(arg)

    @commands.command(aliases=['MINNA'])
    @commands.cooldown(rate=1, per=30)
    async def minna(self, ctx: commands.Context, arg1):
        if arg1 == "everyone":
            await ctx.message.delete()
            await ctx.send(f"@everyone\n"
                           f":flag_id: Gimana kabar hari ini?\n"
                           f":flag_gb: How you'll today?")
        elif arg1 == "here":
            await ctx.message.delete()
            await ctx.send(f"@here\n"
                           f":flag_id: Gimana kabar hari ini?\n"
                           f":flag_gb: How you'll today?")

    @commands.command(aliases=['MOTIVATION', 'mot'])
    @commands.cooldown(rate=1, per=8)
    async def motivation(self, ctx: commands.Context):
        embed = discord.Embed(
            title='Motivational Quote', colour=0x87CEEB,
            description=random.choice(open('misc/quotes.txt', encoding="utf8").readlines())
        )
        await ctx.send(embed=embed)
        time.sleep(0.001)
        await ctx.send(random.choice(open('misc/gifs.txt', encoding="utf8").readlines()))

    @commands.command(aliases=['MAKAR'])
    async def makar(self, ctx, member: discord.Member):
        pass

    @commands.command(aliases=['POLL'])
    async def poll(self, ctx, *, message):
        emb = discord.Embed(title=" POLL", description=f"{message}")
        msg = await ctx.channel.send(embed=emb)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

    @commands.command(aliases=['GIF'])
    async def gif(self, ctx, *, q="random"):
        api_key = getenv('GIPHY_KEY')
        api_instance = giphy_client.DefaultApi()

        try:
            # Search Endpoint

            api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=q, colour=0x87CEEB)
            emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    @commands.command(aliases=['DM'])
    async def dm(self, ctx, member: discord.Member, *, content):
        await ctx.message.delete(delay=2)
        channel = await member.create_dm()
        await channel.send(content)


def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))
