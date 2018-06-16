import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

import io
minutes = 0
hour = 2

Client = discord.Client()  
client = commands.Bot(command_prefix = "?") 



@client.event 
async def on_ready():
    print("Bot is online and connected to Discord")
    await client.change_presence(game=discord.Game(name="In KuedoxServer - https://discord.gg/QsHTZBS "))

@client.event
async def on_message(message):
    if message.content == "!help":
        await client.send_message(message.author, "**__:הפקודות בשרת__** \n \n  **!help** - שולח את פקודות השרת \n \n **!Channel** - שולח קישור לערוץ של קודוקס \n \n **!Shop** - שולח קישור לחנות של קודוקס \n \n **!inv** - שולח קישור להיכנס לשרת " )

    if message.content == "!Channel":
        await client.send_message(message.channel, "**__KuedoxChannel - __** https://www.youtube.com/channel/UCQS4XEIHjOuIwwOghvoBp5A")


    if message.content == "!Shop":
        await client.send_message(message.channel, "**My-Shop - ** https://sellfy.com/Kuedox")

    if message.content == "!inv":
        await client.send_message(message.channel, "**__InviteLink__** - https://discord.gg/QsHTZBS")

    if message.content == "אפשר באנר?":
        await client.send_message(message.channel, "תקנה.")
        
    if message.content == "קוודוקס":
        await client.send_message(message.channel, ":3?כן")



    if message.content.startswith('!user'):
      #  if message.author.role == "421580859729248267":
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]


            userembed = discord.Embed(
                title="Username",
                description=user.name,
                color=0xe67e22
            )
            userembed.set_author(
                name="User Info:"
            )
            userembed.add_field(
                name="Joined the server at:",
                value=userjoinedat

            )

            userembed.add_field(
                 name="User Created at:",
                 value=usercreatedat
            )
            userembed.add_field(
                name="Discord_TAG:",
                value=user.discriminator
            )
            userembed.add_field(
                name="User ID:",
                value=user.id
            )
                    
            await client.send_message(message.channel, embed=userembed)
        
     







        

client.run("NDIxMzk2ODc4MjIzOTk4OTc2.DYPcxg.oGDLmSvXR9kQr2fTQWrfYcySucQ") 
 

    
