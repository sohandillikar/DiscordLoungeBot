import discord
from messages import color
from commands import *

def help_command_message(member):
    message = discord.Embed(
        title='Lounge Bot Commands',
        description='Here is a list of all my commands',
        color=color
    )
    message.add_field(name='Command Prefix', value=f'`{command_prefix}`')
    message.add_field(name='Create Lounge', value=f'`{create_lounge_command}lounge_name`')
    message.add_field(name='Close Lounge', value=f'`{close_lounge_command}`')
    message.add_field(name='Add Text Channel', value=f'`{add_text_channel_command}channel_name`')
    message.add_field(name='Add Voice Channel', value=f'`{add_voice_channel_command}channel_name`')
    message.add_field(name='Remove Channel', value=f'`{remove_channel_command}channel_id`')
    message.add_field(name='Invite Member', value=f'`{invite_command}ping_member`\nExample :\n{invite_command}{member.mention}')
    message.add_field(name='Kick Member', value=f'`{kick_command}ping_member`\nExample :\n{kick_command}{member.mention}')
    return message
