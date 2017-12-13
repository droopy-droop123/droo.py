from discord.ext import commands

class General:
    """General."""
    
    @commands.command()
    async def add(self, ctx, left : int, right : int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    @commands.command()
    async def repeat(ctx, times : int, content='repeating...'):
        """Repeats a message multiple times."""
        for i in range(times):
            await ctx.send(content)
def setup():
    bot.add_cog(General())
    
