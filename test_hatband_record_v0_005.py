# test_hatband_record_v0_005.py

import pytest
from hatband_record_v0_005 import Record

"""
def test_successful_record_creation():
    content_chunk = "This is a valid content chunk."
    record = Record(content_chunk)
    assert record.content_chunk == content_chunk
    assert record.short_index_key == content_chunk[:5]
    assert record.medium_index_key == content_chunk[:25]
    assert record.long_index_key == content_chunk[:50]
    assert record.value == content_chunk
"""

def test_successful_record_creation():
    content_chunk = "This is a valid content chunk."
    record = Record(content_chunk)
    assert record.content_chunk == content_chunk

def test_value_error_on_short_content_chunk():
    with pytest.raises(ValueError) as excinfo:
        Record("abcd")
    assert "Content chunk must be at least 5 characters long." in str(excinfo.value)


def test_correct_key_generation():
    content_chunk = "This is a test content chunk."
    record = Record(content_chunk)
    assert record.short_index_key == "This "
    assert record.medium_index_key == "This is a test content ch"
    assert record.long_index_key == "This is a test content chunk."


def test_to_dict_method():
    content_chunk = "Test content"
    record = Record(content_chunk)
    record_dict = record.to_dict()
    assert record_dict['short_index_key'] == "Test "
    assert record_dict['medium_index_key'] == "Test content"
    assert record_dict['long_index_key'] == "Test content"
    assert record_dict['value'] == content_chunk


def test_index_key_edge_cases():
    content_chunk_short_medium = "12345678901234567890123"
    record_short_medium = Record(content_chunk_short_medium)
    assert record_short_medium.medium_index_key == content_chunk_short_medium
    content_chunk_medium_long = "1234567890123456789012345678901234567890123456789"
    record_medium_long = Record(content_chunk_medium_long)
    assert record_medium_long.long_index_key == content_chunk_medium_long







