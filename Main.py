#FOR PRIVATE GITHUB IF YOU FIND THIS AND DONT BELONG HERE, I WILL BE VERY SAD --> :(

from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
import praw




#Step 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE AND SET UP DISCORD CLIENT
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN') #TOKEN is a constant string.
reddit = praw.Reddit(
    client_id="nzI5EwUqP6hSVn9l234C8w",
    client_secret = "kekre0sXL_hlDhZ6qA-k01k329XAaQ",
    user_agent="Grand_Effect1265",
)


#STEP 1: BOT SETUP

intents: Intents = Intents.default() #We created variable 'intents', and Intents is a class which manages permissions, and Intents.default() sets those permissions to the default ones
intents.message_content = True # NOQA
client : Client = Client(intents = intents) #no idea what this is

#STEP 2: MESSAGE FUNCTIONALITY

async def send_message(message: Message, user_message: str) -> None: #Async def allows the function to work in the background while other tasks are executed.
    if not user_message:                                             #this code says that Message represents the message received and that the message is a string and returns none
        print("(Message was empty because intents weren't enabled)")
        return #If the message intent is empty, it returns the message and exits the function
    if is_private := user_message[0] == '?': #It uses the walrus operator to evaluate and assign is_private to user_message
        user_message = user_message[1:] #It splices the question mark out of the message. The question mark is a request from user for private messaging
    try:
        response: str = get_response(user_message) #This basically refers our code to the responses section
        await message.author.send(response) if is_private else await message.channel.send(response) #If the message is private, it DMs the user privately, if not it messages the channel
    except Exception as e:
        print(e) #This basically logs any error from the code and outputs it

#STEP 3: HANDLING THE STARTUP FOR OUR BOT

@client.event #Client event basically means this function will execute when a certain event occurs
async def on_ready() -> None: #Bot runs when its ready
    print(f'{client.user} is now running!') #Basically tells us that the bot is working

#STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message (message: Message) -> None:
    if message.author == client.user:
        return #Basically, this code checks to see if the message author is the bot itself, so it returns early before it can respond to its own messages, creating a feedback loop

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print (f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

#STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()