#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from fbchat import Client, ThreadType, Message
import asyncio

thread_ids = set()

# Subclass fbchat.Client and override required methods
class PoppyBot(Client):
    async def on_message(self, mid=None, author_id=None, message_object=None, thread_id=None,
                         thread_type=ThreadType.USER, at=None, metadata=None, msg=None):
        await self.mark_as_delivered(thread_id, message_object.uid)
        await self.mark_as_read(thread_id)

        print("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid and thread_id not in thread_ids:
            thread_ids.add(thread_id)
            poppy = f"""```
 _________
< enough! >
 ---------
    \   ^__^
     \  (oo)\_______
        (__)\       )\\/\\ 
            ||----w |
            ||     ||

contact me at:

 ✉ mymail@ownserver.net
 ☎ +321 1234567890

 ▶ youtu.be/k_Jq38JKN3A
 ▶ tiny.cc/fortheplants

[you were no {len(thread_ids)} blocked]

```"""
            reply = Message(text=poppy)
            await self.send(reply, thread_id=thread_id, thread_type=thread_type)
            print("Sent message")
            await self.block_user(author_id)
            print(f"Blocked: {author_id}")
            with open('threads.conf', 'a') as config_file:
                config_file.write(thread_id + "\n")
            print(thread_ids, "<-", thread_id)

# Read list of thread IDs already announced to if available
try:
    with open('threads.conf', 'r') as config_file:
        thread_ids = set(config_file.read().split())
except FileNotFoundError:
    pass
    
print(thread_ids)

loop = asyncio.get_event_loop()

async def start():
    client = PoppyBot(loop=loop)
    print("Logging in...")
    await client.start("<username>", "<password>")
    print(f"Own ID: {client.uid}")
    client.listen()
    print("Listening...")

loop.run_until_complete(start())
loop.run_forever()
