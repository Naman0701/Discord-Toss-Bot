import discord
import random
import os

TOKEN=os.environ['TOKEN']

client=discord.Client()

@client.event
async def on_ready():
    print('Hi {0.user}'.format(client))

@client.event
async def on_message(message):
    uname=str(message.author).split('#')[0]
    user_message=str(message.content)
    channel=str(message.channel.name)
    print(f'{uname}:{user_message} {channel}')
    
    if message.author==client.user:
        return
    if message.channel.name=='toss':
        if user_message.lower()=='/toss':
            l=['heads','tails']
            num=random.randrange(1000)
            response=f'Result: {l[num%2]}'
            await message.channel.send(response)
            return

client.run(TOKEN)
