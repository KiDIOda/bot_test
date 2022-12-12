import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>A<<")

bot.run('MTA0OTY2NzYwNzYyOTk0Mjg0NA.GhqyCE.tC1CZvoOwdfFO5H2w12GKFuPC5-96X4cwLpSpQ')