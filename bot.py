#YoumuBot 0.1
#Discord.py bot by Cappuchino

import json
import os
import logging
import datetime
import time
import traceback
import sys
import discord
import oauth
from discord import Forbidden, ConnectionClosed
from discord.ext import commands
from discord.opus import OpusError, OpusNotLoaded
from discord.ext.commands import CommandOnCooldown, CommandNotFound, NotOwner
import libneko
import logging
#here's the bot itbot = self
bot = commands.Bot(command_prefix='y!', owner_id=254542844197470209)
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
    print("Extensions and Cogs are below.")

#commands
@bot.command()
async def hello(ctx):
    """Hello World!"""
    await ctx.send("world")

@bot.command()
async def shinderu(ctx):
    """Omae wa mou shinderu."""
    await ctx.send("NANI!?")

@bot.command()
async def test(ctx):
    await ctx.send("Bot is online :traffic_light: ")

@bot.command()
async def foo(ctx):
    """foobar"""
    await ctx.send("bar")

@bot.command()
async def info(ctx):
    """Bot Info"""
    embed=discord.Embed(title="Youmu Konpaku", description="Shitty discord.py bot named after Cappuchino's waifu", color=0x37fb8a)
    embed.set_author(name="Cappuchino#1651", url="https://www.youtube.com/channel/UClyFkZBvh8itBGe3wE2z_gg?view_as=subscriber", icon_url="https://puu.sh/AgtVY/18f1c2ef1e.png")
    embed.set_thumbnail(url="https://puu.sh/AgtUF/c414e425ba.jpg")
    await ctx.send(embed=embed)



@bot.async_event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(InvalidCMD)


@bot.command()
async def say(ctx, *, message):
    """Makes bot say anything"""
    await ctx.send(message)

@commands.is_owner()
@bot.command()
async def shutdown(ctx, is_owner=True):
    """shuts down bot, only used by the one and only Mr.Cappuchino."""
    print ("""WARNING: BOT SHUT DOWN""")
    await ctx.send("""```BOT SHUTTING DOWN...```""")
    sys.exit()

@bot.command()
async def detail(ctx, *, member: discord.Member):
    """Displays Member info"""
    fmt = '{0} joined on {0.joined_at} and has {1} roles.'
    await ctx.send(fmt.format(member, len(member.roles)))
@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Invalid Member.')

@bot.command()
async def kick(ctx, *,is_owner=True, member: discord.Member):
    """Kicks someone (Currently only usable by Cappuchino)"""
    try:
     await ctx.kick(member)
    except:
            # Unable to kick
        await ctx.send("Unable to kick.")
        pass

async def ban(ctx, *,is_owner=True, member: discord.Member):
    """bans someone (Currently only usable by Cappuchino)"""
    try:
     await ctx.ban(member)
    except:
            # Unable to ban
        await ctx.send("Unable to ban.")
        pass
    
@bot.command()
async def dsay(ctx, *, message):
    """Repeats a message, then deletes the initial command."""
    try:
        await ctx.message.delete()
    finally:
        return await ctx.send(message)

class OwnerCog:

    def __init__(self, bot):
        self.bot = bot
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
if __name__ == '__main__':
        try:
            bot.load_extension('cogs.owner')
            bot.load_extension('cogs.members')
            bot.load_extension("cogs.Pt2")
            bot.load_extension("cogs.error_handler")
        except Exception as error:
            print('An Extension Failed to load.[{}]'.format(error))


token = ""
#Error Codes and shortcuts
InvalidCMD = ("```ERROR: Invalid Command. Please check syntax.```")
PlaceHolder = ("```ERROR: This command has been reserved and has not be implemented.```")
NotOwner = ("You're not Cappuchino, GTFO.")
#main stuff
bot.run(token)
