import flask
import bot_api
import time
import gen_html
import webbrowser
import threading
import nuker

from flask_socketio import SocketIO

def find_path():
    import os
    path = os.path.join(os.getcwd(), 'pages')
    return path if os.path.exists(path) else None
api = None
class WebUI:
    def __init__(self, app):
        self.app: flask.Flask = app
        self.api = None  # Initialize api attribute


    def start(self):
        self.app.add_url_rule('/', 'token', self.token_get)
        self.app.add_url_rule('/nuke', 'nuke', self.nuke)
        self.app.add_url_rule('/serverlist', 'serverlist', self.serverlist, methods=['POST', 'GET'])
        self.app.add_url_rule('/handle_token', 'handle_token', self.handle_token, methods=['POST', 'GET'])
        self.app.add_url_rule('/start_action', 'start_action', self.start_action, methods=['POST'])
        self.app.add_url_rule('/handle_server', 'handle_server', self.handle_server, methods=['POST', 'GET'])
        print('Starting WebUI...')
        host = '127.0.0.1'
        port = 5000
        print('URL: http://{}:{}'.format(host, port))
        webbrowser.open('http://{}:{}'.format(host, port))
        self.app.run(host=host, port=port, debug=False)


    def token_get(self):
        return flask.render_template('token.html', token='token')

    def handle_token(self):
        global api
        try:
            token = flask.request.form['token']
            print(f'[+] Received token: {token}')
            api = bot_api.Bot(token)

            guild_names = []
            print("[+] Getting guilds...")
            guilds = api.get_guilds().json()
            for guild in guilds:
                guild_names.append(guild['name'])
            print("[+] Generating HTML...")
            gen_html.generate_html(guild_names)
            print("[+] Done!")
            
            print(f'[+] Logged in as: {api.name}')
            return flask.redirect('/serverlist')
        except KeyError:
            return flask.redirect('/')
        
    def nuke(self):
        global api
        print(api.name)
        return flask.render_template('nuke.html', username=api.name, server = self.managed_guild['name'])

    def start_action(self):
        try:
            # Gather data from the form
       
            nuke_channels = flask.request.form.get('nukeChannels') == 'on'
            channels_amount = flask.request.form.get('channelsAmount')
            create_channels = flask.request.form.get('createChannels') == 'on'
            custom_channel_names = flask.request.form.get('customChannelNames')
            channels_amount_create = flask.request.form.get('channelsAmountCreate')
            nuke_roles = flask.request.form.get('nukeRoles') == 'on'
            roles_amount = flask.request.form.get('rolesAmount')
            kick_members = flask.request.form.get('kickMembers') == 'on'
            spam_text = flask.request.form.get('spamText') == 'on'
            spam_amount = flask.request.form.get('spamAmount')
            spam_text_value = flask.request.form.get('spamTextValue')

            # Print the gathered data to the console
            print("[+] Gathered Data:")
            print(f"[+] Nuke Channels: {nuke_channels}")
            print(f"[+] Channels Amount: {channels_amount}")
            print(f"[+] Create Channels: {create_channels}")
            print(f"[+] Custom Channel Names: {custom_channel_names}")
            print(f"[+] Channels Amount Create: {channels_amount_create}")
            print(f"[+] Nuke Roles: {nuke_roles}")
            print(f"[+] Roles Amount: {roles_amount}")
            print(f"[+] Kick Members: {kick_members}")
            print(f"[+] Spam Text: {spam_text}")
            print(f"[+] Spam Amount: {spam_amount}")
            print(f"[+] Spam Text Value: {spam_text_value}")

            # self.send_data_to_client("Starting action...") 
            # time.sleep(5)
            self.nuker = nuker.Nuker(api)
            self.nuker.set_guild(self.managed_guild)
            if nuke_channels:
                self.nuker.nuke_channels()
            if create_channels:
                self.nuker.create_channels(int(channels_amount_create), custom_channel_names)
            if nuke_roles:
                self.nuker.nuke_roles()
                self.nuker.create_roles(int(roles_amount))
            if spam_text:
                time.sleep(1) # wait for channels to be created since getting chanels was delayed
                self.nuker.spam_channels(int(spam_amount), spam_text_value)
            if kick_members:
                self.nuker.kick_members()
            
            
            return flask.redirect('/nuke')  # Redirect to the nuke page or another appropriate page
        except Exception as e:
            print(f"Error processing action: {e}")
            return flask.redirect('/')  # Redirect to the nuke page or another appropriate page
    def handle_server(self):
        print("[+] Handling server...")
        print(flask.request.form.get("server"))
        chosen_server = flask.request.form.get("server")
        print(f"[+] Chosen server: {chosen_server}")
        self.managed_guild = api.get_guilds().json()[int(chosen_server)]
        print(f"[+] Managed guild: {self.managed_guild}")
        time.sleep(1)
        return flask.redirect('/nuke')
    

        
    def serverlist(self):
        return flask.render_template('serverlist.html')
    

app_instance = flask.Flask(__name__, template_folder=find_path())

webui = WebUI(app_instance)
if __name__ == '__main__':
    webui.start()


