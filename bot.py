import os
import discord
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH')
twilio_num = os.getenv('TWILIO_NUM')

text_client = Client(account_sid, auth_token)
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "!text" in message.content:
        to_number = "+1" + ''.join(i for i in message.content if i.isdigit())
        pre_text_content = message.content.split("!text",1)[1]
        text_content = ''.join(i for i in pre_text_content if not i.isdigit()).strip()

        text_client.api.account.messages.create(
            to=str(to_number),
            from_=str(twilio_num),
            body=text_content
        )

        await message.channel.send(f'{message.author.mention} has texted {to_number}, saying: \'{text_content}\'!')
        



        









client.run(TOKEN)