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
            await message.channel.send('Hello again')
            await self.client.process_commands(message)

    @Cog.listener("on_message")
    async def agree(self, message):
        Agree = ["yes", "yep", "ok"]
        if message.content in Agree:
            await message.channel.send('good')
            await self.client.process_commands(message)


async def setup(bot):
    print("Loading On messages ...")
    await bot.add_cog(on_Messages_Evenets(bot))
