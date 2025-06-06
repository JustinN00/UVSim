# Load/Store
# Load a word from a specific location in memory into the accumulator
def load(cpu, address: int):
    cpu.accumulator = cpu.memory[address]
    print(f"LOAD memory[{address:02d}] into accumulator. Acc = {cpu.accumulator:+05d}")


# Store a word from the accumulator into a specific location in memory
def store(cpu, address: int):
    cpu.memory[address] = cpu.accumulator
    print(f"STORE accumulator into memory[{address:02d}]. memory[{address:02d}] = {cpu.accumulator:+05d}")