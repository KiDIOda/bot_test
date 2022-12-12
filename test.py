import discord
from discord.ext import commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>A<<")

bot.run('')