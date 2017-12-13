from discord.ext import commands

description = '''an example description, you can edit this'''

# this specifies what extensions to load when the bot starts up
startup_extensions = ["members", "rng", 'general', 'owner']

bot = commands.Bot(command_prefix='prefixgoeshere', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run('put your token here')
