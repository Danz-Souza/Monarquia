import random
from discord.ext import commands

bom_dia = ['Bom dia!', 'bom dia', '!bom dia', 'bdia']
bomdia_resposta = "Bom diaaa"

boa_tarde = ['Boa tarde!', 'Boa tarde', 'boa tarde', 'btarde', 'Btarde']
boatarde_resposta = "Boa taaarde"

boa_noite = ['Boa noite!', 'boa noite!', 'Boa noite', 'boa noite','bnoite', 'Bnoite', 'Good night']
boanoite_resposta = 'Boa nooooite'

class comprimentar(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() 
    async def on_message(self, message):
        msg = message.content   
        if any(word in msg for word in bom_dia):
            await message.channel.send(bomdia_resposta)
        if any(word in msg for word in boa_tarde):
            await message.channel.send(boatarde_resposta)
        if any(word in msg for word in boa_noite):
            await message.channel.send(boanoite_resposta)

def setup(bot):
    bot.add_cog(comprimentar(bot))