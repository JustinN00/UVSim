# I/O Operations

# Read a word from the keyboard into a specific location in memory
def read(cpu, user_input, address: int): 
    cpu.memory.store(address, user_input)
    
# Write a word from a specific location in memory to screen
def write(cpu, address: int) -> str:
    value = cpu.memory.load(address)
    return f"WRITE value (from memory[{address:02d}]): {value:+05d}"