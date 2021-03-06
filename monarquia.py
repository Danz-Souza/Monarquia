from private.config import TOKEN
import os

from discord.ext import commands

bot = commands.Bot("!")


def load_cogs(bot):
    bot.load_extension("manager")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"commands.{cog}")


load_cogs(bot)
bot.run(TOKEN)