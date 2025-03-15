import unittest
from click.testing import CliRunner
import json
import os



# Import Click group from hatband_cli_v0_003
from hatband_cli_v0_004 import hatband_group

print(os.path.abspath("hatband_cli_v0_003.py"))

HATBAND_STORAGE = "test_hatband_storage"



class TestCli(unittest.TestCase):

    version = "v0.004"

    def setUp(self):
        self.runner = CliRunner()
        self.temp_dir = self.runner.isolated_filesystem()
        self.temp_dir.__enter__()
        self.storage_dir = os.path.join(os.getcwd(), HATBAND_STORAGE)
        os.makedirs(self.storage_dir)

    def tearDown(self):
        for filename in os.listdir(self.storage_dir):
            os.remove(os.path.join(self.storage_dir, filename))
        os.rmdir(self.storage_dir)
        self.temp_dir.__exit__(None,None,None)

    def test_insertl(self):
        result = self.runner.invoke(hatband_group, [
            "insertl",
            "--hatband-name", "test_hatband",
            "--key", "test_key",
            "--value", "test_value",
            "--storage-dir", self.storage_dir
        ])
        if result.exception:
            print(result.output)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Inserted at index: 0", result.output)

        with open(os.path.join(self.storage_dir, "test_hatband.json"), "r") as f:
            data = json.load(f)
            self.assertEqual(data, [{"hatband": "test_hatband", "key": "test_key", "value": "test_value"}])

    def test_list_records(self):
        with open(os.path.join(self.storage_dir, "test_hatband.json"), "w") as f:
            json.dump([{"hatband": "test_hatband", "key": "test_key", "value": "test_value"}], f)

        result = self.runner.invoke(hatband_group, [
            "list_records",
            "--hatband-name", "test_hatband",
            "--storage-dir", self.storage_dir
        ])
        print(result.output)
        print(result.exception)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("{'hatband': 'test_hatband', 'key': 'test_key', 'value': 'test_value'}", result.output)

if __name__ == '__main__':
    unittest.main()