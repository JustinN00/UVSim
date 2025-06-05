# Unit Tests 

import unittest
from unittest.mock import patch
from io import StringIO
from UVSim.load_store_operations import load, store
from UVSim.cpu import CPU


class TestLoadStoreOperations(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU()

    # load() tests
    def test_load_positive(self):
        self.cpu.memory[10] = 4321
        with patch('sys.stdout', new=StringIO()) as mock_out:
            load(self.cpu, 10)
            self.assertEqual(self.cpu.accumulator, 4321)
            self.assertIn("Acc = +4321", mock_out.getvalue())

    def test_load_negative(self):
        self.cpu.memory[11] = -765
        with patch('sys.stdout', new=StringIO()) as mock_out:
            load(self.cpu, 11)
            self.assertEqual(self.cpu.accumulator, -765)
            self.assertIn("Acc = -0765", mock_out.getvalue())

    # store() tests
    def test_store_positive(self):
        self.cpu.accumulator = 123
        with patch('sys.stdout', new=StringIO()) as mock_out:
            store(self.cpu, 15)
            self.assertEqual(self.cpu.memory[15], 123)
            self.assertIn("+0123", mock_out.getvalue())

    def test_store_negative(self):
        self.cpu.accumulator = -9876
        with patch('sys.stdout', new=StringIO()) as mock_out:
            store(self.cpu, 20)
            self.assertEqual(self.cpu.memory[20], -9876)
            self.assertIn("-9876", mock_out.getvalue())

if __name__ == "__main__":
    unittest.main()
