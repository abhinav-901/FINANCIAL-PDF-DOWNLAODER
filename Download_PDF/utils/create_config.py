import configparser
from pathlib import Path
import os


class CreateConfig:
    """
    This file is used to create config file
     for accessing configurable parameters
    """

    def __init__(self):
        self.config = configparser.ConfigParser()

    def create_config(self):

        self.config['FILE_PATH'] = {'company_code_path': 'path',
                                    'output_path': 'output/pdf/path'}
        self.config['PATTERN'] = {'regex_pattern_string': 'pattern string'}
        file_dir = Path(__file__).parent
        file_name = 'config.ini'
        file_path = os.path.join(file_dir, file_name)
        print(f"Created config.ini and saved at location below\n{file_path}")
        with open(file_path, 'w') as fp:
            self.config.write(fp)


if __name__ == '__main__':
    CreateConfig().create_config()
