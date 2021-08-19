from os import getenv

import requests
# import json
import discord

from dotenv import load_dotenv
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
from googleapiclient.discovery import build

from main import bot

load_dotenv()
Key = getenv('BLOGSPOT_API')  # Replace with your API key.
BlogID = getenv('BLOG_ID')  # Replace with your BlogId here.

Roles = ["◉ Member"]  # Add your server roles here.

blog = build("blogger", "v3", developerKey=Key)


class BlogApi(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.channel = None
        self.guild = None
        self.bot = bot

    @commands.command(pass_context = True, aliases=['blog_search', 'blog_s'])
    async def search(self, ctx: commands.Context, arg):
        search_term = str(arg).replace(" ", "%")
        base_url = "https://www.googleapis.com/blogger/v3/blogs/" + BlogID + "/posts/search"
        complete_url = base_url + "?q=" + search_term + \
                       "&key=" + Key
        response = requests.get(complete_url)
        result = response.json()

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        embed = discord.Embed(title="List of Search results",
                              description="Checked on " + f"{current_time}\n", color=0x349bfc)
        embed.set_author(name="Dase's Place", icon_url="https://avatars.githubusercontent.com/u/77565642")
        embed.set_thumbnail(url="https://www.dase-s-place.com/favicon.ico")
        try:
            for count, value in enumerate(result["items"]):
                title = result["items"][count]["title"]
                url = result["items"][count]["url"]
                embed.description = embed.description + \
                                    f"{count + 1}. [{title}]({url})\n"
            embed.set_footer(text='Apa ada artikel yang kalian mau?\nAny article do you want?')

            await ctx.send(embed=embed)
        except:
            await ctx.send("There is something wrong with the response.")

    bot.recentPosts = None
    bot.recentPostsTime = None
    bot.recentPostsEdit = None

    @tasks.loop(seconds=300.0)
    async def fetchUpdates(self):
        posts = blog.posts().list(blogId=BlogID).execute()
        postsList = posts["items"]
        postTime = postsList[0]["published"]
        if not self.bot.recentPosts:
            self.bot.recentPostsTime = postTime
            self.bot.recentPosts = postsList
        elif self.bot.recentPostsTime != postTime:
            titleValue = str(posts["items"][0]["title"])
            urlValue = str(posts["items"][0]["url"])

            channel = self.bot.get_channel(864547212574982205)  # Add channel ID
            embed = discord.Embed(title=":flag_id: Artikel baruku!\n:flag_gb: My new article!",
                                  description=f"[{titleValue}]({urlValue})")

            embed.set_author(name="Dase's Place", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_thumbnail(url="https://www.dase-s-place.com/favicon.ico")
            for i in Roles:
                if i.lower() in postsList[0]["title"].lower():
                    guild = self.bot.guilds[0]
                    await channel.send(discord.utils.get(guild.roles, name=i).mention, delete_after=86400.0)
                    await channel.send(embed=embed, delete_after=86400.0)
                    break

            self.bot.recentPostsTime = postTime
            self.bot.recentPosts = postsList


f = BlogApi(bot)
f.fetchUpdates.start()


def setup(bot: commands.Bot):
    bot.add_cog(BlogApi(bot))
