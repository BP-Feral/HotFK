# Setup Python ----------------------------------------------- #
import configparser


# CLass Block ------------------------------------------------ #
class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./resources/configurations.ini')


# Functions -------------------------------------------------- #
    def reset(self):

        # Add Section
        self.config["VIDEO"] = {
            'fps': '60',
            "default-width": "1920",
            "default-height": "1080",
            "fullscreen": "True"
        }

        # Add Section
        self.config["MULTIPLAYER"] = {
            'offline': "True"
        }

        # Add Section
        self.config["SOUND"] = {
            "sound-volume": "0.5",
            "music-volume": "0.3"
        }

        # Add Section
        self.config["DEV"] = {
            "version": "pre-0.0.9a",
            "debug_mode": "True"
        }

        # Write to file
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
        return self.config['VIDEO']['fullscreen']

    def get_offline(self):
        return self.config['MULTIPLAYER']['offline']

    def get_sound_volume(self):
        return round( float(self.config['SOUND']['sound-volume']), 1)

    def get_music_volume(self):
        return round( float(self.config['SOUND']['music-volume']), 1)

    def get_version(self):
        return self.config['DEV']['version']

    def get_debug_mode(self):
        return self.config['DEV']['debug_mode']


# Setters ---------------------------------------------------- #
    def set_music_volume(self, value):
        self.config['SOUND']['music-volume'] = str(value)