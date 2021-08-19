from discord import HTTPException
from discord.ext import commands
from anilistbook.searchAnime import animeSearch
from anilistbook.reverseSearch import reverseSearch
from anilistbook.searchManga import mangaSearch
from anilistbook.searchStudio import studioSearch
from anilistbook.searchStaff import staffSearch
from anilistbook.searchCharacter import charSearch
from anilistbook.searchUser import *


class AniListApi(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.channel = None
        self.guild = None
        self.bot = bot
        self.last_msg = None

    @commands.command(aliases=['ANIME'])
    async def anime(self, ctx: commands.Context, *, title):
        embed = animeSearch(title)
        await ctx.send(embed=embed)

    @commands.command(aliases=['MANGA'])
    async def manga(self, ctx: commands.Context, *, title):
        embed = mangaSearch(title)
        await ctx.send(embed=embed)

    @commands.command(aliases=['REVERSE'])
    async def reverse(self, ctx: commands.Context, *, link):
        if link.endswith(".jpg") or link.endswith(".png") or link.endswith(".jpeg"):
            await ctx.send(embed=animeSearch(title=str(reverseSearch(link))))
        else:
            await ctx.send(embed=discord.Embed(description="Link is not a .jpg or a .png file."))

    @commands.command(aliases=['ANIUSER'])
    async def user(self, ctx: commands.Context, *, userName):
        result = generateUserInfo(userName)
        if result:
            try:
                userEmbed = userSearch(result)
                await ctx.send(embed=userEmbed)

                userAnimeEmbed = userAnime(result)
                await ctx.send(embed=userAnimeEmbed)

                userMangaEmbed = userManga(result)
                await ctx.send(embed=userMangaEmbed)

            except HTTPException:
                pass
        else:
            await ctx.send(embed=userError(userName))

    @commands.command(aliases=['STUDIO'])
    async def studio(self, ctx: commands.Context, *, studioName):
        embed = studioSearch(studioName)
        await ctx.send(embed=embed)

    @commands.command(aliases=['STAFF'])
    async def staff(self, ctx: commands.Context, *, staffName):
        embed = staffSearch(staffName)
        await ctx.send(embed=embed)

    @commands.command(aliases=["CHARACTER", 'char'])
    async def character(self, ctx: commands.Context, *, charName):
        embed = charSearch(charName)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(AniListApi(bot))
