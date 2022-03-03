import random
from discord.ext import commands

palavras_tristes = ['sad', 'triste', 'depressão', 'deprimido', 'ansioso', 'ansiedade', 'raiva', 'puto', 'F']

palavras_encorajadoras = ['Saia dessa amigo', 
        'Tenso em', 
        'Fique triste não',
        'To com depresaaaaaaaão', 
        "Que pena em, mas quem disse que isso é problema meu?",
        "Cada um com seus problemas"
        ]

class encorajabot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() 
    async def on_message(self, message):
        msg = message.content   
        if any(word in msg for word in palavras_tristes):
            await message.channel.send(random.choice(palavras_encorajadoras))

def setup(bot):
    bot.add_cog(encorajabot(bot))