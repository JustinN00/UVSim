# arithmetic_operations.py

# Define opcodes
ADD = 30
SUBTRACT = 31
DIVIDE = 32
MULTIPLY = 33

# Create memory and accumulator
memory = [0] * 100
accumulator = 0

def load_memory(address, value):
    if 0 <= address < len(memory):
        memory[address] = value
    else:
        raise ValueError("Invalid memory address.")

def set_accumulator(value):
    global accumulator
    accumulator = value

def get_accumulator():
    return accumulator

def perform_operation(opcode, address):
    global accumulator
    if address < 0 or address >= len(memory):
        raise ValueError("Invalid memory address.")

    value = memory[address]

    if opcode == ADD:
        accumulator += value
    elif opcode == SUBTRACT:
        accumulator -= value
    elif opcode == DIVIDE:
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        accumulator //= value
    elif opcode == MULTIPLY:
        accumulator *= value
    else:
        raise ValueError("Invalid opcode.")
