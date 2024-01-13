import discord
from discord.ext import commands
from discord.ext.commands import Cog


class reaction_add_Evenets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad reaction_add Events")
    @Cog.listener("on_raw_reaction_add")
    async def added_reaction(self, reaction: discord.RawReactionActionEvent):
        ID= reaction.message_id
        message = await self.bot.get_channel(reaction.channel_id).fetch_message(ID)
        await message.channel.send("Reaction added")
        await self.client.process_commands(message)


async def setup(bot):
    print("Loading Reaction add ...")
    await bot.add_cog(reaction_add_Evenets(bot))
