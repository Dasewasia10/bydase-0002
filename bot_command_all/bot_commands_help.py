import DiscordUtils
import discord
from datetime import datetime
from discord.ext import commands


class HelpCommands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """Command khusus fungsi help (d!help)"""

    @commands.command(name='help')
    @commands.cooldown(rate=1, per=30)
    async def help(self, ctx: commands.Context, arg1):
        # Di bawah adalah command untuk memanggil daftar command yang tersedia
        if arg1 == "list":
            embed = discord.Embed(title="list command",
                                  description=":flag_id:Daftar seluruh command yang tersedia.\n:flag_gb:List of all "
                                              "available command.",
                                  colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.add_field(name="help", value="help [id][en][all]", inline=False)
            # embed.add_field(name="Admin", value="[ban][kick]", inline=True)
            embed.add_field(name="Member", value="[hello][ping][minna][say]\n[motivation][poll]\n[gif][dm]",
                            inline=False)
            embed.add_field(name="Animanga", value="[user][anime][manga][reverse][studio][staff][character]",
                            inline=False)
            embed.add_field(name="Werewolf", value="[wcardlist][wend][wmod][wcard {card_name}]", inline=False)
            embed.add_field(name="other", value="[dm][dmid][dmen]", inline=False)
            embed.set_footer(text="d!help list", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)
        # Di bawah adalah command untuk memanggil fungsi help berdasarkan bahasa
        elif arg1 == "id":
            with open('bot_help_command/help_command_id.txt', 'r') as f:
                msg_id = f.read()
                embed = discord.Embed(title=f":flag_id: help id", description=msg_id, colour=0x87CEEB,
                                      timestamp=datetime.utcnow())
                embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
                embed.set_footer(text="d!help id",
                                 icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                await ctx.send(embed=embed)
        elif arg1 == "en":
            with open('bot_help_command/help_command_en.txt', 'r') as f:
                msg_en = f.read()
                embed = discord.Embed(title=f":flag_gb: help en", description=msg_en, colour=0x87CEEB,
                                      timestamp=datetime.utcnow())
                embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
                embed.set_footer(text="d!help en",
                                 icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                await ctx.send(embed=embed)
        # Di bawah adalah command untuk memanggil fungsi help secara keseluruhan
        elif arg1 == "all":
            with open('bot_help_command/help.txt', 'r') as f:
                msg1 = f.read()
            with open('bot_help_command/member.txt', 'r') as g:
                msg2 = g.read()
            with open('bot_help_command/anilist.txt', 'r') as h:
                msg3 = h.read()
            with open('bot_help_command/werewolf.txt', 'r') as i:
                msg4 = i.read()
            embed1 = discord.Embed(title=f"help", color=0x87CEEB, timestamp=datetime.utcnow()).add_field(
                name="Help command", value=msg1)
            embed1.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed1.set_footer(text="d!help all",
                              icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed2 = discord.Embed(title=f"help", color=0x87CEEB, timestamp=datetime.utcnow()).add_field(
                name="Member command", value=msg2)
            embed2.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed2.set_footer(text="d!help all",
                              icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed3 = discord.Embed(title=f"help", color=0x87CEEB, timestamp=datetime.utcnow()).add_field(
                name="Anilist command", value=msg3)
            embed3.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed3.set_footer(text="d!help all",
                              icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            embed4 = discord.Embed(title=f"help", color=0x87CEEB, timestamp=datetime.utcnow()).add_field(
                name="Werewolf command", value=msg3)
            embed4.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed4.set_footer(text="d!help all",
                              icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
            paginator.add_reaction('⏪', "back")
            paginator.add_reaction('⏩', "next")
            embeds = [embed1, embed2, embed3, embed4]
            await paginator.run(embeds)

        # Di bawah adalah command untuk memanggil fungsi help dengan penjelasan terinci per command
        elif arg1 == "hello" or arg1 == "h":
            msg = ":flag_id: Bot akan menyapamu.\n:flag_gb: Bot will greeting to you."
            embed = discord.Embed(title=f"hello", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="[d!hello][d!h]",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)
        elif arg1 == "ping":
            msg = ":flag_id: Mengecek ping milikmu saat ini.\n:flag_gb: Checking your own ping right now."
            embed = discord.Embed(title=f"ping", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!ping",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)
        elif arg1 == "say":
            msg = ":flag_id: Membuat ByDase mengucapkan kalimat yang kau ketik.\n:flag_gb: Make ByDase say the " \
                  "sentence you type. "
            embed = discord.Embed(title=f"say", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!say",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)
        elif arg1 == "minna":
            msg = ":flag_id: Menanyakan kabar seluruh penghuni server.\n:flag_gb: Ask for everyone's dispatch."
            embed = discord.Embed(title=f"minna", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!minna",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)
        elif arg1 == "motivation" or arg1 == "mot":
            msg = ":flag_id: Memberikanmu motivasi.\n:flag_gb: Giving you motivation."
            embed = discord.Embed(title=f"motivation", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="[d!motivation][d!mot]",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)
        elif arg1 == "poll":
            msg = ":flag_id: Membuat polling dengan mengetikkan pesan.\n:flag_gb: Create a poll by typing a message."
            embed = discord.Embed(title=f"motivation", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!poll",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)
        elif arg1 == "gif":
            msg = ":flag_id: ByDase ngasih gif random. Beri kata kunci tertentu untuk mendapatkan jenis gif yang " \
                  "diinginkan.\n" \
                  ":flag_gb: ByDase gives random gifs. Give certain keywords to get the desired type of gif."
            embed = discord.Embed(title=f"gif", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!gif {keyword}",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)
        elif arg1 == "dm":
            msg = ":flag_id: ByDase ngirimkan pesanmu via DM ke user tertentu.\n" \
                  ":flag_gb: ByDase sends your message via DM to a specific user."
            embed = discord.Embed(title=f"motivation", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="[d!motivation][d!mot]",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        # Di bawah adalah command untuk memanggil fungsi help dengan penjelasan terinci per command, khusus bagian
        # animanga
        elif arg1 == "aniuser":
            msg = ":flag_id: User yang berada dalam database Anilist." \
                  "\n:flag_gb: Users residing in the Anilist database."
            embed = discord.Embed(title=f"aniuser", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!aniuser",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg1 == "anime":
            msg = ":flag_id: Anime yang berada dalam database Anilist." \
                  "\n:flag_gb: Anime residing in the Anilist database."
            embed = discord.Embed(title=f"anime", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!anime",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg1 == "manga":
            msg = ":flag_id: Manga yang berada dalam database Anilist." \
                  "\n:flag_gb: Manga residing in the Anilist database."
            embed = discord.Embed(title=f"manga", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!manga",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg1 == "staff":
            msg = ":flag_id: Staff yang berada dalam database Anilist." \
                  "\n:flag_gb: Staff residing in the Anilist database."
            embed = discord.Embed(title=f"staff", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!staff",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg1 == "studio":
            msg = ":flag_id: Studio yang berada dalam database Anilist." \
                  "\n:flag_gb: Studios residing in the Anilist database."
            embed = discord.Embed(title=f"studio", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!studio",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg1 == "character":
            msg = ":flag_id: Karakter anime yang berada dalam database Anilist." \
                  "\n:flag_gb: Anime characters residing in the Anilist database."
            embed = discord.Embed(title=f"character", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!character",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        # Werewolf Command
        elif arg1 == "wcardlist":
            msg = ":flag_id:Daftar nama kartu yang tersedia pada game Werewolf versi Dase.\n" \
                  ":flag_gb:List of card names available in the Dase version of the Werewolf game."
            embed = discord.Embed(title=f"wcardlist", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!wcardlist",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg1 == "wend":
            msg = ":flag_id:Menyelesaikan game dan mencabut role yang diperuntukan kepada Narator/Moderator game." \
                  ":flag_gb:Complete the game and remove the role assigned to the Narrator/Moderator game."
            embed = discord.Embed(title=f"wend", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!wend",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg1 == "wmod":
            msg = ":flag_id:Melakukan polling untuk mendapatkan role yang diperuntukan kepada Narator/Moderator game." \
                  "\n:flag_gb:Conduct a poll to get the role assigned to the Narrator/Moderator game."
            embed = discord.Embed(title=f"wmod", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!wmod",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg1 == "wcard {card_name}":
            msg = ":flag_id:Narator/Moderator game memberikan kartu yang telah ditentukan kepada pemain." \
                  "\n:flag_gb:The Narrator/Moderator of the game gives the player a pre-determined card."
            embed = discord.Embed(title="wcard {card_name}", description=msg, colour=0x87CEEB,
                                  timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!wcard {card_name}",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        # Another command
        elif arg1 == "dm":
            with open('bot_help_command/help_command.txt', 'r') as f:
                msg = f.read()
            embed = discord.Embed(title=f"help", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!help all",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            channel = await ctx.author.create_dm()
            await channel.send(embed=embed)

        elif arg1 == "dmid":
            with open('bot_help_command/help_command_id.txt', 'r') as f:
                msg1 = f.read()
            embed = discord.Embed(title=f"help", description=msg1, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!help id",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            channel = await ctx.author.create_dm()
            await channel.send(embed=embed)

        elif arg1 == "dmen":
            with open('bot_help_command/help_command_en.txt', 'r') as g:
                msg2 = g.read()
            embed = discord.Embed(title=f"help", description=msg2, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!help en",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            channel = await ctx.author.create_dm()
            await channel.send(embed=embed)

        # Di bawah adalah command yang muncul ketika command yang dicari tidak ada
        else:
            await ctx.message.delete(delay=5)
            embed = discord.Embed(
                description=":flag_id:Maaf, fungsi tersebut tidak kami miliki! Silahkan masukkan kata yang "
                            "benar!\n:flag_gb:Sorry, we not have that help function! Please input the right word!",
                colour=0xd80000, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="Deleted in 10s",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed, delete_after=10)

    @commands.command(name='help_admin')
    @commands.cooldown(rate=1, per=30)
    async def help_admin(self, ctx: commands.Context, arg2):
        # Admin command (for Admin and Modder role only)
        # ## Admin only
        if arg2 == "self":
            with open('bot_help_command/admin.txt', 'r') as g:
                msg2 = g.read()
                embed = discord.Embed(title=f"help_admin", description=msg2, colour=0x87CEEB,
                                      timestamp=datetime.utcnow())
                embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
                embed.set_footer(text="d!help_admin self",
                                 icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
                channel = await ctx.author.create_dm()
                await channel.send(embed=embed)

        elif arg2 == "matikan":
            msg = ":flag_id:Hanya untuk mengumumkan kepada seluruh Member untuk mematikan bot." \
                  "\n:flag_gb:Just to announce to all Members to turn off the bot."
            embed = discord.Embed(title=f"matikan", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!matikan",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg2 == "shutdown":
            msg = ":flag_id:Mematikan bot." \
                  "\n:flag_gb:Turn off the bot."
            embed = discord.Embed(title=f"shutdown", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!shutdown",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg2 == "restart":
            msg = ":flag_id:Memulai kembali bot." \
                  "\n:flag_gb:Restart the bot."
            embed = discord.Embed(title=f"restart", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!restart",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg2 == "kick":
            msg = ":flag_id:Menendang Member dari server." \
                  "\n:flag_gb:Kick Member from the server."
            embed = discord.Embed(title=f"kick", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!kick",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg2 == "mute":
            msg = ":flag_id:Melakukan mute kepada Member selama 3 hari." \
                  "\n:flag_gb:Mute Member for 3 days."
            embed = discord.Embed(title=f"mute", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!mute",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg2 == "ban":
            msg = ":flag_id:Melakukan ban terhadap Member." \
                  "\n:flag_gb:Banning Member."
            embed = discord.Embed(title=f"ban", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!ban",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg2 == "unban":
            msg = ":flag_id:Melakukan unban terhadap Member." \
                  "\n:flag_gb:Unbanning Member."
            embed = discord.Embed(title=f"unban", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!unban",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg2 == "snipe":
            msg = ":flag_id:Mengecek pesan terakhir yang terhapus." \
                  "\n:flag_gb:Checks the last deleted message."
            embed = discord.Embed(title=f"snipe", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!snipe",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg2 == "allmembers":
            msg = ":flag_id:Mengecek semua pesan dan server yang terdapat bot ByDase di sana." \
                  "\n:flag_gb:Checks all messages and servers that have ByDase bots there."
            embed = discord.Embed(title=f"allmembers", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!allmembers",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg2 == "messagehistory":
            msg = ":flag_id:Menyimpan seluruh pesan pada suatu channel ke dalam file txt. Pesan tersimpan ke dalam " \
                  "folder [message history]." \
                  "\n:flag_gb:Save all messages on a channel into a txt file. Messages are stored in the [message " \
                  "history] folder. "
            embed = discord.Embed(title=f"messagehistory", description=msg, colour=0x87CEEB,
                                  timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!messagehistory",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

    @commands.command(name='help_modder')
    @commands.cooldown(rate=1, per=30)
    async def help_modder(self, ctx: commands.Context, arg3):
        # ## Modder can do too
        if arg3 == "self":
            with open('bot_help_command/admin.txt', 'r') as g:
                msg2 = g.read()
            embed = discord.Embed(title=f"help_modder", description=msg2, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!help_modder self",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            channel = await ctx.author.create_dm()
            await channel.send(embed=embed)

        elif arg3 == "test":
            msg = ":flag_id:Melakukan tes untuk mengecek bot ByDase aktif atau tidak." \
                  "\n:flag_gb:Do a test to check the ByDase bot is active or not."
            embed = discord.Embed(title=f"test", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!test",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg3 == "word":
            msg = ":flag_id:Kata-kata yang dideteksi oleh bot ByDase dalam versi buruk maupun yang diapresiasi." \
                  "\n:flag_gb:Words detected by the ByDase bot in both bad and appreciated versions."
            embed = discord.Embed(title=f"word", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!word",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg3 == "giveaway":
            msg = ":flag_id:Mengadakan giveaway." \
                  "\n:flag_gb:Hold a giveaway."
            embed = discord.Embed(title=f"giveaway", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!giveaway",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg3 == "reactrole":
            msg = ":flag_id:Mengatur sebuah pesan agar dapat dipasangkan reaction roles." \
                  "\n:flag_gb:Set up a message to be assigned reaction roles."
            embed = discord.Embed(title=f"reactrole", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!reactrole",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg3 == "apply":
            msg = ":flag_id:Command untuk memberikan pertanyaan kepada user baru yang ingin bergabung ke dalam server " \
                  "Dase\'s Place dan mendapatkan role Member. Data tersimpan ke dalam folder [data member]." \
                  "\n:flag_gb:Command to ask questions to new users who want to join the Dase\'s Place server and get " \
                  "the Member role. The data is stored in the [data member] folder."
            embed = discord.Embed(title=f"apply", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!apply",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg3 == "giverole":
            msg = ":flag_id:Command untuk memberikan role kepada user. Gunakan dengan bijak!" \
                  "\n:flag_gb:Command to assign a role to the user. Use wisely!"
            embed = discord.Embed(title=f"giverole", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!giverole",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg3 == "removerole":
            msg = ":flag_id:Command untuk melepaskan role kepada user. Gunakan dengan bijak!" \
                  "\n:flag_gb:Command to remove a role from the user. Use wisely!"
            embed = discord.Embed(title=f"removerole", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!removerole",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg3 == "cekmember":
            msg = ":flag_id:Mengetahui jumlah Member pada server Dase\'s Place." \
                  "\n:flag_gb:Knowing the number of Members on the Dase\'s Place server."
            embed = discord.Embed(title=f"cekmember", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!cekmember",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)

        elif arg3 == "cekbot":
            msg = ":flag_id:Mengetahui jumlah Utility pada server Dase\'s Place." \
                  "\n:flag_gb:Knowing the number of Utilities on the Dase\'s Place server."
            embed = discord.Embed(title=f"cekmember", description=msg, colour=0x87CEEB, timestamp=datetime.utcnow())
            embed.set_author(name="ByDase", icon_url="https://avatars.githubusercontent.com/u/77565642")
            embed.set_footer(text="d!cekmember",
                             icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(HelpCommands(bot))
