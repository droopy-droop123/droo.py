import random
from discord.ext import commands

class RNG:
    """Some random cog."""
    
    @commands.command()
    async def roll(self, ctx, dice : str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def choose(self, ctx, *choices : str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))


def setup(bot):
    bot.add_cog(RNG())
