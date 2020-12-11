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
            await message.channel.send('Here are the commands for currently available games: **;guess** (Guess a number, 1-10)  **;rps** (Rock, paper, scissors!) **;coin** (Coinflip) **;fight** (Fight against a bot). ')
            await message.channel.send('If you are feeling sad, type ;sad...we hope these will cheer you up! ;(')

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
        # ppunch = random.randint(10,25)
        # bpunch = random.randint(10,25)
        # pdefend = random.randint(1,10)
        # bdefend = random.randint(1,10)
        # pprepare = random.randint(1,10)
        # bprepare = random.randint(1,10)
        # bm = random.randint(1,3)
        phealth = 100
        bhealth = 100
        RunGame = True 
        # pdef = False
        # bdef = False
        # pprep = False
        # bprep = False
        if message.content.startswith(';helpfight'):
            await message.channel.send('Each person has 100 hitpoints. A **punch** does 10-25 damage. **defend** reduces the next incoming damage by 1-10 damage. **prepare** will add 1-10 damage to your next punch but does not stack. And if you do not want to fight anymore, just wait to get stabbed.')
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("Noob learning how to fight a bot."))
        if message.content.startswith(';fight'):
            await message.channel.send('Welcome to the ring! Do you want to **punch**, **prepare** an attack, or **defend**? OR type **;helpfight** if you are a noob.')
            await client.change_presence(status=discord.Status.idle, activity=discord.Game("Fending off a bully..."))

            def action(m):
                return m.author == message.author and type(m.content) == str
            while RunGame == True:
                try:
                    player = await self.wait_for('message', check=action, timeout=10.0)  
                    p = player.content.lower()
                    await message.channel.send("Your move!")
                except asyncio.TimeoutError:
                    return await message.channel.send('Sorry, you took too long and got stabbed...')

                # Player Punch
                # 1 = punch, 2 = defend, 3 = prepare
                bm = random.randint(1,3)
                if p == "punch" and bm == 1:
                    ppunch = random.randint(10,25)
                    bpunch = random.randint(10,25)
                    await message.channel.send(f'**You punched** for {ppunch} damage.')
                    bhealth -= ppunch
                    await message.channel.send(f'Minigame health: {bhealth}')
                    await message.channel.send(f'**Minigames punched** for {bpunch} damage.Your move!')
                    phealth -= bpunch
                    await message.channel.send(f'Your health: {phealth}')
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                    if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')
                elif p == 'defend' and bm == 1:
                    bpunch = random.randint(10,25)
                    pdefend = random.randint(1,10)
                    await message.channel.send(f'**You defend.** Next time you get hit, you will take reduced damage.')
                    await message.channel.send(f'**Minigames punches.** Instead of taking {bpunch} damage, you now take {bpunch - pdefend}. Your move!')
                    phealth -= (bpunch - pdefend)
                    await message.channel.send(f'Your health: {phealth}')
                    if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')
                elif p == "prepare" and bm == 1:
                    bpunch = random.randint(10,25)
                    pprepare = random.randint(1,10)
                    await message.channel.send(f'**You** decide to **prepare** an attack. Your next punch will do {pprepare} extra damage!')
                    await message.channel.send(f'**Minigames punches.** You take {bpunch} damage. Your move!')
                    phealth -= bpunch
                    await message.channel.send(f'Your health: {phealth}')
                    pprep = True
                    if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')
                elif p == "punch" and bm == 2:
                    ppunch = random.randint(10,25)
                    bdefend = random.randint(1,10)
                    await message.channel.send(f'**You punched** for {ppunch} damage.')
                    await message.channel.send(f'**Minigames defends.** Instead of taking {ppunch} damage, bot now takes {ppunch - bdefend}. Your move!')
                    bhealth -= (ppunch - bdefend)
                    await message.channel.send(f'Minigame health: {bhealth}')
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                elif p == "defend" and bm == 2:
                    await message.channel.send(f'**You defend.** Next time you get hit, you will take reduced damage.')
                    await message.channel.send(f'**Minigames defends.** It will take reduced damage.')
                    bdef = True
                    pdef = True
                elif p == "prepare" and bm == 2:
                    await message.channel.send(f'**You** decide to **prepare** an attack. Your next punch will do {pprepare} extra damage!')
                    await message.channel.send(f'**Minigames defends.** It will take reduced damage from your next punch. Your move!')
                    pprep = True
                    bdef = True
                    
                elif p == "punch" and bm == 3:
                    ppunch = random.randint(10,25)
                    bprepare = random.randint(1,10)
                    await message.channel.send(f'**You punched** for {ppunch} damage.')
                    bhealth -= ppunch
                    await message.channel.send(f'Minigame health: {bhealth}')
                    bprep = True
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                    await message.channel.send(f'**Minigames** decides to **prepare** an attack. His next punch will do {bprepare} extra damage! Your move!')
                elif p == "defend" and bm == 3:
                    pdefend = random.randint(1,10)
                    bprepare = random.randint(1,10)
                    await message.channel.send(f'**You defend.** Next time you get hit, you will take reduced damage.')
                    await message.channel.send(f'**Minigames** decides to **prepare** an attack. His next punch will do {bprepare} extra damage! Your move!')
                    bprep = True
                    pdef = True
                elif p == "prepare" and bm == 3:
                    pprepare = random.randint(1,10)
                    bprepare = random.randint(1,10)
                    await message.channel.send(f'**You** decide to **prepare** an attack. Your next punch will do {pprepare} extra damage!')
                    await message.channel.send(f'**Minigames** decides to **prepare** an attack. His next punch will do {bprepare} extra damage! Your move!')
                    pprep = True
                    bprep = True

                #bot is preped
                elif p == "punch" and bm == 1 and bprep == True:
                    ppunch = random.randint(10,25)
                    bpunch = random.randint(10,25)
                    bprepare = random.randint(1,10)
                    await message.channel.send(f'**You punched** for {ppunch} damage.')
                    bhealth -= ppunch
                    await message.channel.send(f'Minigame health: {bhealth}')
                    await message.channel.send(f'**Minigames punched**, landing a critical for {bpunch} + {bprepare} damage.Your move!')
                    phealth -= (bpunch + bprepare)
                    await message.channel.send(f'Your health: {phealth}')
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                    if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')
                elif p == 'defend' and bm == 1 and bprep == True:
                   pdefend = random.randint(1,10)
                   bpunch = random.randint(10,25)
                   bprepare = random.randint(1,10)
                   await message.channel.send(f'**You defend.** Next time you get hit, you will take {pdefend} reduced damage.')
                   await message.channel.send(f'**Minigames punches.** Instead of taking {bpunch} damage, you now take {bpunch} + {bprepare} - {pdefend}. Your move!')
                   phealth -= (bpunch + bprepare) - pdefend
                   await message.channel.send(f'Your health: {phealth}')
                   if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')
                elif p == "prepare" and bm == 1 and bprep == True:
                   pprepare = random.randint(1,10)
                   bpunch = random.randint(10,25)
                   bprepare = random.randint(1,10)
                   await message.channel.send(f'**You** decide to **prepare** an attack. Your next punch will do {pprepare} extra damage!')
                   await message.channel.send(f'**Minigames punches.** You take {bpunch} + {bprepare} damage. Your move!')
                   phealth -= (bpunch + bprepare)
                   await message.channel.send(f'Your health: {phealth}')
                   pprep = True
                   if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')
                elif p == "punch" and bm == 1 and bprep == True and pprep == True:
                    ppunch = random.randint(10,25)
                    bpunch = random.randint(10,25)
                    bprepare = random.randint(1,10)
                    pprepare = random.randint(1,10)
                    await message.channel.send(f'**You punched** for {ppunch + pprepare} damage.')
                    bhealth -= (pprepare + ppunch)
                    await message.channel.send(f'Minigame health: {bhealth}')
                    await message.channel.send(f'**Minigames punched** landed a critical for {bpunch} + {bprepare} damage.Your move!')
                    phealth -= (bpunch + bprepare)
                    await message.channel.send(f'Your health: {phealth}')
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                    if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')

                #player is prepped
                elif p == "punch" and bm == 1 and pprep == True:
                    ppunch = random.randint(10,25)
                    bpunch = random.randint(10,25)
                    pprepare = random.randint(1,10)
                    await message.channel.send(f'**You punched** for {ppunch} + {pprepare} damage.')
                    bhealth -= (ppunch + pprepare)
                    await message.channel.send(f'Minigame health: {bhealth}')
                    await message.channel.send(f'**Minigames punched** for {bpunch} damage.Your move!')
                    phealth -= bpunch
                    await message.channel.send(f'Your health: {phealth}')
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                    if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')
                elif p == "punch" and bm == 2 and pprep == True:
                    ppunch = random.randint(10,25)
                    bdefend = random.randint(1,10)
                    pprepare = random.randint(1,10)
                    await message.channel.send(f'**You punched** for {ppunch} + {pprepare} damage.')
                    await message.channel.send(f'**Minigames defends.** Instead of taking {ppunch} + {pprepare} damage, bot now takes {(ppunch + pprepare) - bdefend}. Your move!')
                    bhealth -= (pprepare + ppunch) - bdefend
                    await message.channel.send(f'Minigame health: {bhealth}')
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                elif p == "punch" and bm == 3 and pprep == True:
                    ppunch = random.randint(10,25)
                    pprepare = random.randint(1,10)
                    bprepare = random.randint(1,10)
                    await message.channel.send(f'**You punched** for {ppunch} + {pprepare} damage.')
                    bhealth -= (pprepare + ppunch)
                    await message.channel.send(f'Minigame health: {bhealth}')
                    await message.channel.send(f'**Minigames** decides to **prepare** an attack. His next punch will do {bprepare} extra damage! Your move!')
                    pprep = False
                    bprep = True
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                
                #bot is defending
                elif p == 'punch' and bdef == True:
                    ppunch = random.randint(10,25)
                    bdefend = random.randint(1,10)
                    await message.channel.send(f'**Minigames was defending** this whole time! **Your attack** was supposed to hit for {ppunch} but instead dealt {ppunch} - {bdefend}.')
                    bhealth -= (ppunch - bdefend)
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                    bdef = False
                elif p == 'punch' and pprep == True and bdef == True:
                    pprepare = random.randint(1,10)
                    ppunch = random.randint(10,25)
                    bdefend = random.randint(1,10)
                    await message.channel.send(f'**Minigames was defending** this whole time! **Your attack** was supposed to hit for a critical of {ppunch} + {pprepare} but instead dealt {ppunch + pprepare} - {bdefend}.')
                    bhealth -= (ppunch + pprepare) - bdefend
                    await message.channel.send(f'Minigame health: {bhealth}')
                    if bhealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU WIN!**')
                    bdef = False
                #player is defending
                elif bm == 1 and pdef == True:
                    bpunch = random.randint(10,25)
                    pdefend = random.randint(1,10)
                    await message.channel.send(f'**Minigames punches.** Instead of taking {bpunch} damage, you now take {bpunch} - {pdefend}. Your move!')
                    phealth -= (bpunch - pdefend)
                    if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')
                    pdef = False
                elif bm == 1 and bprep == True and pdef == True:
                    bprepare = random.randint(1,10)
                    bpunch = random.randint(10,25)
                    pdefend = random.randint(1,10)
                    await message.channel.send(f'**Minigames punches.** Instead of taking {bpunch} damage, you now take {bpunch} + {bprepare} - {pdefend}. Your move!')
                    phealth -= (bpunch + bprepare) - pdefend
                    await message.channel.send(f'Minigame health: {bhealth}')
                    if phealth < 0:
                        RunGame = False
                        pprep = False
                        bprep = False
                        bdef = False
                        pdef = False
                        await message.channel.send('**YOU LOSE!**')
                    pdef = False

        #heppi
        if message.content.startswith(';sad'):
            happystuff = ['https://www.youtube.com/watch?v=44gylLm2CnA', 'https://www.youtube.com/watch?v=pOeig6_aAtE', 'https://www.youtube.com/watch?v=q2tsdfRhtew', 'https://www.youtube.com/watch?v=DJfg39WkMvE', 'https://www.youtube.com/watch?v=AL1q-zZWViM', 'https://www.youtube.com/watch?v=-LWo7DEzbpM']
            await message.channel.send(random.choice(happystuff))




client = MyClient()
client.run('Nzc4MDY1OTY4MzkxOTEzNDky.X7MkZg.9bhEvfqmNsp5OzdZixKzXmwtJLo')