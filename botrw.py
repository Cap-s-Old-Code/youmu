import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='y!')
@bot.async_event
async def on_ready():
    print ("██╗   ██╗ ██████╗ ██╗   ██╗███╗   ███╗██╗   ██╗    ██╗  ██╗ ██████╗ ███╗   ██╗██████╗  █████╗ ██╗  ██╗██╗   ██╗")
    print ("╚██╗ ██╔╝██╔═══██╗██║   ██║████╗ ████║██║   ██║    ██║ ██╔╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗██║ ██╔╝██║   ██║")
    print (" ╚████╔╝ ██║   ██║██║   ██║██╔████╔██║██║   ██║    █████╔╝ ██║   ██║██╔██╗ ██║██████╔╝███████║█████╔╝ ██║   ██║")
    print ("  ╚██╔╝  ██║   ██║██║   ██║██║╚██╔╝██║██║   ██║    ██╔═██╗ ██║   ██║██║╚██╗██║██╔═══╝ ██╔══██║██╔═██╗ ██║   ██║")
    print ("   ██║   ╚██████╔╝╚██████╔╝██║ ╚═╝ ██║╚██████╔╝    ██║  ██╗╚██████╔╝██║ ╚████║██║     ██║  ██║██║  ██╗╚██████╔╝")
    print ("   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ")
    print ("Youmu Konpaku Early Alpha Codename Espresso")
    print("Bot Name: {}".format(bot.user.name))
    print("Bot ID: {}".format(str(bot.user.id)))
    print("CMD Prefix: {}".format(bot.command_prefix))
    print("Bot is ready")