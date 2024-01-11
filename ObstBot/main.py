import asyncio
import discord
from discord.ext import commands
import config

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.event
async def on_raw_reaction_add(reaction: discord.RawReactionActionEvent):
    pass


async def load():
    await bot.load_extension("cogs.random")


async def main():
    if __name__ == '__main__':
        await load()
        await bot.start(config.getBotKey())


asyncio.run(main())