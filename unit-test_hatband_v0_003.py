# unit-test_hatband_v0_003.py

import unittest
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hatband_v0_003 import Hatband, floor


# PLEASE ABIDE: Two spaces between regardless of PEP, FLAKE, or some whore dominatrix.

class TestHatband(unittest.TestCase):


    """
    def setUp(self):
        self.storage_dir = "test_hatband_storage"
        os.makedirs(self.storage_dir, exist_ok=True)
        self.hatbandFile = Hatband(storage_dir=self.storage_dir)
        self.hatbandMem = Hatband(use_memory=True)

    def tearDown(self):
        for filename in os.listdir(self.storage_dir):
            os.remove(os.path.join(self.storage_dir, filename))
        os.rmdir(self.storage_dir)

    """


    def setUp(self):
        self.storage_dir = "test_hatband_storage"
        self.hatbandFile = Hatband(storage_dir=self.storage_dir)
        self.hatbandMem = Hatband(use_memory=True)
        self.hatbandFile._data = {}
        self._reset_test_files()
        self.hatbandFile.reset_data()


    def _reset_test_files(self):
        d_short_path = os.path.join(self.storage_dir, "d-short.json")
        with open(d_short_path, "w") as f:
            json.dump([{'key': '1', 'value': 'data1', 'hatband': 'd-short'}, {'key': '2', 'value': 'data2', 'hatband': 'd-short'}], f)
        e_medium_path = os.path.join(self.storage_dir, "e-medium.json")
        with open(e_medium_path, "w") as f:
            json.dump([{'key': '1', 'value': 'data1', 'hatband': 'e-medium'}, {'key': '2', 'value': 'data2', 'hatband': 'e-medium'}, {'key': '3', 'value': 'data3', 'hatband': 'e-medium'}], f)
        a_short_path = os.path.join(self.storage_dir, "a-short.json")
        with open(a_short_path, "w") as f:
            json.dump([], f)
        simple_test_path = os.path.join(self.storage_dir, "simple-test.json")
        with open(simple_test_path, "w") as f:
            json.dump([], f)

    """
    def test_file_insert_simple(self):
        self.hatbandFile.use_memory = False
        file_path = os.path.join(self.storage_dir, 'simple-test.json')
        record = {'key': 'simple', 'value': 'test', 'hatband': 'simple-test'}
        index = self.hatbandFile.hatband_insertM(record)
        self.assertEqual(index, 0)
    """

    def test_file_insert_simple(self):
        self.hatbandFile.use_memory = False
        file_path = os.path.join(self.storage_dir, 'simple-test.json')
        index = self.hatbandFile.hatband_insertR({'key': 'simple', 'value': 'test', 'hatband': 'simple-test'})
        print(f"DEBUGGING: index={index}")
        self.assertEqual(index, 0)


    def test_in_memory_insertL(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'a-short'}
        index = self.hatbandMem.hatband_insertL(record)
        self.assertEqual(index, 0)


    def test_file_insertL(self):
        self.hatbandFile.use_memory = False
        file_path = os.path.join(self.storage_dir, 'a-short.json')
        record = {'key': 'test', 'value': 'data', 'hatband': 'a-short'}
        index = self.hatbandFile.hatband_insertL(record)
        data = self.hatbandFile._load_data(file_path)
        print(f"DEBUG: {data=}")
        self.assertEqual(data, [record])


    """
    def test_file_insertL(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'a-short'}
        index = self.hatbandFile.hatband_insertL(record)
        self.assertEqual(index, 0)
        file_path = os.path.join(self.storage_dir, 'a-short.json')
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [record])
    """

    def test_file_persistence(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'a-short'}
        self.hatbandFile.hatband_insertL(record)
        retrieved_record, index = self.hatbandFile.hatband_retrieve('a-short', 'test')
        self.assertEqual(index, 0)
        self.assertEqual(retrieved_record, record)


    def test_in_memory_retrieve(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'a-short'}
        self.hatbandMem.hatband_insertL(record)
        retrieved_record, index = self.hatbandMem.hatband_retrieve('a-short', 'test')
        self.assertEqual(index, 0)
        self.assertEqual(retrieved_record, record)


    def test_file_retrieve(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'a-short'}
        self.hatbandFile.hatband_insertL(record)
        retrieved_record, index = self.hatbandFile.hatband_retrieve('a-short', 'test')
        self.assertEqual(index, 0)
        self.assertEqual(retrieved_record, record)
        

    def test_in_memory_insertM(self):
        self.hatbandMem.hatband_insertL({'key': '1', 'value': 'data1', 'hatband': 'd-short'})
        self.hatbandMem.hatband_insertL({'key': '2', 'value': 'data2', 'hatband': 'd-short'})
        record = {'key': '3', 'value': 'data3', 'hatband': 'd-short'}
        index = self.hatbandMem.hatband_insertM(record)
        self.assertEqual(index, 1)
        self.assertEqual(self.hatbandMem.categories['d-short'][1], record)


    def test_file_insertM(self):
        self.hatbandFile.categories['d-short'] = [{'key': '1', 'value': 'data1', 'hatband': 'd-short'},{'key': '2', 'value': 'data2', 'hatband': 'd-short'}]
        file_path = os.path.join(self.storage_dir, 'd-short.json')
        with open(file_path, 'w') as f:
            json.dump([{'key': '1', 'value': 'data1', 'hatband': 'd-short'}, {'key': '2', 'value': 'data2', 'hatband': 'd-short'}], f)
        record = {'key': '3', 'value': 'data3', 'hatband': 'd-short'}
        index = self.hatbandFile.hatband_insertM(record)
        self.assertEqual(index, 1)
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.assertEqual(data[1], record)


    def test_in_memory_insertR(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'b-medium'}
        index = self.hatbandMem.hatband_insertR(record)
        self.assertEqual(index, 0)
        self.assertEqual(self.hatbandMem.categories['b-medium'][0], record)

    def test_file_insertR(self):
        self.hatbandFile.use_memory = False
        file_path = os.path.join(self.storage_dir, 'a-short.json')
        index = self.hatbandFile.hatband_insertR({'key': 'test', 'value': 'data', 'hatband': 'a-short'})
        self.assertEqual(index, 0)



    """
    def test_file_insertR(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'b-medium'}
        index = self.hatbandFile.hatband_insertR(record)
        file_path = os.path.join(self.storage_dir, 'b-medium.json')
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.assertEqual(index, 0)
        self.assertEqual(data[0], record)
    """

    """
    def test_file_insertM_empty(self):
        self.hatbandFile.use_memory = False
        record = {'key': 'test', 'value': 'data', 'hatband': 'c-long'}
        index = self.hatbandFile.hatband_insertM(record)
        self.assertEqual(index, 0)
        self.hatbandFile.categories['c-long'] = self.hatbandFile._load_data(os.path.join(self.storage_dir, 'c-long.json'))
        self.assertEqual(self.hatbandFile.categories['c-long'], [record])
    """

    def test_file_insertM_empty(self):
        self.hatbandFile.use_memory = False
        file_path = os.path.join(self.storage_dir, 'a-short.json')
        index = self.hatbandFile.hatband_insertM({'key': 'test', 'value': 'data', 'hatband': 'a-short'})
        self.assertEqual(index, 0)


    """
    def test_file_insertM_even(self):
        self.hatbandFile.categories['d-short'] = [{'key': '1', 'value': 'data1', 'hatband': 'd-short'},{'key': '2', 'value': 'data2', 'hatband': 'd-short'}]
        record = {'key': '3', 'value': 'data3', 'hatband': 'd-short'}
        print(f"Data before insert: {self.hatbandFile.categories['d-short']}") #Print the data
        print(f"Record to insert: {record}") #Print the record
        index = self.hatbandFile.hatband_insertM(record)
        self.assertEqual(index, 1)
        self.assertEqual(self.hatbandFile.categories['d-short'][1], record)
    """

    def test_file_insertM_even(self):
        self.hatbandFile.use_memory = False
        file_path = os.path.join(self.storage_dir, 'd-short.json')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                print(f"Data before insert: {data}")
        record = {'key': '3', 'value': 'data3', 'hatband': 'd-short'}
        index = self.hatbandFile.hatband_insertM(record)
        self.assertEqual(index, 1)


    """
    def test_file_insertM_odd(self):
        self.hatbandFile.categories['e-medium'] = [{'key': '1', 'value': 'data1', 'hatband': 'e-medium'}, {'key': 2, 'value': 'data2', 'hatband': 'e-medium'}, {'key': '3', 'value': 'data3', 'hatband': 'e-medium'}]
        record = {'key': '4', 'value': 'data4', 'hatband': 'e-medium'}
        index = self.hatbandFile.hatband_insertM(record)
        self.assertEqual(index, 1)
        self.assertEqual(self.hatbandFile.categories['e-medium'][1], record)
    """


    """
    def test_file_insertM_odd(self):
        self.hatbandFile.use_memory = False
        file_path = os.path.join(self.storage_dir, 'e-medium.json')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                print(f"Data before insert: {data}")
        record = {'key': 4, 'value': 'data4', 'hatband': 'e-medium'}
        index = self.hatbandFile.hatband_insertM(record)
        self.assertEqual(index, 1)
    """


    def test_file_insertM_odd(self):
        self.hatbandFile.use_memory = False
        file_path = os.path.join(self.storage_dir, 'e-medium.json')
        print(f"Data before insert: {self.hatbandFile._load_data(file_path)}")
        record = {'key': 4, 'value': 'data4', 'hatband': 'e-medium'}
        index = self.hatbandFile.hatband_insertM(record)
        self.assertEqual(index, 2)


    def test_file_retrieve_exists(self):
        record = {'key': 'test', 'value': 'data', 'hatband': 'f-long'}
        self.hatbandFile.hatband_insertR(record)
        retrieved_record, index = self.hatbandFile.hatband_retrieve('f-long', 'test')
        self.assertEqual(retrieved_record, record)
        self.assertEqual(index, 0)


    def test_file_retrieve_not_exists(self):
        retrieved_record, index = self.hatbandFile.hatband_retrieve('g-short', 'nonexistent')
        self.assertEqual(retrieved_record, {})
        self.assertEqual(index, -1)


    def test_file_retrieve_with_index(self):
        self.hatbandFile.categories['h-medium'] = [{'key': '1', 'value': 'data1', 'hatband': 'h-medium'}, {'key': '2', 'value': 'data2', 'hatband': 'h-medium'}]
        file_path = os.path.join(self.storage_dir, 'h-medium.json')
        with open(file_path, "w") as f:
            json.dump([{'key': '1', 'value': 'data1', 'hatband': 'h-medium'}, {'key': '2', 'value': 'data2', 'hatband': 'h-medium'}], f)
        retrieved_record, index = self.hatbandFile.hatband_retrieve('h-medium', '2', 1)
        self.assertEqual(retrieved_record, self.hatbandFile.categories['h-medium'][1])
        self.assertEqual(index, 1)


    def test_file_retrieve_with_index_not_found(self):
        self.hatbandFile.categories['i-long'] = [{'key': '1', 'value': 'data1', 'hatband': 'i-long'}, {'key': '2', 'value': 'data2', 'hatband': 'i-long'}]
        retrieved_record, index = self.hatbandFile.hatband_retrieve('i-long', '3', 0)
        self.assertEqual(retrieved_record, {})
        self.assertEqual(index, -1)


if __name__ == '__main__':
    unittest.main()