import asyncio
import time
from random import choice
from typing import Optional

import discord
from discord.ext import commands
from discord.utils import get


class SimpleWerewolf(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.DaftarKartu_id = {
            "abstain": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Abstain.png?raw=true",
            "alpha werewolf": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Alpha%20Werewolf.png?raw=true",
            "apprentice seer": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Apprentice%20Seer.png?raw=true",
            "assassin": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Assassin.png?raw=true",
            "beholder": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Beholder.png?raw=true",
            "blabbermouth": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Blabbermouth.png?raw=true",
            "blacksmith": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Blacksmith.png?raw=true",
            "cultist hunter": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Cultist%20Hunter.png?raw=true",
            "cultist": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Cultist.png?raw=true",
            "cupid": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Cupid.png?raw=true",
            "cursed": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Cursed.png?raw=true",
            "detective": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Detective.png?raw=true",
            "diseased": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Diseased.png?raw=true",
            "doctor": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Doctor.png?raw=true",
            "doppleganger": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Doppleganger.png?raw=true",
            "drunk": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Drunk.png?raw=true",
            "executioner": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Executioner.png?raw=true",
            "fool": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Fool.png?raw=true",
            "guardian": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Guardian.png?raw=true",
            "halfblood": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/HalfBlood.png?raw=true",
            "hunter": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Hunter.png?raw=true",
            "little girl": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Little%20Girl.png?raw=true",
            "lonewolf": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Lonewolf.png?raw=true",
            "lover": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Lover.png?raw=true",
            "lycan": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Lycan.png?raw=true",
            "mason": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Mason.png?raw=true",
            "mayor": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Mayor.png?raw=true",
            "minion": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Minion.png?raw=true",
            "nostradamus": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Nostradamus.png?raw=true",
            "orphan": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Orphan.png?raw=true",
            "politican": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Politican.png?raw=true",
            "prince": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Prince.png?raw=true",
            "psycopath": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Psycopath.png?raw=true",
            "seer": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Seer.png?raw=true",
            "sheriff": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Sheriff.png?raw=true",
            "sorceser": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Sorceser.png?raw=true",
            "spellcaster": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Spellcaster.png?raw=true",
            "strong villager": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Strong%20Villager.png?raw=true",
            "thief": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Thief.png?raw=true",
            "tough guy": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Tough%20Guy.png?raw=true",
            "tradesman": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Tradesman.png?raw=true",
            "trickster": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Trickster.png?raw=true",
            "turner": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Turner.png?raw=true",
            "vampire": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Vampire.png?raw=true",
            "villager": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Villager.png?raw=true",
            "volunteer": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Volunteer.png?raw=true",
            "werewolf": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Werewolf.png?raw=true",
            "witch": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Witch.png?raw=true",
            "wolfcub": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Wolfcub.png?raw=true",
            "wolfman": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Wolfman.png?raw=true",
            "zombie": "https://github.com/Dasewasia10/bydase-0002/blob/main/Kartu%20Werewolf/Zombie.png?raw=true",
        }

    # ## Command dimulai dari sini

    @commands.command(aliases=['tw'])
    async def test_w(self, ctx):
        keyword = self.DaftarKartu_id
        await ctx.author.send(keyword)

    @commands.command(aliases=['WCARDLIST', 'wcl'])
    async def wcardlist(self, ctx, choose):
        title = "Kartu yang tersedia! | Available Card!"
        des = ":flag_id:Berikut daftar nama kartu yang tersedia pada game Werewolf versi Dase!\n" \
              ":flag_gb:The following is a list of card names available in the Dase version of the Werewolf game!"
        cardlist = list(self.DaftarKartu_id.keys())

        text = ""
        column_one_cardlist = cardlist[0:20]
        for w in column_one_cardlist:
            text += f"{w}\n"
        text2 = ""
        column_two_cardlist = cardlist[21:40]
        for x in column_two_cardlist:
            text2 += f"{x}\n"
        text3 = ""
        column_three_cardlist = cardlist[41:50]
        for y in column_three_cardlist:
            text3 += f"{y}\n"

        else:
            embed = discord.Embed(title=title, description=des, colour=discord.Colour.random())
            embed.add_field(name="Card 1", value=text, inline=True)
            embed.add_field(name="Card 2", value=text2, inline=True)
            embed.add_field(name="Card 3", value=text3, inline=True)
            embed.set_footer(text='Read it carefully ^-^. Run d!wdc {card_name} for details of each card. (Function '
                                  'come soon)')
            if choose == "here":
                await ctx.send(embed=embed)
            elif choose == "dm":
                await ctx.author.send(embed=embed)

    @commands.command(aliases=['WEND'])
    @commands.has_permissions(administrator=True)
    async def wend(self, ctx: commands.Context, member: discord.Member):
        role = get(member.guild.roles, name="The Narrator")
        await member.remove_roles(role)
        await ctx.author.send(f"Role {role.mention} is already deleted from you.")

    @commands.command(aliases=['WMOD'])
    async def wmod(self, ctx: commands.Context, timeout: Optional[int] = 10):
        emoji = "\N{Smiling Face with Sunglasses}"
        arg = ":flag_id:Pemilihan Narator!\n:flag_gb:Narrator Election!"
        embed = discord.Embed(description=arg)
        member = discord.Member

        msg = await ctx.send(embed=embed)
        await msg.add_reaction(emoji)
        await asyncio.sleep(timeout)
        message = await msg.channel.fetch_message(msg.id)
        reaction = get(message.reactions, emoji=emoji)
        users = [user async for user in reaction.users() if user.id != self.bot.user.id]
        role = get(choice(users).guild.roles, name="The Narrator")
        await ctx.send(f"Congrats {choice(users).mention}. I'll give you the {role.mention} role.")
        await member.add_roles(choice(users), role)

        time.sleep(18000)
        if role in choice(users):
            await member.remove_roles(choice(users), role)
        elif role not in choice(users):
            await ctx.channel.send(f"{choice(users)} is not has this role anymore.")

    @commands.command(aliases=['WCARD'])
    @commands.has_role("The Narrator")
    # This command will delivered a card by it name
    async def wcard(self, ctx, member: discord.Member, *, card):
        keyword = self.DaftarKartu_id
        if card.lower() not in keyword:
            embed = discord.Embed(description=":flag_id:Ketik nama yang benar.\n:flag_gb:Type the right card name.")
            await ctx.channel.send(embed=embed, delete_after=5)
        else:
            # picture = discord.File(keyword.get(card))
            embed = discord.Embed(description=":flag_id:Kartu telah dikirim.\n:flag_gb:Card has been delivered.")
            embed.set_footer(text='5 seconds...')
            await ctx.channel.send(embed=embed, delete_after=5)
            dm = await member.create_dm()
            await dm.send(keyword.get(card))


def setup(bot: commands.Bot):
    bot.add_cog(SimpleWerewolf(bot))
