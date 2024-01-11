from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# load token from somewhere
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

# bot setup
intents: Intents = Intents.default()
intents.message_content = True #NOQA
client: Client = Client(intents=intents)

# message functionality
async def send_message(message: Message,user_message:str) -> None:
    if not user_message:
        print('(Message was empty because intents were probably not enabled')
        return


    if is_private := user_message[0] == '?': # if there's a question mark, it will message in dms.
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# handling startup for bot
@client.event
async def on_ready() -> None:
    print(f' {client} is now running')


#handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user: # if bot wrote message, don't respond
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# main entry point where code runs

def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()




