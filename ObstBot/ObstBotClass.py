import discord
from discord.ext import commands
import logging
import logging.handlers

class ObstBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        logger = logging.getLogger('discord')
        logger.setLevel(logging.INFO)

        handler = logging.handlers.RotatingFileHandler(
            filename='ObstBot/Log/discord.log',
            encoding='utf-8',
            maxBytes=16 * 1024,  # 32 MiB
            backupCount=5,  # Rotate through 5 files
        )

        dt_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        super().__init__(command_prefix=commands.when_mentioned_or('/'), intents=intents, case_insensitive=True)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('-----------------------------------------------')