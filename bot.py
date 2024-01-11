import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send() if is_private else await message.channel.send()
    except Exception as e:
        print(e)



def run_discord_bot():
    TOKEN = 'MTE5NDg4OTUwNDE2NzgyMTM3Mg.GkC73r.ZlkBwbswRwqF3dOTWYQZu4KecoIUs7aQSMBaf4'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is not running!')

        client.run(TOKEN)