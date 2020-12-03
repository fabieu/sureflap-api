import configparser
import os
import validators

try:
    config = configparser.ConfigParser()
    config.read(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config.ini')))

    endpoint = config['api']['endpoint'].replace('"', '')
    email = config['user']['email'].replace('"', '')
    password = config['user']['password'].replace('"', '')
except:
    print('No valid config.ini found! Please make sure you rename "config.ini.sample" to "config.ini" and edit the settings correctly.')
    os._exit(0)


def validate():
    if email != "SureFlapEmail" and password != "SureFlapPassword":
        if validators.url(endpoint):
            return True
        else:
            print("Invalid endpoint provided. Please check the syntax!")
            return False
    else:
        print("Please edit the config.ini first!")
        return False

    
