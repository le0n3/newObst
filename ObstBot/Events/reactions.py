import discord
from discord.ext import commands
from discord.ext.commands import Cog
from ObstBot.Datenbank import SocialCreditEdit
from ObstBot.DiscordeLogging import DLogging


class reaction_add_Evenets(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad reaction_add Events")

    @Cog.listener("on_raw_reaction_add")
    async def added_reaction(self, reaction: discord.RawReactionActionEvent):
        chanel: discord.TextChannel = self.bot.get_channel(reaction.channel_id)
        message:discord.Message = await chanel.fetch_message(reaction.message_id)
        print(reaction.emoji.name)

        if chanel.guild:
            if reaction.emoji.name == 'socialCredit_p':
                SocialCreditEdit(message.author, 10)
                await DLogging.Info(f"{message.author.name} hast +10 Credits bekommen von {reaction.member.name}", self.bot)

            elif reaction.emoji.name == 'socialCredit_n':
                SocialCreditEdit(message.author, -10)
                await DLogging.Info(f"{message.author.name} hast -10 Credits bekommen von {reaction.member.name}",self.bot)


async def setup(bot):
    print("Loading Reaction add ...")
    await bot.add_cog(reaction_add_Evenets(bot))
