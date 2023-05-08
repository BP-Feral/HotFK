import os, shutil
from __cleanup import clean_project, reset_project

clean_project()
reset_project()

flags = ['--noconsole', '--name "Heroes of the Fallen Kingdom"', '--icon "resources/images/icons/icon.ico"', '--hidden-import glcontext']
script_path = "main.py"
os.system(f"pyinstaller {' '.join(flags)} {script_path}")


dst_dir = './dist/Heroes of the Fallen Kingdom/resources'
src_dir = './resources'
shutil.copytree(src_dir, dst_dir)

dst_dir = './dist/Heroes of the Fallen Kingdom/lib'
src_dir = './lib'
shutil.copytree(src_dir, dst_dir)

dst_dir = './dist/Heroes of the Fallen Kingdom'
shutil.copy2('steam_api64.dll', dst_dir)
shutil.copy2('steam_api64.lib', dst_dir)
shutil.copy2('steam_appid.txt', dst_dir)
shutil.copy2('SteamworksPy64.dll', dst_dir)