# test_control_operations.py

from control_operations import *

# Load a small program into memory
# Assume format: (opcode * 100) + operand
# e.g., 4007 means BRANCH to address 7

load_instruction(0, 4104)  # BRANCHNEG to 04 (accumulator is not negative -> skip)
load_instruction(1, 4205)  # BRANCHZERO to 05 (accumulator is not zero -> skip)
load_instruction(2, 4006)  # BRANCH to 06 (should jump unconditionally)
load_instruction(3, 4300)  # HALT (should be skipped)
load_instruction(4, 4300)  # HALT (should be skipped unless accumulator < 0)
load_instruction(5, 4300)  # HALT (should be skipped unless accumulator == 0)
load_instruction(6, 4300)  # HALT (should be hit)

# Test 1: accumulator > 0
set_accumulator(5)
print("Test 1: Accumulator > 0")

while not is_halted():
    print(f"Executing instruction at {get_instruction_pointer()}")
    execute_instruction()

print("Program halted.\n")

# Reset state for Test 2: accumulator = 0
set_accumulator(0)
load_instruction(0, 4205)  # Change instruction to test BRANCHZERO

# Reset environment
instruction_pointer = 0
halted = False

print("Test 2: Accumulator == 0")

while not is_halted():
    print(f"Executing instruction at {get_instruction_pointer()}")
    execute_instruction()

print("Program halted.")
