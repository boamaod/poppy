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

# Subclass fbchat.Client and override required methods
class PoppyBot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(reply, thread_id=thread_id, thread_type=thread_type)
            self.blockUser(author_id)

client = PoppyBot('<username>', '<password>')
client.listen()
