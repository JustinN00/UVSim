# test_arithmetic_operations.py

from arithmetic_operations import *

# Load sample values into memory
load_memory(10, 25)
load_memory(20, 5)

# Set initial accumulator value
set_accumulator(10)

# Perform operations
perform_operation(ADD, 10)        # 10 + 25 = 35
print(f"After ADD: {get_accumulator()}")  # Expected: 35

perform_operation(SUBTRACT, 20)   # 35 - 5 = 30
print(f"After SUBTRACT: {get_accumulator()}")  # Expected: 30

perform_operation(MULTIPLY, 20)   # 30 * 5 = 150
print(f"After MULTIPLY: {get_accumulator()}")  # Expected: 150

perform_operation(DIVIDE, 10)     # 150 // 25 = 6
print(f"After DIVIDE: {get_accumulator()}")  # Expected: 6

# Final result
print(f"Final Accumulator: {get_accumulator()}")  # Should print: 6
