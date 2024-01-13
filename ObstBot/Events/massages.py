from discord.ext import commands
from discord.ext.commands import Cog


class on_Messages_Evenets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad on_messags Events")

    @Cog.listener("on_message")
    async def greet(self, message):
        Cheers = ["Hi", "hi", "Hello", "hello"]
        if message.content in Cheers:
            pass


async def setup(bot):
    print("Loading On messages ...")
    await bot.add_cog(on_Messages_Evenets(bot))
