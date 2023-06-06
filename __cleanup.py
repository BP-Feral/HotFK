import configparser
import shutil, os

def clean_project():
    dir = '__pycache__'
    locations = ['./', './classes', './scenes', './scenes/extras']

    for location in locations:
        try:
            path = os.path.join(location, dir)
            shutil.rmtree(path)
        except:
            print(f"There is no cache in {location}")

    try:
        shutil.rmtree('./build')
    except:
        print(f"There were no builds to clear")
    try:
        shutil.rmtree('./dist')
    except:
        print(f"There were no dists to clear")

    try:
        os.remove('./Heroes of the Fallen Kingdom.spec')
    except:
        print(f"There was no spec file to remove")

    print("Cleanup Complete!")

def reset_project():
    config = configparser.ConfigParser()
    config.read('./resources/configurations.ini')

    config['DEV']['first-run'] = "True"
    with open("./resources/configurations.ini", 'w') as configfile:
        config.write(configfile)
    print("Reset Complete!")

clean_project()
reset_project()