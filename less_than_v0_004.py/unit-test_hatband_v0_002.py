# unit-test_hatband_v0_002.py

import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hatband_v0_002 import Hatband


class TestHatband(unittest.TestCase):

    version = "v0.002"

    def setUp(self):
        self.hatband = Hatband()

    def test_hatband_insertL(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'a-short'}
        index = self.hatband.hatband_insertL(record)
        self.assertEqual(index, 0)
        self.assertEqual(self.hatband.categories['a-short'][0], record)

    def test_hatband_insertR(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'b-medium'}
        index = self.hatband.hatband_insertR(record)
        self.assertEqual(index, len(self.hatband.categories['b-medium']) - 1)
        self.assertEqual(self.hatband.categories['b-medium'][-1], record)

    def test_hatband_insertM_empty(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'c-long'}
        index = self.hatband.hatband_insertM(record)
        self.assertEqual(index, 0)
        self.assertEqual(self.hatband.categories['c-long'], [record])

    def test_hatband_insertM_even(self):
        self.hatband.categories['d-short'] = [{'key': '1', 'value': 'data1', 'hatband': 'd-short'},{'key': '2', 'value': 'data2', 'hatband': 'd-short'}]
        record = {'key': '3', 'value': 'data3', 'hatband': 'd-short'}
        print(f"Data before insert: {self.hatband.categories['d-short']}") #Print the data
        print(f"Record to insert: {record}") #Print the record
        index = self.hatband.hatband_insertM(record)
        self.assertEqual(index, 1)
        self.assertEqual(self.hatband.categories['d-short'][1], record)
        
    def test_hatband_insertM_odd(self):
        self.hatband.categories['e-medium'] = [{'key': '1', 'value': 'data1', 'hatband': 'e-medium'}, {'key': 2, 'value': 'data2', 'hatband': 'e-medium'}, {'key': '3', 'value': 'data3', 'hatband': 'e-medium'}]
        record = {'key': '4', 'value': 'data4', 'hatband': 'e-medium'}
        index = self.hatband.hatband_insertM(record)
        self.assertEqual(index, 1)
        self.assertEqual(self.hatband.categories['e-medium'][1], record)

    def test_hatband_retrieve_exists(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'f-long'}
        self.hatband.hatband_insertR(record)
        retrieved_record, index = self.hatband.hatband_retrieve('f-long', 'test')
        self.assertEqual(retrieved_record, record)
        self.assertEqual(index, 0)

    def test_hatband_retrieve_not_exists(self):
        retrieved_record, index = self.hatband.hatband_retrieve('g-short', 'nonexistent')
        self.assertEqual(retrieved_record, {})
        self.assertEqual(index, -1)

    def test_hatband_retrieve_with_index(self):
        self.hatband.categories['h-medium'] = [{'key': '1', 'value': 'data1', 'hatband': 'h-medium'}, {'key': '2', 'value': 'data2', 'hatband': 'h-medium'}]
        retrieved_record, index = self.hatband.hatband_retrieve('h-medium', '2', 1)
        self.assertEqual(retrieved_record, self.hatband.categories['h-medium'][1])
        self.assertEqual(index, 1)

    def test_hatband_retrieve_with_index_not_found(self):
        self.hatband.categories['i-long'] = [{'key': '1', 'value': 'data1', 'hatband': 'i-long'}, {'key': '2', 'value': 'data2', 'hatband': 'i-long'}]
        retrieved_record, index = self.hatband.hatband_retrieve('i-long', '3', 0)
        self.assertEqual(retrieved_record, {})
        self.assertEqual(index, -1)


if __name__ == '__main__':
    unittest.main()