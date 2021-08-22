import configparser
import os
import sys
import logging

# Global configuration variables
ENDPOINT = "https://app.api.surehub.io"


class InvalidConfig(Exception):
    pass


class ConfigValidator(configparser.ConfigParser):
    def __init__(self, config_file):
        super(ConfigValidator, self).__init__()

        self.config_file = config_file
        open(config_file)  # Force FileNotFoundError if config file doesn't exists
        self.read(config_file)
        self.validate_config()

    def validate_config(self):
        required_values = {
            'api': {
                'port': None,
                'log_level': ['critical', 'error', 'warning', 'info', 'debug', 'trace'],
                'debug': ['false', 'true']
            },
            'auth': {
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

    def get_setting(self, section, key):
        try:
            result = self.get(section, key).replace('"', '')
        except configparser.NoOptionError:
            result = None
        return result


try:
    config_validator = ConfigValidator(os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'config.ini')))

    # Set config attributes
    global PORT, CORS, EMAIL, PASSWORD, LOG_LEVEL
    PORT = int(config_validator.get_setting('api', 'port'))
    CORS = str(config_validator.get_setting('api', 'cors'))
    EMAIL = str(config_validator.get_setting('auth', 'email'))
    PASSWORD = str(config_validator.get_setting('auth', 'password'))
    LOG_LEVEL = str(config_validator.get_setting('api', 'log_level'))
    DEBUG = True if str(config_validator.get_setting('api', 'debug')) in ["True", "true", "1"] else False

except FileNotFoundError:
    logging.error(
        'No config.ini found! Please make sure you rename "config.ini.sample" to "config.ini" and edit the settings correctly.')
    raise SystemExit(2)

except InvalidConfig as e:
    logging.error(e)
    raise SystemExit(2)

except:
    logging.error("Configuration not successfull due to an unknown error!")
    raise SystemExit(2)
