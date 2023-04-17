# Setup Python ----------------------------------------------- #
import discordsdk as dsdk
import time as t
import uuid

from pygame import init, display, time, FULLSCREEN, mouse, image
from classes.mixer import Mixer


# CLass Block ------------------------------------------------ #
class gameEngine:
    def __init__(self, settings):
        
        init()

        # Game settings
        self.fps = settings['fps']
        self.width = settings['default-width']
        self.height = settings['default-height']
        self.fullscreen = settings['fullscreen']
        self.offline = settings['offline']
        self.debug_mode = settings['debug-mode']
        self.version = settings['version']

        # Objects
        self.mainClock = time.Clock() 
        self.mixer = Mixer()

        # Hide mouse
        mouse.set_visible(False)

        # Check for fullscreen setting
        if self.fullscreen:
            self.screen = display.set_mode((self.width, self.height), FULLSCREEN)
        else:
            self.screen = display.set_mode((self.width, self.height))

        # Set game icon and title
        game_icon = image.load('resources/images/icons/icon.ico')
        display.set_caption("Heroes of the Fallen Kingdom")
        display.set_icon(game_icon)

    ##### discord rpc #####
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
        self.mixer.update_music_volume()
        self.mixer.update_sound_volume()

        self.app.run_callbacks()

    def update_discord_status(self, state):
        self.activity.state = state
        self.activity_manager.update_activity(self.activity, lambda result: self.debug_callback("update_activity", result))

    def clear_discord_activity(self):
        self.activity_manager.clear_activity