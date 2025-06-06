# test_control_operations.py
import unittest
from UVSim.control_operations import branch, branchneg, branchzero, halt
from UVSim.cpu import CPU


class TestControlOperations:
    def test_branch(self):
        test_cpu = CPU()
        test_cpu.instruction_counter = 1
        branch(test_cpu, 10)
        assert test_cpu.instruction_counter == 9

    def test_branchneg(self):
        test_cpu = CPU()
        test_cpu.instruction_counter = 1
        test_cpu.accumulator = 1
        branchneg(test_cpu, 10)
        assert test_cpu.instruction_counter == 1

        test_cpu.accumulator = -1
        branchneg(test_cpu, 11)
        assert test_cpu.instruction_counter == 10
    
    def test_branchzero(self):
        test_cpu = CPU()
        test_cpu.instruction_counter = 1
        test_cpu.accumulator = 1
        branchzero(test_cpu, 10)
        assert test_cpu.instruction_counter == 1

        test_cpu.accumulator = 0
        branchzero(test_cpu, 10)
        assert test_cpu.instruction_counter == 9

    def test_halt(self):
        test_cpu = CPU()
        test_cpu.instruction_counter = 1
        halt(test_cpu)
        assert test_cpu.instruction_counter == 99

if __name__ == "__main__":
    unittest.main()