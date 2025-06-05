# I/O Operations

from UVSim.constants import MIN_WORD_VALUE, MAX_WORD_VALUE
from UVSim.cpu import CPU


# Read a word from the keyboard into a specific location in memory
def read(cpu: CPU, address: int): 
    while True:
        try:
            value = int(input(f"READ value (store to memory[{address:02d}]): "))
            if MIN_WORD_VALUE <= value <= MAX_WORD_VALUE:
                cpu.memory[address] = value
                break
            else:
                print(f"Error: Value must be between {MIN_WORD_VALUE} and {MAX_WORD_VALUE}.")
        except ValueError:
            print("Error: Invalid input. Please enter a signed integer.")


# Write a word from a specific location in memory to screen
def write(cpu: CPU, address: int):
    value = cpu.memory[address]
    print(f"WRITE value (from memory[{address:02d}]): {value:+05d}")
