import discord
import random
import os

# TOKEN=os.environ['TOKEN']
TOKEN='OTgwNTQ0Nzg0Mzc0NTY3MDEy.G3HrQA.wU5Om8fxEE5WUb94pp3e98upXbR5mPuRPDsIAY'
client=discord.Client()

ol=['Bind','Split','Breeze','Fracture','Haven','Icebox','Ascent']
l=ol.copy()
            
@client.event
async def on_ready():
    print('Hi {0.user}'.format(client))

@client.event
async def on_message(message):
    n=['1','2','3','4','5','6','7']
    uname=str(message.author).split('#')[0]
    user_message=str(message.content)
    channel=str(message.channel.name)
    print(f'{uname}:{user_message} {channel}')
    global l,ol
    
    if message.author==client.user:
        return
    if message.channel.name=='toss':
        if user_message.lower()=='/toss':
            tt=['heads','tails']
            num=random.randrange(1000)
            response=f'Result: {tt[num%2]}'
            await message.channel.send(response)
            return
        if user_message.lower()=='/reset':
            l=[]
            l=ol.copy()
            await message.channel.send('MAP RESET')
            return
        if user_message.lower()=='/map':
            maps=''
            for i in range(len(l)):
                maps+=str(i+1)+'.'+l[i]+'  '
            await message.channel.send(maps)
        if user_message in n:
            print(int(user_message)-1)
            print(l[int(user_message)-1])
            l.pop(int(user_message)-1)
            if len(l)==3:
                res=random.randint(0,2)
                await message.channel.send('THE RANDOM MAP IS : '+l[res])
                return
            maps=''
            for i in range(len(l)):
                maps+=str(i+1)+'.'+l[i]+'  '
            await message.channel.send(maps)
            return
            
            return
            
            

client.run(TOKEN)
