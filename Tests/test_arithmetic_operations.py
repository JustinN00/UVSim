import unittest
from UVSim.cpu import CPU
from UVSim.arithmetic_operations import perform_operation

class TestArithmeticOperations:
    def test_add(self):
        test_cpu = CPU()
        test_cpu.memory[0] = 10
        test_cpu.accumulator = 15
        perform_operation(test_cpu, 30, 0)
        assert test_cpu.accumulator == 25

    def test_sub(self):
        test_cpu = CPU()
        test_cpu.memory[0] = 10
        test_cpu.accumulator = 15
        perform_operation(test_cpu, 31, 0)
        assert test_cpu.accumulator == 5

    def test_div(self):
        test_cpu = CPU()
        test_cpu.memory[0] = 10
        test_cpu.accumulator = 20
        perform_operation(test_cpu, 32, 0)
        assert test_cpu.accumulator == 2

    def test_div_by_zero(self):
        test_cpu = CPU()
        test_cpu.memory[0] = 0
        test_cpu.accumulator = 10
        division_error = False
        try:
            perform_operation(test_cpu,32, 0)
        except ZeroDivisionError:
            division_error = True
        assert division_error

    def test_mult(self):
        test_cpu = CPU()
        test_cpu.memory[0] = 2
        test_cpu.accumulator = 10
        perform_operation(test_cpu, 33, 0)
        assert test_cpu.accumulator == 20

    def test_invalid_op(self):
        test_cpu = CPU()
        error = False
        try:
            perform_operation(test_cpu, 1, 0)
        except ValueError:
            error = True
        assert error

    def test_invalid_memory(self):
        test_cpu = CPU()
        error = False
        try:
            perform_operation(test_cpu, 30, -1)
        except ValueError:
            error = True
        assert error


if __name__ == "__main__":
    unittest.main()