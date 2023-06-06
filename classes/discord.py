# Setup Python =============================================== #
import discordsdk as dsdk
import time, uuid, pygame

from maintenance import process_exists
from PIL import Image


# Discord Class ============================================== #
class Discord():
    def __init__(self, mixer):
        if process_exists("discord.exe"):
            self.discord_active = True
        else:
            self.discord_active = False

        self.mixer = mixer
        self.portrait = None

        if self.discord_active:
            discord_application_id = 1097332146923913288
            self.app = dsdk.Discord(discord_application_id, dsdk.CreateFlags.default)

            self.activity_manager = self.app.get_activity_manager()
            self.activity_manager.on_activity_join_request = self.on_activity_join_request
            time.sleep(0.2)
            #
            self.activity_manager.on_activity_join = self.on_activity_join
            self.activity_manager.on_activity_invite = self.on_activity_invite
            time.sleep(0.2)

            self.user_manager = self.app.get_user_manager()
            self.image_manager = self.app.get_image_manager()
            time.sleep(0.2)

            self.user_manager.on_current_user_update = self.on_current_user_update
            time.sleep(0.2)

            # setup activity
            self.activity = dsdk.Activity()
            self.activity.state = "Just started"

            # activity icon
            self.activity.assets.large_image = "https://i.imgur.com/thAl2Ll.png"

            # update the activity
            self.update_discord_status("Just Started")

# Functions ================================================== #
    def get_portrait(self):
        # handle
        handle = dsdk.ImageHandle()
        handle.type = dsdk.ImageType.user
        handle.id = self.user.id
        handle.size = 256

        self.image_manager.fetch(handle, True, self.on_image_loaded)

        return self.portrait

    def get_username(self):
        return [self.user.username, self.user.discriminator]

    def on_image_loaded(self, result, handle):
        if result != dsdk.Result.ok:
            print(f"Failed to fetch the image (result {result})")
        else:
            print("Fetched the image!")
            print("Handle:", handle.type, handle.id, handle.size)

            dimensions = self.image_manager.get_dimensions(handle)
            print("Dimensions:", dimensions.width, dimensions.height)

            # we load the image
            data = self.image_manager.get_data(handle)
            im = Image.frombytes("RGBA", (dimensions.width, dimensions.height), data)
            self.portrait = pygame.image.fromstring(im.tobytes(), im.size, im.mode).convert() # type: ignore

    def is_active(self):
        return self.discord_active

    def clear_activity(self):
        self.activity_manager.clear_activity

    def disable(self):
        self.discord_active = False


# Updates ---------------------------------------------------- #
    def on_current_user_update(self):
        self.user = self.user_manager.get_current_user()
        print(f"Hello, {self.user.username}#{self.user.discriminator}")

        self.get_portrait()

    def on_activity_join_request(self, user):
        print(f"{user.username} wants to join you")
        self.mixer.sound_play('resources/sounds/Join.mp3')

    def debug_callback(self, debug, result, *args):
            print(debug, "success") if result == dsdk.Result.ok else print(debug, "failure", result, args)

    def update_discord_status(self, state):
        if self.discord_active:
            self.activity.state = state
            self.activity_manager.update_activity(self.activity, lambda result: self.debug_callback("update_activity", result))

    def tick(self):
        # Call required updates
        if self.is_active():
            try:
                self.app.run_callbacks()
            except:
                self.disable()

    def on_activity_join(self, join_secret):
        print("Activity Joined")

    def on_activity_invite(self, type, user, activity):
        print("Activity Invite Received")

    def update_party(self, min, max):
        # party settings
        print("party updated")
        self.activity.party.id = str(uuid.uuid4())
        self.activity.party.size.current_size = min
        self.activity.party.size.max_size = max
        self.activity.secrets.join = str(uuid.uuid4())
        self.activity.timestamps.start = int(time.time())
        self.activity_manager.update_activity(self.activity, lambda result: self.debug_callback("update_activity", result))