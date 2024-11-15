import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
print(TOKEN)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send(f"Hello {message.author.name}! How can I help you today?")

client.run(TOKEN)