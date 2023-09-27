import configparser
# Settings Class =============================================== #
class Settings():

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./resources/config.ini')

    def reset(self):
        self.config["VIDEO"] = {
            'fps': '60',
            "default-width": "1920",
            "default-height": "1080",
            "fullscreen": "True",
            "use-native": "False"
        }
        self.config["MULTIPLAYER"] = {
            'offline': "True"
        }
        self.config["SOUND"] = {
            "sound-volume": "0.5",
            "music-volume": "0.3"
        }
        self.config["DEV"] = {
            "version": "pre-0.0.12a",
            "debug-mode": "True",
            "first-run": "True"
        }
        self.config["CHAT"] = {
            "console-toggle": "False"
        }
        self.write_to_file()

    def write_to_file(self):
        with open("./resources/configurations.ini", 'w') as configfile:
            self.config.write(configfile)

# Getters ---------------------------------------------------- #
    def get_fps(self):
        return int(self.config['VIDEO']['fps'])

    def get_width(self):
        return int(self.config['VIDEO']['default-width'])

    def get_height(self):
        return int(self.config['VIDEO']['default-height'])

    def get_fullscreen(self):
        return True if self.config['VIDEO']['fullscreen'] == "True" else False

    def get_offline(self):
        return self.config['MULTIPLAYER']['offline']

    def get_sound_volume(self):
        return float(self.config['SOUND']['sound-volume'])

    def get_music_volume(self):
        return float(self.config['SOUND']['music-volume'])

    def get_version(self):
        return self.config['DEV']['version']

    def get_console_toggle(self):
        return True if self.config['CHAT']['console-toggle'] == "True" else False

    def get_debug_mode(self):
        return self.config['DEV']['debug-mode']

    def get_native(self):
        return True if self.config['VIDEO']['use-native'] == "True" else False

    def get_first_run(self):
        return True if self.config['DEV']['first-run'] == "True" else False

# Setters ---------------------------------------------------- #
    def set_music_volume(self, value):
        self.config['SOUND']['music-volume'] = str(value)

    def set_sound_volume(self, value):
        self.config['SOUND']['sound-volume'] = str(value)

    def set_console_toggle(self, value):
        self.config['CHAT']['console-toggle'] = str(value)

    def set_width(self, value):
        self.config['VIDEO']['default-width'] = str(value)

    def set_height(self, value):
        self.config['VIDEO']['default-height'] = str(value)

    def set_first_run(self, value):
        self.config['DEV']['first-run'] = str(value)
        self.write_to_file()