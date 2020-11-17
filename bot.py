import discord
from discord.ext import commands

client = commands.Bot(command_prefix =  ';')
# bot = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready.")

client.run('Nzc4MDY1OTY4MzkxOTEzNDky.X7MkZg.9bhEvfqmNsp5OzdZixKzXmwtJLo')
# import discord
# import random
# import asyncio

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged in as')
#         print(self.user.name)
#         print(self.user.id)
#         print('------')

#     async def on_message(self, message):
#         # we do not want the bot to reply to itself
#         if message.author.id == self.user.id:
#             return

#         if message.content.startswith('$guess'):
#             await message.channel.send('Guess a number between 1 and 10.')

#             def is_correct(m):
#                 return m.author == message.author and m.content.isdigit()

#             answer = random.randint(1, 10)

#             try:
#                 guess = await self.wait_for('message', check=is_correct, timeout=5.0)
#             except asyncio.TimeoutError:
#                 return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

#             if int(guess.content) == answer:
#                 await message.channel.send('You are right!')
#             else:
#                 await message.channel.send('Oops. It is actually {}.'.format(answer))

# client = MyClient()





