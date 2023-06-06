import sys, os
from steamworks import STEAMWORKS
from maintenance import process_exists

if sys.version_info >= (3, 8):
  os.add_dll_directory(os.getcwd()) # Required since Python 3.8

class Steam():
    def __init__(self):
        self.steam_running = self.check_if_running()
        if self.steam_running:
            self.steamworks = STEAMWORKS()
            self.steamworks.initialize()

    def check_if_running(self):
        if process_exists("steam.exe"):
            return True
        else:
            return False

    def get_current_user(self):
        self.my_steam64 = self.steamworks.Users.GetSteamID()
        self.my_steam_level = self.steamworks.Users.GetPlayerSteamLevel()
        print(f"logged in as {self.my_steam64}, level {self.my_steam_level}")

    def is_running(self):
        return True if self.steam_running == True else False