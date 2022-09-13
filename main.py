import os
from itertools import cycle

import aiohttp
import discord
from discord import Webhook
from discord.ext import tasks

import getRandRow

BotToken = os.environ['BotToken']
WEBHOOK_URL = os.environ['WEBHOOK_URL']
TEST = os.environ['TEST']

status = cycle(
    ['Destroying Nerds in a Block Game', 'Sacrificing Nerds To The Blood God'])


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# The actual Bot
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        change_status.start()
        print('------')

    async def on_message(self, message):

        a = 'Nerd'
        aa = 'Techno'
        why = 'Why'
        # don't respond to ourselves
        if message.author == self.user:
            return

        if aa.lower() in message.content.lower():
            await message.channel.send('DONT USE MY NAME LIKE YOU OWN IT. NERD'
                                       )

        if message.content == '!randomQuote':
            q = await getRandRow.getRandomRow()
            await message.channel.send(q)

        if a.lower() in message.content.lower():
            await message.reply('Spoken like a true NERD')

        if why.lower() in message.content.lower():
            if message.content.lower(
            ) == 'cause why not' or message.content.lower(
            ) == 'cause why not?':
                replied_message = await message.channel.fetch_message(
                    message.reference.message_id)
                author = replied_message.author
                author_name = author.display_name
                author_pfp = author.avatar

                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(WEBHOOK_URL, session=session)
                    await webhook.send(content='Understandable, have a nice day!', username=author_name,
                                       avatar_url=author_pfp)

            else:
                await message.reply('Cause why not?')

        if message.content == '!test':
            await message.reply(TEST)

intents = discord.Intents.all()
client = MyClient(intents=intents)
client.run(BotToken)