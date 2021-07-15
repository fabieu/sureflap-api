from configparser import ConfigParser
import os
import logging
import logging.config
from requests.models import ProtocolError
import yaml

# Initialize logging
with open('logging.conf', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("sureflap")


# Global configuration variables
ENDPOINT = "https://app.api.surehub.io"


class InvalidConfig(Exception):
    pass


class ConfigValidator(ConfigParser):
    def __init__(self, config_file):
        super(ConfigValidator, self).__init__()

        self.config_file = config_file
        open(config_file)
        self.read(config_file)
        self.validate_config()

    def validate_config(self):
        required_values = {
            'api': {
                'port': None,
            },
            'user': {
                'email': None,
                'password': None,
            },
        }

        for section, keys in required_values.items():
            if section not in self:
                raise InvalidConfig(
                    f'{self.__class__.__name__}: Missing section "{section}" in {self.config_file}')

            for key, values in keys.items():
                if key not in self[section] or self[section][key] in ('', 'YOUR_PERSONAL_ACCESS_TOKEN'):
                    raise InvalidConfig(
                        f'{self.__class__.__name__}: Missing value for "{key}" in section "{section}" in {self.config_file}')

                if values:
                    if self[section][key] not in values:
                        allowed_values = f"[{(', '.join(map(str, values)))}]"
                        raise InvalidConfig(
                            f'{self.__class__.__name__}: Invalid value for "{key}" under section "{section}" in {self.config_file} - allowed values are {allowed_values}')


def init_config():
    try:
        config = ConfigValidator(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.ini')))

        global EMAIL, PASSWORD, PORT
        PORT = config['api']['port']
        EMAIL = config['user']['email'].replace('"', '')
        PASSWORD = config['user']['password'].replace('"', '')
        return True

    except FileNotFoundError:
        logger.error(
            'No config.ini found! Please make sure you rename "config.ini.sample" to "config.ini" and edit the settings correctly.')

    except InvalidConfig as e:
        logger.error(e)
        raise SystemExit(2)

    except:
        logger.error("Configuration was not successfull!")
