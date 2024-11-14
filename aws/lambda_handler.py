# AWS Lambda handler functions
import json
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!")
    }