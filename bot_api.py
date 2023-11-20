import requests
import time
import os
import random
"""Bot api for discord bot made by Cloudzikk

 * Educational Purpose Only
 * Author: [Cloudzik1337]
 * Date: [20.11.23]

https://github.com/cloudzik1337
"""

class Bot:
    """Backend for discord bot"""
    def __init__(self, token):
        self.token = 'Bot ' + token 
        # as start we use v9 discord api
        self.api = "https://discord.com/api/v9"
        self.session = requests.Session()
        self._logged_as()
     

    def _change_api(self):
        new_api = random.randint(6, 9)
        self.api = f"https://discord.com/api/v{new_api}"

    def _logged_as(self):
        #log in to bot token 
        r = self._get("/users/@me")
        if r == 401:
            print("Invalid token")
            return
        self.name = r.json()["username"]
        self.id = r.json()["id"]
            


    def _get(self, endpoint, data=None):
        return self.session.get(f"{self.api}{endpoint}", headers = {"Authorization": self.token, "Content-Type": "application/json"}, json=data)
    
    def _post(self, endpoint, data=None):
        return self.session.post(f"{self.api}{endpoint}", headers = {"Authorization": self.token, "Content-Type": "application/json"}, json=data)
    
    def _patch(self, endpoint, data=None):
        return self.session.patch(f"{self.api}{endpoint}", headers = {"Authorization": self.token, "Content-Type": "application/json"}, json=data)
    
    def _delete(self, endpoint, data=None):
        return self.session.delete(f"{self.api}{endpoint}", headers = {"Authorization": self.token, "Content-Type": "application/json"}, json=data)
    
    def get_guilds(self):
        return self._get("/users/@me/guilds")
    
    def get_channel(self, channelid):
        return self._get(f"/channels/{channelid}")
    
    def get_guild(self, guildid):
        return self._get(f"/guilds/{guildid}")
    
    def get_guild_channels(self, guildid):
        return self._get(f"/guilds/{guildid}/channels")

    def send_message(self, channelid, content):
        return self._post(f"/channels/{channelid}/messages", data={"content": content})
    
    def find_text_channels(self, guildid):
        channels = self.get_guild_channels(guildid).json()
        text_channels = []
        for channel in channels:
            if channel["type"] == 0:
                text_channels.append(channel)
        return text_channels
    
    def find_voice_channels(self, guildid):
        channels = self.get_guild_channels(guildid).json()
        voice_channels = []
        for channel in channels:
            if channel["type"] == 2:
                voice_channels.append(channel)
        return voice_channels
    
    def get_messages(self, channelid):
        return self._get(f"/channels/{channelid}/messages")
    
    def delete_all_channels(self, guildid):
        channels = self.get_guild_channels(guildid).json()
        for channel in channels:
            self.delete_channel(channel["id"])

    def delete_channel(self, channelid):
        return self._delete(f"/channels/{channelid}")
    
    def create_channel(self, guildid,type, name=None):
        if name == None:
            name = os.urandom(16).hex()
        return self._post(f"/guilds/{guildid}/channels", data={"name": name, "type": type})
    
    def spam_channel(self, channelid, content, amount, delay=0.3):
        for _ in range(amount):

            try :self.send_message(channelid, content)
            except:pass
            time.sleep(delay)
        
    def get_roles(self, guildid):
        return self._get(f"/guilds/{guildid}/roles")
    
    def delete_role(self, guildid, roleid):
        return self._delete(f"/guilds/{guildid}/roles/{roleid}")
    
    def delete_all_roles(self, guildid):
        roles = self.get_roles(guildid).json()
        for role in roles:
            self.delete_role(guildid, role["id"])
    
    def create_role(self, guildid, name="CloudNuker", color=0, hoist=False, mentionable=False, permissions=0):
        return self._post(f"/guilds/{guildid}/roles", data={"name": name, "color": color, "hoist": hoist, "mentionable": mentionable, "permissions": permissions})

    def create_invite(self, channelid, max_age=0, max_uses=0, temporary=False, unique=False):
        return self._post(f"/channels/{channelid}/invites", data={"max_age": max_age, "max_uses": max_uses, "temporary": temporary, "unique": unique})
