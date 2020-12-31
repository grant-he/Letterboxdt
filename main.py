import discord
import os
# import requests
# import json

client = discord.Client()
users = []

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg == '!help':
    embed = discord.Embed(title='Help with Letterboxd Bot', description='Some useful commands', color=0x5bb36b)
    embed.add_field(name='!follow', value='Follow user', inline=True)
    embed.add_field(name='!unfollow', value='Unfollow user', inline=True)
    embed.add_field(name='!following', value='Display all followed users', inline=True)
    await message.channel.send(embed=embed)
  elif msg == '!following':
    if len(users) == 0:
      await message.channel.send('No users are being followed in the channel')
    else:
      result = 'List of Letterboxd members being followed in the channel: '
      for user in users[:-1]:
        result += user + ', '
      result += users[-1]
      await message.channel.send(result)
  elif msg.startswith('!follow '):
    new_user = msg.split('!follow ', 1)[1]
    if new_user in users:
      await message.channel.send(f'> **{new_user}** is already being followed')
    else:
      users.append(new_user)
      # TODO: Add link and profile picture to user
      await message.channel.send(f'> Now following **{new_user}** in this channel')
  elif msg.startswith('!unfollow '):
    rem_user = msg.split('!unfollow ', 1)[1]
    if rem_user in users:
      users.remove(rem_user)
      # TODO: Add link to user
      await message.channel.send(f'**{rem_user}** is no longer being followed in this channel.')
    else:
      await message.channel.send(f'**{rem_user}** was not found')

client.run(os.getenv('TOKEN'))