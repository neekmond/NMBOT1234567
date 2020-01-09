import discord
from discord.ext import commands

client = discord.Client()

bot = commands.Bot(command_prefix='>')

@client.event()
async def ping(ctx):
    await ctx.send('pong')

access_token = os.environ["BOT_TOKEN"
client.run('access_token')
