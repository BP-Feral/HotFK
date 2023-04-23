# Setup Python ----------------------------------------------- #
import discordsdk as dsdk
import time as t
import uuid

from pygame import init, display, time, FULLSCREEN, mouse, image
from classes.mixer import Mixer
from classes.settings import Settings
from maintenance import process_exists


# CLass Block ------------------------------------------------ #
class gameEngine:
    def __init__(self):

        init()

        # Game settings
        self.width = int
        self.height = int
    
        self.settings = Settings()
        #self.update_game_settings()

        # Objects
        self.mainClock = time.Clock() 
        self.mixer = Mixer(self.settings)

        # Is discord open?
        if process_exists("discord.exe"):
            self.discord_active = True
            print("Discord running")
        else:
            print("Discord is not running")
            self.discord_active = False

        # Hide mouse
        mouse.set_visible(False)

        # Check for fullscreen setting
        if self.settings.get_fullscreen():
            self.screen = display.set_mode((self.settings.get_width(), self.settings.get_height()), FULLSCREEN)
        else:
            self.screen = display.set_mode((self.settings.get_width(), self.settings.get_height()))

        # Set game icon and title
        game_icon = image.load('resources/images/icons/icon.ico')
        display.set_caption("Heroes of the Fallen Kingdom")
        display.set_icon(game_icon)

        # Initialize discord activity if Discord is running
        if self.discord_active:
            discord_application_id = 1097332146923913288
            self.app = dsdk.Discord(discord_application_id, dsdk.CreateFlags.default)
            self.activity_manager = self.app.get_activity_manager()
            
            # setup activity
            self.activity = dsdk.Activity()
            self.activity.state = "Just started"

            # party settings
            self.activity.party.id = str(uuid.uuid4())
            self.activity.party.size.current_size = 1
            self.activity.party.size.max_size = 4
            self.activity.secrets.join = str(uuid.uuid4())
            self.activity.timestamps.start = int(t.time())

            # activity icon        
            self.activity.assets.large_image = "https://i.imgur.com/thAl2Ll.png"

            # update the activity
            self.activity_manager.update_activity(self.activity, lambda result: self.debug_callback("update_activity", result))


# Callbacks -------------------------------------------------- #
    def debug_callback(self, debug, result, *args):
        if result == dsdk.Result.ok:
            print(debug, "success")
        else:
            print(debug, "failure", result, args)


# Updates ---------------------------------------------------- #
    def updates(self):
        if self.discord_active:
            try:
                self.app.run_callbacks()
            except:
                self.discord_active = False

    def update_discord_status(self, state):
        if self.discord_active:
            self.activity.state = state
            self.activity_manager.update_activity(self.activity, lambda result: self.debug_callback("update_activity", result))

    def clear_discord_activity(self):
        if self.discord_active:
            self.activity_manager.clear_activity