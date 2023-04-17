# Setup Python ----------------------------------------------- #
import configparser


# CLass Block ------------------------------------------------ #
class Settings:
    def __init__(self):
        pass
    
    def reset(self):
        
        config_file = configparser.ConfigParser()

        # Add Section
        config_file.add_section("Video")

        # Add settings to section
        config_file.set("Video", "fps", "60")
        config_file.set("Video", "default-width", "1920")
        config_file.set("Video", "default-height", "1080")
        config_file.set("Video", "fullscreen", "True")

        # Add Section
        config_file.add_section("Multiplayer")
        # Add settings to section
        config_file.set("Multiplayer", "offline", "True")

        # Add Section
        config_file.add_section("Sound")
        # Add settings to section
        config_file.set("Sound", "sound-volume", "1")
        config_file.set("Sound", "music-volume", "1")

        # Add Section
        config_file.add_section("Dev")
        # Add settings to section
        config_file.set("Dev", "version", "pre-0.0.9a")
        config_file.set("Dev", "debug_mode", "True")

        with open(r"configurations.ini", 'w') as configfileObj:
            config_file.write(configfileObj)
            configfileObj.flush()
            configfileObj.close()

        print("Config file 'configurations.ini' created")

        # PRINT FILE CONTENT
        read_file = open("configurations.ini", "r")
        content = read_file.read()
        print("Content of the config file are:\n")
        print(content)
        read_file.flush()
        read_file.close()