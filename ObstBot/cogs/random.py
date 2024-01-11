import discord
from discord.ext import commands


class Random(commands.Cog):
    def __init__(self,bot):
        self.bot: commands.Bot = bot
        self.guild: discord.Guild = bot.get_guild(1108113142564794528)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad Random Comands")

    @commands.command(brief='Nächster Boss', description='Zeigt den Genauen Zeitraum bis zum Nächsten Boss an')
    async def next(self,ctx: discord.ext.commands.Context):
        await ctx.message.delete()


async def setup(bot):
    print("Loading Random Cog ...")
    await bot.add_cog(Random(bot))

