import asyncio
import discord
import Events.massages
import config
from ObstBotClass import ObstBot

bot = ObstBot()


@bot.event
async def on_raw_reaction_add(reaction: discord.RawReactionActionEvent):
    pass


async def load():
    await bot.load_extension("Cogs.random")


async def main():
    if __name__ == '__main__':
        await load()
        await bot.start(config.getBotKey())


asyncio.run(main())