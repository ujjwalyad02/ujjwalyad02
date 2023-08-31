from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
import csv

API_ID = '25789186'
API_HASH = 'b94a4f282c25eb3669ed09d8949d9c07'
PHONE_NUMBER = 'your_phone_number'  # Your phone number with country code
MAX_MEMBERS = 10000  # Maximum number of unique members to scrape

async def main():
    async with TelegramClient(PHONE_NUMBER, API_ID, API_HASH) as client:
        dialog = await client.get_input_entity('group_username')  # Replace with the group username
        limit = 100  # Number of messages to fetch
        max_members = MAX_MEMBERS
        participants = set()

        while max_members > 0:
            messages = await client.get_messages(dialog, limit=limit)
            
            for message in messages:
                if message.sender_id:
                    participants.add(message.sender_id)
                    max_members -= 1
                    if max_members <= 0:
                        break
            
            if len(messages) < limit:
                break

        with open('group_members.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Member ID'])
            writer.writerows([[member_id] for member_id in participants])

if __name__ == '_main_':
    import asyncio
    asyncio.run(main())
