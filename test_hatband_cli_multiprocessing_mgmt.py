# test_hatband_cli_multiprocessing_mgmt.py

import pytest
import sys
import os
from hatband_cli_multiprocessing_mgmt import generate_index_key, generate_batch_index_keys
from unittest.mock import patch


sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def test_generate_index_key():
    with patch('hatband_cli_multiprocessing_mgmt.Record') as mock_record:
        mock_record.return_value = {'index_key': 'test_key'}
        result = generate_index_key('test_content')
        assert result == 'test_key'

def test_generate_batch_index_keys():
    with patch('hatband_cli_multiprocessing_mgmt.Record') as mock_record:
        mock_record.return_value = {'index_key': 'test_key'}
        content_chunks = ['content1', 'content2', 'content3']
        results = generate_batch_index_keys(content_chunks)
        assert results == ['test_key', 'test_key', 'test_key']


