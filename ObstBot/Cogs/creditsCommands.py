import discord
from discord.ext import commands
from ObstBot.DiscordeLogging import DLogging
from ObstBot.Datenbank import *

class Credits(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Lodad Credit Comands")

    @commands.command(brief='Ruft deine Credits ab', description='Holt die Aktuelle anzhal deiner Aktuellen Creits und gibt diese aus')
    async def MyCredits(self, ctx: discord.ext.commands.Context):
        CreditsCount: str = GetMyCredits(ctx.author)
        await ctx.message.delete()
        if not CreditsCount.startswith("Error: "):
            await ctx.send(CreditsCount, delete_after=15)
            await DLogging.Info(f"My Credits wurde von {ctx.author} ausgeführt",self.bot)
        else:
            await DLogging.Error(CreditsCount, self.bot)


    @commands.command(brief='Thop Three', description='Zeigt die Aktuellen Top 3')
    async def Top(self, ctx: discord.ext.commands.Context):
        mess = TopThree()
        await ctx.message.delete()
        await ctx.send(mess, delete_after=15)
        await DLogging.Info(f"Top Three wurde von {ctx.author} ausgeführt", self.bot)


async def setup(bot):
    print("Loading Credits Cog ...")
    await bot.add_cog(Credits(bot))
