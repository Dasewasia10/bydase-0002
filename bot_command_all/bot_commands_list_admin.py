import time

import aiofiles
import discord
import asyncio
import os
import sys

from discord.utils import get
from typing import Optional
from random import choice
from discord.ext import commands
from main import bot


def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)


class CommandsAdmin(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """Command untuk menyapa pendatang baru"""

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(877980286271496212)

        if not channel:
            return

        await channel.send(f":flag_id: Selamat datang, {member.mention}! Semoga hari-harimu sangat hebat!\n"
                           f":flag_gb: Welcome, {member.mention}! Hope your days will great!")
        await member.create_dm.send(member,
                                    f':flag_id: Selamat datang di Dase\'s Place! Semoga hari-harimu sangat hebat!\n'
                                    f':flag_gb: Welcome to Dase\'s Place! Hope your days will great!')

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        channel = self.bot.get_channel(863445778420334617)

        if not channel:
            return

        await channel.send(f":flag_id: Sayang sekali, {member.mention} telah meninggalkan kita.\n"
                           f":flag_gb: Too bad, {member.mention} has left us.")
        await member.create_dm.send(member, f':flag_id: Semoga kehidupanmu menjadi semakin baik!\n'
                                            f':flag_gb: Wish for your good fortune!')

    # ## Command khusus Admin

    @commands.command(aliases=['MATIKAN'])
    @commands.has_role(863645078635413524)
    @commands.cooldown(rate=1, per=30)
    async def matikan(self, ctx: commands.Context):
        """Hanya chat info ke penghuni Discord, bukan untuk mematikan bot"""
        await ctx.send("@everyone Bot kumatikan dulu.")

    @commands.command(aliases=['TEST'])
    @commands.has_role(863645350308872192)
    async def test(self, ctx: commands.Context):
        """Hanya chat mengetes bot apakah berfungsi dengan baik atau tidak"""
        await ctx.message.delete(delay=3)
        await ctx.send("Test berhasil!", delete_after=5)

    @commands.command(aliases=['WORD'])
    async def word(self, ctx: commands.Context):
        msg = ":flag_id:Kata-kata yang dideteksi oleh bot ByDase.\n:flag_gb:Words detected by the ByDase bot."
        with open('respon_and_answer/bad_word.txt', encoding="utf8") as file:
            bad_word = list(file.readline())
        with open('respon_and_answer/praise_word.txt', encoding="utf8") as file2:
            praise_word = list(file2.readline())
        some_bad = ""
        some_praise = ""
        for word in bad_word:
            some_bad += f"👉{word}\n"
        for word in praise_word:
            some_praise += f"👉{word}\n"
        else:
            embed = discord.Embed(title="Member on Dase's Place", description=msg,
                                  colour=discord.Colour.random())
            embed.add_field(name="Bad Word", value=some_bad, inline=True)
            embed.add_field(name="Bad Word", value=some_praise, inline=True)
            await ctx.author.send(embed=embed)

    """Kick a member for spamming."""

    @commands.command(aliases=['SHUTDOWN', 'sd'])
    @commands.has_role(863645078635413524)
    async def shutdown(self, ctx: commands.Context):
        await ctx.send('@everyone\nBot kumatikan dulu.\nShutting down the bot!')
        await self.bot.logout()

    @commands.command(aliases=['RESTART'])
    @commands.has_role(863645078635413524)
    async def restart(self, ctx: commands.Context):
        await ctx.send("Restarting bot...", delete_after=8)
        await self.bot.logout()
        restart_bot()

    @commands.command(aliases=['GIVEAWAY', 'ga', 'GA'])
    @commands.has_role(863645350308872192)
    async def giveaway(self, ctx: commands.Context, timeout: Optional[int] = 600, *, arg):
        emoji = "\N{HAPPY PERSON RAISING ONE HAND}"
        message = await ctx.send(arg)
        await message.add_reaction(emoji)
        await asyncio.sleep(timeout)
        message = await message.channel.fetch_message(message.id)
        reaction = get(message.reactions, emoji=emoji)
        users = [user async for user in reaction.users() if user.id != self.bot.user.id]
        await ctx.send(f"Congrats {choice(users).mention}")

    @commands.command(aliases=['KICK'])
    @commands.has_role(863645078635413524)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason):
        """Kick a member."""

        message = await ctx.send(f"Are you sure you want to kick @{member}?")
        await message.add_reaction("✅")
        await message.add_reaction("❌")

        check = lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"  # r=reaction, u=user

        try:
            reaction, user = await self.bot.wait_for("reaction_add", check=check, timeout=30)
        except asyncio.TimeoutError:
            await message.edit(content="Kick cancelled, timed out.")
            return

        if str(reaction.emoji) == "✅":
            await member.kick(reason=reason)
            await message.edit(content=f"@{member} has been kicked, because {reason}")
            return

        await message.edit(content="Kick cancelled.")

    @commands.command(aliases=['MUTE'])
    @commands.has_role(863645078635413524)
    async def mute(self, ctx, user: discord.Member):
        channel = self.bot.get_channel(876292626075242546)
        role = get(ctx.message.guild.roles, id=863647005356326912)
        await bot.remove_roles(user, role)
        await channel.send(f"{user} has been muted for 3 days.")
        time.sleep(259200)
        await bot.add_roles(user, role)
        await channel.send(f"{user} is already unmuted.")

    """Ban a member for spamming."""

    @commands.command(aliases=['BAN'])
    @commands.has_role(863645078635413524)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, arg):
        """Ban a member."""
        message = await ctx.send(f"Are you sure you want to ban @{member}?")
        await message.add_reaction("✅")
        await message.add_reaction("❌")

        check = lambda r, u: u == ctx.author and str(r.emoji) in "✅❌"  # r=reaction, u=user

        try:
            reaction, user = await self.bot.wait_for("reaction_add", check=check, timeout=30)
        except asyncio.TimeoutError:
            await message.edit(content="Ban cancelled, timed out.")
            return

        if str(reaction.emoji) == "✅":
            await member.ban()
            await message.edit(content=f"@{member} has been banned, because {arg}")
            # await channel.send(f"Banned @{member} from Dase's Place.")
            return

        await message.edit(content="Ban cancelled.")

    @commands.command(aliases=['UNBAN'])
    @commands.has_role(863645078635413524)
    async def unban(self, ctx: commands.Context, *, member):
        """Unban a member."""
        channel = self.bot.get_channel(876292869856559135)

        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await channel.send(f"Unbanned {user.name}#{user.discriminator} from Dase's Place."
                                   f"\nHe/She have to be invited again.")
                return

    @commands.command(aliases=['REACTROLE', 'rr', 'RR'])
    @commands.has_permissions(administrator=True, manage_roles=True)
    async def reactrole(self, ctx, role: discord.Role = None, msg: discord.Message = None, emoji=None):
        await ctx.message.delete(delay=2)

        if role is not None and msg is not None and emoji is not None:
            await msg.add_reaction(emoji)
            bot.reaction_roles.append((role.id, msg.id, str(emoji.encode("utf-8"))))

            async with aiofiles.open("reaction_roles.txt", mode="a") as file:
                emoji_utf = emoji.encode("utf-8")
                await file.write(f"{role.id} {msg.id} {emoji_utf}\n")

            await ctx.channel.send("Reaction has been set.", delete_after=3)

        else:
            await ctx.send("Invalid arguments.", delete_after=5)

    @commands.command(aliases=['SNIPE'])
    @commands.has_role(863645078635413524)
    async def snipe(self, ctx):
        try:
            contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]

        except:
            await ctx.channel.send("Couldn't find a message to snipe!")
            return

        embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in : #{channel_name}")

        await ctx.channel.send(embed=embed)

    # Command non-admin

    @commands.command(aliases=['APPLY'])
    async def apply(self, ctx: commands.Context, language):
        await ctx.message.delete(delay=3)
        if ctx.author.roles == get(ctx.message.guild.roles, id=863647005356326912):
            ctx.author.send("You already has the main role! Get another on the server!")
        else:
            embed = discord.Embed(description=":flag_id: Isi form kebenaran ini!"
                                              "\n:flag_gb: Fill this correctness form!", color=ctx.author.color)
            await ctx.author.send(embed=embed)  # Sends a message to the author

            data_member = f"data member/{ctx.author} - {language}.txt"
            yahallo = self.bot.get_channel(863445778420334613)

            answers = []  # Empty list as the user will input the answers

            def check(m):
                # Check that the messages were sent in DM by the right author
                return ctx.author == m.author and isinstance(m.channel, discord.DMChannel)

            if language == "en":
                questions1 = ["What\'s your name/alias?",
                              "What\'s your gender? (Male/Female)",
                              f"Are you willing to comply with the rules that apply here? (Please read on #{yahallo})"
                              ]  # Create your list of answers

                for i in questions1:
                    embed = discord.Embed(description=i, color=discord.Color.purple())
                    embed.set_footer(text=f"Answer this on 123 sec.")
                    await ctx.author.send(embed=embed)  # Sends the questions one after another
                    try:
                        msg = await bot.wait_for('message', timeout=123, check=check)
                    except asyncio.TimeoutError:
                        await ctx.author.send("Timeout message. Please type dt!apply again.")
                        return  # Will no longer proceed, user has to run the command again
                    else:
                        answers.append(msg)  # Appends the answers, proceed

                with open(data_member, "w", encoding="utf8") as file:
                    file.write(f"----Break Line----\n"
                               f"From : {ctx.author}\n"
                               f"{questions1[0]} - {answers[0].content}\n"
                               f"{questions1[1]} - {answers[1].content}\n"
                               f"{questions1[2]} - {answers[2].content}\n\n"
                               f"{ctx.author.name} joined in {ctx.author.joined_at}\n"
                               f"----Break Line----\n")

            elif language == "id":
                questions2 = ["Siapa nama/alias mu?",
                              "Apa gendermu? (Lelaki/Cewek)",
                              f"Apakah kamu akan bersedia mematuhi aturan yang berlaku di Dase's Place? (Silahkan "
                              f"baca di #{yahallo}) "
                              ]  # Membuat list jawaban berdasarkan pertanyaan

                for j in questions2:
                    embed = discord.Embed(description=j, color=discord.Color.purple())
                    embed.set_footer(text=f"Jawab dalam 123 detik.")
                    await ctx.author.send(embed=embed)  # Sends the questions one after another
                    try:
                        msg = await bot.wait_for('message', timeout=123, check=check)
                    except asyncio.TimeoutError:
                        await ctx.author.send("Waktu telah habis. Silahkan ketik dt!apply lagi.")
                        return  # Will no longer proceed, user has to run the command again
                    else:
                        answers.append(msg)  # Appends the answers, proceed

                with open(data_member, "w", encoding="utf8") as file:
                    file.write(f"----Batas----\n"
                               f"Dari : {ctx.author}\n"
                               f"{questions2[0]} - {answers[0].content}\n"
                               f"{questions2[1]} - {answers[1].content}\n"
                               f"{questions2[2]} - {answers[2].content}\n\n"
                               f"{ctx.author.name} masuk pada {ctx.author.joined_at}\n"
                               f"----Batas----\n")

            channel = bot.get_channel(876789180166967346)
            e = discord.Embed(color=ctx.author.color)
            e.title = f"Answered from {ctx.author} : {language}"
            e.description = f"1. {answers[0].content}\n" \
                            f"2. {answers[1].content}\n" \
                            f"3. {answers[2].content}\n" \
                            f"{ctx.author.name} joined in {ctx.author.joined_at}"
            await channel.send(embed=e)
            await ctx.author.add_roles(get(ctx.message.guild.roles, id=863647005356326912))
            await ctx.author.send("Now, cek #🔰get-your-role🔰 to get the role you want to.")

    @commands.command(aliases=['GIVEROLE'])
    @commands.has_role(863645350308872192)
    async def giverole(self, ctx: commands.Context, role: discord.Role, member: discord.Member):
        if role not in member.roles:
            await member.add_roles(role)
            await ctx.channel.send(content=f"{member.mention} now have {role.mention} role.")
            await ctx.author.send(f"Now, you have **{role.name}** role.")
        else:
            await ctx.author.send(f"You already has **{role.name}** role.")

    @commands.command(aliases=['REMOVEROLE'])
    @commands.has_role(863645350308872192)
    async def removerole(self, ctx: commands.Context, role: discord.Role, member: discord.Member):
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.channel.send(content=f"{member.mention} now not have {role.mention} role.")
            await ctx.author.send(f"Role **{role.name}** is already deleted from you.")
        else:
            await ctx.author.send(f"You are not have **{role.name}** role.")

    @commands.command(aliases=['CEKMEMBER'])
    @commands.has_role(863645350308872192)
    async def cekmember(self, ctx: commands.Context):
        some_member = ""
        role = get(ctx.guild.roles, id=863647005356326912)
        for member in ctx.guild.members:
            if role in member.roles:
                some_member += f"👉{member}\n"
        else:
            embed = discord.Embed(title="Member on Dase's Place", description=some_member,
                                  colour=discord.Colour.random())
            await ctx.author.send(embed=embed)

    @commands.command(aliases=['CEKBOT'])
    @commands.has_role(863645350308872192)
    async def cekbot(self, ctx: commands.Context):
        some_bot = ""
        role = get(ctx.guild.roles, id=863645640852897792)
        for member in ctx.guild.members:
            if role in member.roles:
                some_bot += f"👉{member}\n"
        else:
            embed = discord.Embed(title="Bot on Dase's Place", description=some_bot,
                                  colour=discord.Colour.random())
            await ctx.author.send(embed=embed)

    @commands.command(aliases=['ALLMEMBERS'])
    @commands.has_role(863645078635413524)
    async def allmembers(self, ctx: commands.Context):
        for guild in bot.guilds:
            all_guild = ""
            all_member = ""
            for member in guild.members:
                all_member += f":point_right:{member}\n"
                if str(guild) not in all_guild:
                    all_guild += f":point_right_tone1:{guild}\n"
            else:
                embed = discord.Embed(title="Member on all Discord Server, with the server itself",
                                      colour=discord.Colour.random())
                embed.add_field(name="Member", value=all_member, inline=True)
                embed.add_field(name="Guild", value=all_guild, inline=True)
                await ctx.author.send(embed=embed)

    @commands.command(aliases=['MESSAGEHISTORY', 'mh'])
    @commands.has_role(863645078635413524)
    async def messagehistory(self, ctx: commands.Context):
        filename = f"message history/{ctx.channel.name}.txt"
        with open(filename, "w", encoding="utf8") as file:
            async for msg in ctx.channel.history(limit=None):
                await ctx.channel.send("Success to create history channel txt", delete_after=5)
                file.write(f"{msg.created_at} - {msg.author.display_name}: {msg.clean_content}\n")


def setup(bot: commands.Bot):
    bot.add_cog(CommandsAdmin(bot))
