#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from fbchat import log, Client
from fbchat.models import *

poppy = """```
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

```"""

reply = Message(text=poppy)

thread_ids = set()

# Subclass fbchat.Client and override required methods
class PoppyBot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid and thread_id not in thread_ids:
            self.send(reply, thread_id=thread_id, thread_type=thread_type)
            thread_ids.add(thread_id)
            self.blockUser(author_id)
            with open('threads.conf', 'a') as config_file:
                config_file.write(thread_id + "\n")
            print(thread_ids, thread_id)

# Read list of thread IDs already announced to if available
try:
    with open('threads.conf', 'r') as config_file:
        thread_ids = set(config_file.read().split())
except FileNotFoundError:
    pass
    
print(thread_ids)

client = PoppyBot('<username>', '<password>')
client.listen()
