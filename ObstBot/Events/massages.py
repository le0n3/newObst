import random
import discord
from discord.ext import commands
from discord.ext.commands import Cog


class on_Messages_Evenets(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad on_messags Events")

    @Cog.listener("on_message")
    async def christoph(self, message: discord.message):
        if message.content in "christoph" and message.guild:
            if message.author != self.bot.user:
                r = random.randint(1, 3)
                if r == 1:
                    await message.channel.send("Chillig Chillig Chillig", delete_after=40)

    @Cog.listener("on_message")
    async def LOL(self, message: discord.message):
        if message.content == "LOL" and message.guild:
            if message.author != self.bot.user:
                await message.channel.send("LOL !?!", delete_after=40)

    @Cog.listener("on_message")
    async def absimmung(self, message: discord.message):
        if message.channel == self.bot.get_channel(978181949636112405) and message.author != self.bot.user:
            x = '\U0000274C'
            check = '\U00002705'
            await message.add_reaction(x)
            await message.add_reaction(check)


async def setup(bot):
    print("Loading On messages ...")
    await bot.add_cog(on_Messages_Evenets(bot))