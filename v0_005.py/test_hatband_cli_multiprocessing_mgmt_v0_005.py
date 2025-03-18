# test_hatband_cli_multiprocessing_mgmt.py

import pytest
import sys
import os
from hatband_cli_multiprocessing_mgmt_v0_009 import generate_index_key, generate_batch_index_keys
from unittest.mock import patch, MagicMock


sys.path.append(os.path.abspath(os.path.dirname(__file__)))


def test_generate_index_key():
    mock_record = MagicMock()
    mock_record.short_index_key = 'test_key'
    with patch('hatband_cli_multiprocessing_mgmt.Record', return_value=mock_record):
        result = generate_index_key('test_content')
        assert result == 'test_key'

def test_generate_batch_index_keys():
    mock_record = MagicMock()
    mock_record.short_index_key = 'test_key'
    with patch('hatband_cli_multiprocessing_mgmt.Record', return_value=mock_record):
        content_chunks = ['content1', 'content2', 'content3']
        results = generate_batch_index_keys(content_chunks)
        assert results == ['test_key', 'test_key', 'test_key']


