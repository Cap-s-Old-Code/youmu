import discord
import time
from discord.ext import commands
class YoumuPt2:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pingpong(self, ctx):
        await ctx.send("ding dong")
        pass
    @staticmethod
    async def on_ready():
        print ("Part 2 Loaded Successfully")
    @commands.command()
    async def cogtest(self, ctx):
        await ctx.send("Cog is working correctly. Youmu Konpaku Pt.2")

    @commands.command()
    async def gf(self, ctx):
        await ctx.send("""#GF4Awx""")
   

def setup(bot):
    bot.add_cog(YoumuPt2(bot))