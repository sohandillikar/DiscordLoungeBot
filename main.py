import discord
from commands import *
from messages import *
from lounge import *
from help_command import help_command_message

token = 'YOUR_BOT_TOKEN_HERE'
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=help_command))

@client.event
async def on_message(message):
    if not message.author.bot:
        if message.author in [lounge.owner for lounge in lounges]:
            lounge = [lounge for lounge in lounges if message.author == lounge.owner][0]
        else:
            lounge = None
        if message.content.startswith(create_lounge_command) and len(message.content.replace(create_lounge_command, '')) >= 1:
            if not lounge is None:
                await message.channel.send(embed=already_own_lounge_error(lounge.text_channels[0]))
            else:
                await Lounge(message.author, message.content.replace(create_lounge_command, ''), message.channel, message.guild).create_lounge()
        elif not lounge is None:
            if message.content == close_lounge_command:
                await lounge.close_lounge()
            elif message.content.startswith(add_text_channel_command) and len(message.content.replace(add_text_channel_command, '')) >= 1:
                await lounge.add_channel('text', message.content.replace(add_text_channel_command, ''), message.channel)
            elif message.content.startswith(add_voice_channel_command) and len(message.content.replace(add_voice_channel_command, '')) >= 1:
                await lounge.add_channel('voice', message.content.replace(add_voice_channel_command, ''), message.channel)
            elif message.content.startswith(remove_channel_command) and len(message.content.replace(remove_channel_command, '')) >= 1:
                await lounge.remove_channel(message.content.replace(remove_channel_command, ''), message.channel)
            elif message.content.startswith(invite_command) and len(message.content.replace(invite_command, '')) >= 1:
                await lounge.invite(message.mentions, message.channel)
            elif message.content.startswith(kick_command) and len(message.content.replace(kick_command, '')) >= 1:
                await lounge.kick(message.mentions, message.channel)
        elif message.content == help_command:
            await message.channel.send(embed=help_command_message(client.user))
        elif message.content.startswith(command_prefix):
            await message.channel.send(embed=not_lounge_owner_error)

client.run(token)
