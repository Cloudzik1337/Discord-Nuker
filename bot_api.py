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
        self.api = "https://discord.com/api/v9"
        self.session = requests.Session()
        self.user = None
        self._logged_as()
    



    def _change_api(self):
        new_api = random.randint(6, 9)
        self.api = f"https://discord.com/api/v{new_api}"

    def _logged_as(self):
        r = self._get("/users/@me")
        if r == 401:
            print("Invalid token")
            return
        self.user = r.json()
        # Example Usage: 
        # self.user['username']
        # self.user['id']
            


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
    
    def spam_channel(self, channelid, content, ammount, delay=0.3):
        for _ in range(ammount):

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

    def get_guild_members(self, guildid):
        return self._get(f"/guilds/{guildid}/members")
    
    def ban_member(self, guildid, userid, reason=None, delete_message_days=0):
        return self._put(f"/guilds/{guildid}/bans/{userid}", data={"reason": reason, "delete_message_days": delete_message_days})
    
    def kick_member(self, guildid, userid):
        return self._delete(f"/guilds/{guildid}/members/{userid}")
    def create_webhook(self, channelid, name="CloudNuker"):
        return self._post(f"/channels/{channelid}/webhooks", data={"name": name})
    def send_message_to_wb(self, webhook_url, content):
        return requests.post(webhook_url, json={"content": content})
    def delete_wb(self, url=None, wb_id=None, wb_token=None) -> None:
        if url is not None:
            return self._delete(url)
        return self._delete(f"/webhooks/{wb_id}/{wb_token}")
            