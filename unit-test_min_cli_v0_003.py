import unittest
from click.testing import CliRunner
from hatband_cli_v0_003 import hatband_group


class TestMinimalCli(unittest.TestCase):


    def test_list_records_minimal(self):
        runner = CliRunner()
        result = runner.invoke(hatband_group, ["list_records", "--hatband-name", "test_hatband"])
        print(result.output)
        print(result.exception)
        self.assertEqual(result.exit_code, 0)

    """
    def test_list_records_simple(self):
        runner = CliRunner()
        result = self.runner.invoke(hatband_group, [
            "list_records",
            "--hatband-name", "test_hatband",
            "--storage-dir", self.storage_dir
        ])
        print(result.output)
        print(result.exception)
        self.assertEqual(result.exit_code, 2)"
    """


if __name__ == '__main__':
    unittest.main()