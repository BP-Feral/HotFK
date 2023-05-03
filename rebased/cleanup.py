import configparser
import shutil, os

def clean_project():
    dir = '__pycache__'
    locations = ['./', './classes', './scenes']

    for location in locations:
        try:
            path = os.path.join(location, dir)
            shutil.rmtree(path)
        except:
            print(f"There is no cache in {location}")

def reset_project():
    config = configparser.ConfigParser()
    config.read('./resources/configurations.ini')

    config['DEV']['first-run'] = "True"
    with open("./resources/configurations.ini", 'w') as configfile:
        config.write(configfile)

clean_project()
reset_project()