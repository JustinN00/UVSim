# Unit Tests 

import unittest
from unittest.mock import patch
from io import StringIO
from UVSim.io_operations import read, write
from UVSim.cpu import CPU


class TestIOOperations(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU()

    # read() tests
    @patch('builtins.input', side_effect=['1234'])
    def test_read_valid(self, mock_input):
        read(self.cpu, 5)
        self.assertEqual(self.cpu.memory[5], 1234)

    @patch('builtins.input', side_effect=['abc', '99999', '-1234'])
    def test_read_invalid_then_valid(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            read(self.cpu, 7)
            output = mock_out.getvalue()
            self.assertIn("Invalid input", output)
            self.assertIn("Value must be between", output)
        self.assertEqual(self.cpu.memory[7], -1234)

    # write() tests
    def test_write_positive(self):
        self.cpu.memory[2] = 567
        with patch('sys.stdout', new=StringIO()) as mock_out:
            write(self.cpu, 2)
            self.assertIn("+0567", mock_out.getvalue())

    def test_write_negative(self):
        self.cpu.memory[3] = -89
        with patch('sys.stdout', new=StringIO()) as mock_out:
            write(self.cpu, 3)
            self.assertIn("-0089", mock_out.getvalue())


if __name__ == "__main__":
    unittest.main()
