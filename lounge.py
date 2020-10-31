import discord
from messages import *

lounges = []

class Lounge:
    def __init__(self, owner, category_name, channel, guild):
        self.owner = owner
        self.category_name = category_name
        self.channel = channel
        self.guild = guild
        self.members = [self.owner]
        self.text_channels, self.voice_channels = [], []

    async def create_lounge(self):
        lounges.append(self)
        self.role = await self.guild.create_role(name=self.category_name)
        overwrites = {
            self.guild.default_role : discord.PermissionOverwrite(read_messages=False, send_messages=False),
            self.role : discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        self.category = await self.guild.create_category_channel(self.category_name, overwrites=overwrites)
        self.text_channels.append(await self.category.create_text_channel('general'))
        self.voice_channels.append(await self.category.create_voice_channel('meeting-room'))
        await self.owner.add_roles(self.role)
        await self.channel.send(embed=lounge_created_message(self.text_channels[0]))

    async def close_lounge(self):
        [await channel.delete() for channel in self.text_channels]
        [await channel.delete() for channel in self.voice_channels]
        await self.category.delete()
        await self.role.delete()
        lounges.remove(self)
        await self.channel.send(embed=lounge_closed_message(self.owner))

    async def add_channel(self, channel_type, channel_name, channel):
        if channel_type == 'text':
            self.text_channels.append(await self.category.create_text_channel(channel_name))
            await channel.send(embed=channel_created_message(channel_type, self.text_channels[-1]))
        else:
            self.voice_channels.append(await self.category.create_voice_channel(channel_name))
            await channel.send(embed=channel_created_message(channel_type, self.voice_channels[-1]))

    async def remove_channel(self, channel_id, channel_sent):
        channel = [mchannel for mchannel in self.text_channels + self.voice_channels if str(mchannel.id) == channel_id]
        if len(channel) == 1:
            if channel[0] in self.text_channels:
                self.text_channels.remove(channel[0])
            else:
                self.voice_channels.remove(channel[0])
            await channel[0].delete()
            await channel_sent.send(embed=channel_removed_message(channel_id))
        else:
            await channel_sent.send(embed=channel_not_exist_error(channel_id))

    async def invite(self, members, channel):
        description = 'I have sent invites to the following people :\n'
        for member in members:
            await member.add_roles(self.role)
            await member.send(embed=invitation(self.owner, self.category, self.guild))
            description += member.mention + ' '
        await channel.send(embed=invite_confirm(description))

    async def kick(self, members, channel):
        description = 'I have kicked the following people :\n'
        for member in members:
            await member.remove_roles(self.role)
            await member.send(embed=kick(self.owner, self.category, self.guild))
            description += member.mention + ' '
        await channel.send(embed=kick_confirm(description))
