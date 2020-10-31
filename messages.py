import discord
from commands import *

color = 0x3CB371

def lounge_created_message(channel):
    return discord.Embed(
        title='Woohoo!  :partying_face:',
        description=f'Your private lounge has been created.  Feel free to chillax in the {channel.mention} channel.  :sunglasses:',
        color=color
    )

def lounge_closed_message(owner):
    return discord.Embed(
        title='Lounge Closed',
        description=f'{owner.mention} , I have closed your lounge.',
        color=color
    )

def channel_created_message(channel_type, channel):
    return discord.Embed(
        title=f'{channel_type.title()} Channel Created',
        description=f'I have created a {channel_type} channel for you here, {channel.mention} .',
        color=color
    )

def channel_removed_message(channel_id):
    return discord.Embed(
        title='Channel Removed',
        description=f'I have removed the channel with the id of {channel_id} from your lounge.',
        color=color
    )

def invitation(owner, category, guild):
    return discord.Embed(
        title='Invitation To Lounge  :partying_face:',
        description=f'You have been invited to {owner.name}\'s private lounge ({category.name}) in the {guild.name} Server!',
        color=color
    )

def kick(owner, category, guild):
    return discord.Embed(
        title='You Have Been Kicked  :no_entry_sign:',
        description=f'You have been kicked from {owner.name}\'s private lounge ({category.name}) from the {guild.name} Server!',
        color=color
    )

def invite_confirm(description):
    return discord.Embed(
        title='Invitations Sent  :sunglasses:',
        description=description,
        color=color
    )

def kick_confirm(description):
    return discord.Embed(
        title='Kicks  :no_entry_sign:',
        description=description,
        color=color
    )

def already_own_lounge_error(channel):
    return discord.Embed(
        title='Sorry, No Can Do  :man_gesturing_no:',
        description=f'You already own a lounge, {channel.mention}.  Type `{close_lounge_command}` to close your lounge.',
        color=color
    )

def channel_not_exist_error(channel_id):
    return discord.Embed(
        title='Channel Doesn\'t Exist  :man_shrugging:',
        description=f'There is no channel in your lounge with the id of {channel_id}.',
        color=color
    )

not_lounge_owner_error = discord.Embed(
    title='Trying To Make A Lounge?  :man_shrugging:',
    description=f'You are not the owner of any lounge yet.  Type `{create_lounge_command}lounge_name` to create a lounge.',
    color=color
)
