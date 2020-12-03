import discord
import random
import asyncio
import time
import func

class MyClient(discord.Client):
    # func.score = 0
    # func.tally = []
    # func.count()
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

# List of Games:
        if message.content.startswith(';list'):
            await message.channel.send('Here are the commands for currently available games: **;guess** (Guess a number, 1-10)  **;rps** (Rock, paper, scissors!) **;coin** (Coinflip) **;fight** (Fight against a bot)')

#Game 1: guessing game
        if message.content.startswith(';guess'):
            await message.channel.send('Guess a number between 1 and 10.')
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("Guessing Game!"))

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
                await client.change_presence(status=discord.Status.idle)
                # func.apend()
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))
                await client.change_presence(status=discord.Status.idle)
            # return func.score
# Game 2: rock paper scissors
        if message.content.startswith(';rps'):
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("Rock, Paper, Scissors Game!"))
            await message.channel.send('Rock, paper, scissors, **SHOOT!**')

            def checking_string(m):
                return m.author == message.author and type(m.content) == str

            cpu = random.randint(1,3)

            try:
                player = await self.wait_for('message', check=checking_string, timeout=8.0)  
                x = player.content.lower()
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long')
            #cpu plays rock
            if cpu == 1 and x == 'rock':
                await message.channel.send('CPU played **Rock** and you played **Rock. TIE**')
                await client.change_presence(status=discord.Status.idle)
            elif cpu == 1 and x == 'paper':
                await message.channel.send('CPU played **Rock** and you played **Paper. YOU WIN**')
                await client.change_presence(status=discord.Status.idle)
                # func.count()
                # func.apend()
                # await message.channel.send(f"Points = {func.score}")
            elif cpu == 1 and x == 'scissors':
                await message.channel.send('CPU played **Rock** and you played **Scissors. CPU WINS**')
                await client.change_presence(status=discord.Status.idle)
            #cpu plays paper
            if cpu == 2 and x == 'rock':
                await message.channel.send('CPU played **Paper** and you played **Rock. CPU WINS**')
                await client.change_presence(status=discord.Status.idle)
            elif cpu == 2 and x == 'paper':
                await message.channel.send('CPU played **Paper** and you played **Paper. TIE**')
                await client.change_presence(status=discord.Status.idle)
            elif cpu == 2 and x == 'scissors':
                await message.channel.send('CPU played **Paper** and you played **Scissors. YOU WIN**')
                await client.change_presence(status=discord.Status.idle)
                # func.count()
                # func.apend()
                # await message.channel.send(f"Points = {func.score}")
            #cpu plays scissors
            if cpu == 3 and x == 'rock':
                await message.channel.send('CPU played **Scissors** and you played **Rock. YOU WIN**')
                await client.change_presence(status=discord.Status.idle)
                # func.count()
                # func.apend()
                # await message.channel.send(f"Points = {func.score}")
            elif cpu == 3 and x == 'paper':
                await message.channel.send('CPU played **Scissors** and you played **Paper. CPU WINS**')
                await client.change_presence(status=discord.Status.idle)
            elif cpu == 3 and x == 'scissors':
                await message.channel.send('CPU played **Scissors** and you played **Scissors. TIE**')
                await client.change_presence(status=discord.Status.idle)


# Scoreboard :(
        # if message.content.startswith(';points'):
        #     await message.channel.send(f"Points = {func.score}")

# Game 3: Coinflip
        if message.content.startswith(';coin'):
            await message.channel.send('Heads or Tails?')
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("Coinflip!"))

            def flip(m):
                return m.author == message.author and type(m.content) == str

            coin = random.randint(1,2)

            try:
                player = await self.wait_for('message', check=flip, timeout=5.0)  
                x = player.content.lower()
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long')

            if coin == 1 and x == "heads":
                await message.channel.send('It was **Heads**! Nice guess!')
                await client.change_presence(status=discord.Status.idle)
                # func.count()
                # func.apend()
                # await message.channel.send(f"Points = {func.score}")
            elif coin == 1 and x == "tails":
                await message.channel.send('It was **Heads**... Nice try')
                await client.change_presence(status=discord.Status.idle)
            
            if coin == 2 and x == "heads":
                await message.channel.send('It was **Tails**... Nice try')
                await client.change_presence(status=discord.Status.idle)
            elif coin == 2 and x == "tails":
                await message.channel.send('It was **Tails**! Nice guess!')
                await client.change_presence(status=discord.Status.idle)
                # func.count()
                # func.apend()
                # await message.channel.send(f"Points = {func.score}")

# Game 4: Fight bot
        if message.content.startswith(';helpfight'):
            await message.channel.send('Each person has 100 hitpoints. A **punch** does 10-25 damage. **defend** reduces the next incoming damage by 1-10 damage. **prepare** will add 1-10 damage to your next punch. **run** if you are a loser.')
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("Noob learning how to fight a bot."))
        if message.content.startswith(';fight'):
            await message.channel.send('Welcome to the ring! Do you want to **punch**, **prepare** an attack, **defend**, or **run** away? OR type **;helpfight** if you are a noob.')
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("Fending off a bully..."))

            def action(m):
                return m.author == message.author and type(m.content) == str

            punch = random.randint(10,25)
            defend = random.randint(1,10)
            bm = random.randint(1,3)
            
            try:
                player = await self.wait_for('message', check=action, timeout=5.0)  
                x = player.content.lower()
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long and got stabbed...')
            
            # 1 = punch, 2 = defend, 3 = prepare
            if bm == 1:
                await message.channel.send(f'Bot punched for {punch} damage.')







            

            

client = MyClient()
client.run('Nzc4MDY1OTY4MzkxOTEzNDky.X7MkZg.9bhEvfqmNsp5OzdZixKzXmwtJLo')