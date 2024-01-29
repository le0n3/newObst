import asyncio
import discord
import Events.massages
import config
from ObstBotClass import ObstBot

bot = ObstBot()


async def load():
    await bot.load_extension("Cogs.randomCommands")
    await bot.load_extension("Cogs.zitateCommands")
    await bot.load_extension("Cogs.gameCommands")
    await bot.load_extension("Cogs.creditsCommands")

    await bot.load_extension("Events.massages")
    await bot.load_extension("Events.reactions")



async def main():
    if __name__ == '__main__':
        await load()
        await bot.start(config.getBotKey())


asyncio.run(main())