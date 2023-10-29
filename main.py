import discord

from bot_mantik import gen_pass,emoji_olusturucu
from bot_token import token

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f' {client.user} olarak giriş yaptım.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('$sendmail'):
        await message.channel.send(gen_pass(4))

    elif message.content.startswith('$emoji'):
        await message.channel.send(emoji_olusturucu())
                                   
    else:
        await message.channel.send(message.content)
    
    

client.run(token)