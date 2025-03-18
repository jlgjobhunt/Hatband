#   unit-test_hatband_cli_list_records_v0_009.py

import pytest
import os
import json
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from hatband_v0_009 import Hatband
from hatband_cli_v0_009 import list_records


HATBAND_STORAGE = "test_hatband_storage"

def setup_module():
    os.makedirs(HATBAND_STORAGE, exist_ok=True)
    with open(os.path.join(HATBAND_STORAGE, "test_hatband.json"), "w") as f:
        json.dump([{"hatband": "test_hatband", "key": "key1", "value": "value1"},
                   {"hatband": "test_hatband", "key": "key2", "value": "value2"}], f)
        
def teardown_module():
    for filename in os.listdir(HATBAND_STORAGE):
        os.remove(os.path.join(HATBAND_STORAGE, filename))
    os.rmdir(HATBAND_STORAGE)

def test_list_records_success(capsys):
    list_records(['--hatband-name', 'test_hatband', '--storage-dir', HATBAND_STORAGE])
    captured = capsys.readouterr()
    assert "{'hatband': 'test_hatband', 'key': 'key1', 'value': 'value1'}" in captured.out
    assert "{'hatband': 'test_hatband', 'key': 'key2', 'value': 'value2'}" in captured.out

def test_list_records_no_records(capsys):
    list_records(['--hatband-name', 'nonexistent_hatband', '--storage-dir', HATBAND_STORAGE])
    captured = capsys.readouterr()
    assert "No records found." in captured.out

def test_list_records_missing_hatband_name(capsys):
    list_records(['--storage-dir', HATBAND_STORAGE])
    captured = capsys.readouterr()
    assert "Error: --hatband-name is required." in captured.out

def test_list_records_missing_storage_dir(capsys):
    list_records(['--hatband-name', 'test_hatband'])
    captured = capsys.readouterr()
    assert "{'hatband': 'test_hatband', 'key': 'key1', 'value': 'value1'}" in captured.out
    assert "{'hatband': 'test_hatband', 'key': 'key2', 'value': 'value2'}" in captured.out


