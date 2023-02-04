import pytest
import pathlib
from pathlib import Path
import json

DIR_PATH = pathlib.Path.cwd()
TEST_LOG_TEXT = Path('090127-192_168_0_3_1024.txt')
TEST_FILE = Path(DIR_PATH, TEST_LOG_TEXT)

TEST_ERRORS = []


def param_save(data):
    with open('testParameters.json', 'w+') as f:
        f.write(f"{data}\n")


def json_save(data):
    with open('testJson.json', 'w+') as f:
        f.write(f"{data}")


def test_parameters():
    with open(TEST_FILE) as f:
        param = []
        lines = f.readlines()
        for line in lines:
            if line.find('message') != -1 and line.find('{"') != -1:
                substring = line[line.find('message'):line.rfind('}') + 1].replace('message ', '"') \
                    .replace(' params', '"').replace('=', ':').replace('"', '').replace(',', ', ')\
                    .replace(' : ', ': ')
                try:
                    get_json = json.loads(json.dumps(substring))
                    param.append(get_json)
                    param_save(param)  # save
                except json.decoder.JSONDecodeError as e:
                    TEST_ERRORS.append(f'Error: {e}')


def test_json_format():
    with open(TEST_FILE) as f:
        param = []
        lines = f.readlines()
        for line in lines:
            if line.find('{"') != -1:
                substring = line[line.find('{"'):line.rfind('}') + 1]
                try:
                    get_json = json.loads(substring)
                    param.append(get_json)
                    json_save(param) # save
                except json.decoder.JSONDecodeError as e:
                    TEST_ERRORS.append(f'Error: {e}')



