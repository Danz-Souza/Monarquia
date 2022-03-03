from discord.ext import commands
import random


class dados(commands.Cog):
    """Works with Cryptocurrency"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="d4")
    async def dado4(self, ctx):
        await ctx.send(f"A rolagem do d4 deu **{random.randint(1, 4)}**")
    
    @commands.command(name="d6")
    async def dado6(self, ctx):
        await ctx.send(f"A rolagem do d6 deu **{random.randint(1,6)}**")
    
    @commands.command(name="d8")
    async def dado6(self, ctx):
        await ctx.send(f"A rolagem do d8 deu **{random.randint(1,8)}**")

    @commands.command(name="d10")
    async def dado6(self, ctx):
        await ctx.send(f"A rolagem do d10 deu **{random.randint(1,10)}**")
        
    @commands.command(name="d12")
    async def dado6(self, ctx):
        await ctx.send(f"A rolagem do d12 deu **{random.randint(1,12)}**")
    
    @commands.command(name="d20")
    async def dado6(self, ctx):
        await ctx.send(f"A rolagem do d20 deu **{random.randint(1,20)}**")
                
def setup(bot):
    bot.add_cog(dados(bot))