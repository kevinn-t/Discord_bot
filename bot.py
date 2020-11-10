import discord
from discord.ext import commands

client = commands.Bot(command_prefix =  '.')

@client.event
async def on_ready():
    print("Bot is ready.")
    
client.run("Nzc1NTI5MTA0Njg1OTI0MzUz.X6npww.AnFpJ1dV6lGYjM95EE_WR_bO38Q")



