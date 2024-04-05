import configparser
import os


def read_config(file_path):
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', file_path)
    config.read(config_path)
    return config
